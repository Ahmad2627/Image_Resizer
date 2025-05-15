# 🖼️ Image Resizer with Python (Pillow)

A simple command-line tool written in Python that resizes images using the [Pillow](https://python-pillow.org/) library. This script allows users to load an image, specify a new width and height, and save the resized version.

---

## 📦 Requirements

Before running this script, you need to install the Pillow library (a modern fork of PIL):

bash
pip install pillow
`

---

## 🚀 Features

* Resize any image by providing the new dimensions.
* Input path and output file name are fully customizable.
* Displays the current dimensions of the selected image.
* Simple and beginner-friendly CLI interface.
* Handles missing file errors gracefully.

---

## 📂 How to Use

1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

bash
python image_resizer.py


4. Follow the prompts:

   * Enter the path to the original image.
   * Input the new width and height.
   * Enter a filename to save the resized image.

---

## 💡 Example


Enter the path of the image you want to resize: my_photo.jpg
Current size: (1920, 1080)
Enter new width: 800
Enter new height: 600
Enter the path to save resized image (example: resized_image.jpg): my_resized_photo.jpg
Image resized and saved as my_resized_photo.jpg


---

## ⚠️ Error Handling

* If the image path is invalid or the file doesn't exist, the script will show:

  
  Image not found. Please check the path and try again.
  

---

## 🛠️ Tech Stack

* **Python 3**
* **Pillow** (Python Imaging Library)

---

## 🧠 Concepts Covered

* Working with external libraries (`Pillow`)
* File I/O and image processing
* Basic error handling in Python
* User input and command-line interaction

---

## 📌 Author

**Ahmad**
GitHub: [Ahmad2627](https://github.com/Ahmad2627)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
