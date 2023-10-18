# Image Similarity Calculator

This project provides a simple image similarity calculator using the CLIP (Contrastive Language-Image Pre-training) model. It consists of two Python scripts, `predictor.py` and `app.py`, that allow you to calculate the cosine similarity between two images.

## Requirements

- Python 3.7+
- PyTorch
- CLIP (PyTorch)
- PIL (Python Imaging Library)
- FastAPI (for running app.py)

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/cobanov/fastapi-image-classification.git
cd fastapi-image-classification
```

2. Build and run the docker image

```bash
docker build -t image_similarity .
docker run -d -p 8002:8002 image_recognition
```
