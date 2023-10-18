import torch
import clip
from PIL import Image


class SimilarityCalculator:
    def __init__(self):
        self.device = self._get_device()
        self.model, self.preprocess = self._initialize_model("ViT-B/32", self.device)
        self.cosine_similarity = torch.nn.CosineSimilarity(dim=0)
        self.image_1 = None
        self.image_2 = None
        self.raw_similarity = None

    def _get_device(self):
        return "cuda" if torch.cuda.is_available() else "cpu"

    def _initialize_model(self, model_name="ViT-B/32", device="cpu"):
        model, preprocess = clip.load(model_name, device=device)
        return model, preprocess

    def _embed_image(self, image_path):
        preprocessed_image = (
            self.preprocess(Image.open(image_path)).unsqueeze(0).to(self.device)
        )
        image_embeddings = self.model.encode_image(preprocessed_image)
        return image_embeddings

    def calculate_similarity(self, image_path_1, image_path_2):
        self.image_1 = self._embed_image(image_path_1)
        self.image_2 = self._embed_image(image_path_2)
        self.raw_similarity = self.cosine_similarity(
            self.image_1[0], self.image_2[0]
        ).item()
        return self.raw_similarity
