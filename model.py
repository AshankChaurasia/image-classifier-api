import torch
from torchvision import models, transforms
from PIL import Image
import urllib.request
import json

model = models.resnet50(pretrained=True)
model.eval()

url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
with urllib.request.urlopen(url) as f:
    labels = json.load(f)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

def predict(image_path):
    img = Image.open(image_path).convert("RGB")
    tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(tensor)
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    top_prob, top_idx = torch.topk(probabilities, 3)
    return {
    "predictions": [
        {"result": labels[top_idx[i]], 
         "confidence": round(top_prob[i].item() * 100, 2)}
        for i in range(3)
    ]
    }