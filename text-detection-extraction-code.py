import cv2
import string
import pytesseract
import os

# Set the correct path to your Tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = r"E:\Capstone\Tesseract "

# Path to your image (update this to your local path)
image_path = r"C:\Users\lalit\OneDrive\Pictures\Screenshots\Screenshot 2024-04-15 103649.png"

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
    exit()

# Reading image
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print(f"Error: Unable to load the image from {image_path}")
    exit()

# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect texts from image
try:
    texts = pytesseract.image_to_string(img)
    print("Detected text:")
    print(texts)
except Exception as e:
    print(f"Error in text detection: {e}")
    exit()

conf = r'-c tessedit_char_whitelist=' + string.digits

def draw_boxes_on_character(img):
    img_height, img_width = img.shape[:2]
    boxes = pytesseract.image_to_boxes(img, config=conf)
    for box in boxes.splitlines():
        box = box.split()
        if len(box) >= 5:
            character, x, y, x2, y2 = box[0], int(box[1]), int(box[2]), int(box[3]), int(box[4])
            cv2.rectangle(img, (x, img_height - y), (x2, img_height - y2), (0, 255, 0), 1)
            cv2.putText(img, character, (x, img_height - y2), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 1)
    return img

def draw_boxes_on_text(img):
    raw_data = pytesseract.image_to_data(img)
    for count, data in enumerate(raw_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                x, y, w, h, content = int(data[6]), int(data[7]), int(data[8]), int(data[9]), data[11]
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 1)
                cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
    return img

# Uncomment one of these lines based on your preference
# img = draw_boxes_on_character(img)
img = draw_boxes_on_text(img)

# Show the output
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()