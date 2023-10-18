# app.py
from fastapi import FastAPI, UploadFile
from predictor import SimilarityCalculator
import os
import uuid

app = FastAPI()
similarity_calculator = SimilarityCalculator()

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
TEMP_FOLDER = "temp_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)


@app.post("/predict/")
async def predict(files: list[UploadFile]):
    try:
        if len(files) != 2:
            return {"error": "You must upload exactly two image files."}

        file_exts = [os.path.splitext(file.filename)[1].lower() for file in files]

        for ext in file_exts:
            if ext not in ALLOWED_EXTENSIONS:
                return {
                    "error": "Both uploaded files must be in JPG, JPEG, or PNG format."
                }

        # Save the uploaded files temporarily with UUID4-based names
        image_paths = []

        for i, file in enumerate(files):
            filename = str(uuid.uuid4()) + file_exts[i]
            destination_path = os.path.join(TEMP_FOLDER, filename)
            image_paths.append(destination_path)

            with open(destination_path, "wb") as image_data:
                image_data.write(file.file.read())

        result = similarity_calculator.calculate_similarity(*image_paths)

        return result
    except Exception as e:
        return {"error": str(e)}
