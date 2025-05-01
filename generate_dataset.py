import os
from PIL import Image, ImageDraw
import random

# Define the dataset structure
base_dir = "dataset"
categories = ["Healthy", "Disease", "Pest", "Water Stress"]
images_per_category = 10
image_size = (224, 224)

# Create directories and placeholder images
for category in categories:
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)
    
    for i in range(1, images_per_category + 1):
        img = Image.new('RGB', image_size, color=tuple(random.randint(100, 255) for _ in range(3)))
        d = ImageDraw.Draw(img)
        d.text((10, 10), f"{category} {i}", fill=(0, 0, 0))
        img_path = os.path.join(category_path, f"{category.lower().replace(' ', '')}{i}.jpg")
        img.save(img_path)

print("Dataset created at:", base_dir)
