from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"E:\Capstone\Tesseract\tesseract.exe"

def extract_text_from_image(image_path):
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = "C:/Users/lalit/OneDrive/Pictures/Screenshots/Screenshot 2024-04-15 104323.png"
    text = extract_text_from_image(image_path)
    print(text)
