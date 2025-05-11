#pip install pillow (run this command in terminal to install the required library)

#Simple image resizer script using Python and Pillow library

# Image Resizer Script
from PIL import Image # type: ignore

# Ask the user for image path
image_path = input("Enter the path of the image you want to resize: ")

# Open the image
try:
    img = Image.open(image_path)
except FileNotFoundError:
    print("Image not found. Please check the path and try again.")
    exit()

# Show current size
print(f"Current size: {img.size}")

# Ask user for new width and height
new_width = int(input("Enter new width: "))
new_height = int(input("Enter new height: "))

# Resize the image
resized_img = img.resize((new_width, new_height))

# Ask for save path
save_path = input("Enter the path to save resized image (example: resized_image.jpg): ")

# Save the resized image
resized_img.save(save_path)

print(f"Image resized and saved as {save_path}")
