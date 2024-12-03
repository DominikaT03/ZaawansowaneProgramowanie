import pytesseract
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text_from_image(image_path):
    try:
        image = Image.open(image_path)

        text = pytesseract.image_to_string(image, lang='eng')
        return text
    except Exception as e:
        return f"Błąd: {e}"

image_path = image_path = "C:/Users/domin/Desktop/Zaawansowane Programowanie/zajecia.jpg"
print(read_text_from_image(image_path))