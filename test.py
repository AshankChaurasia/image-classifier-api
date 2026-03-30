import requests

url = "http://localhost:5000/predict"
# image_path = "abus.jpg"
# image_path = "panda.jpg"
# image_path = "jagur.png"
# image_path = "itruck.jpg"
# image_path = "elephant.jpg"
# image_path = "dog.jpg"
# image_path = "cow.webp"
# image_path = "car.jpg"
# image_path = "bus.jpg"
# image_path = "atruck.jpg"
# image_path = "acar.jpg"
# image_path = "redpanda.jpg"
# image_path = "tank.jpg"
# image_path = "tiger.jpg"

image_path = "C++ Cheatsheet - CodeWithHarry.pdf"

with open(image_path, "rb") as f:
    response = requests.post(url, files={"image": f})

print(response.json())