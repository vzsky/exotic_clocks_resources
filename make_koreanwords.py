from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

def create_image_from_text(text, font_path='THSarabunNew.ttf', font_size=24, height=32, text_color=(255, 255, 255, 255), bg_color=(0, 0, 0, 0)):
    font = ImageFont.truetype(font_path, font_size)
    
    temp_img = Image.new('RGBA', (1, 1), color=bg_color)
    draw = ImageDraw.Draw(temp_img)
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    
    image_size = (text_width, height)
    
    img = Image.new('RGBA', image_size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # the -1 offset makes the text fit perfectly
    draw.text((0, -1), text, font=font, fill=text_color)
    
    return img

def convert_grey_to_black_or_transparent(img, threshold=90):
    pixels = img.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (r, g, b, 255 if a > threshold else 0)
    
    return img

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_base64

# Example usage
numbers = ["한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열", "열한", "열두"]
digits = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십"]

hour = "시"
minute = "분"

# font_path = '/Users/mb99n/Library/Fonts/JUA.ttf'
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"

KW_HOURS = ["KW_1", "KW_2", "KW_3", "KW_4", "KW_5", "KW_6", "KW_7", "KW_8", "KW_9", "KW_A", "KW_B", "KW_C"]
KW_MINUTES = ["KW_S1", "KW_S2", "KW_S3", "KW_S4", "KW_S5", "KW_S6", "KW_S7", "KW_S8", "KW_S9", "KW_SA"]
KW_WORDS = ["KW_HOUR", "KW_MIN"]

def print_star_format (words, labels, font_path) :
    for i, word in enumerate(words) : 
        image = create_image_from_text(word, font_path, font_size=15, height=14)
        image = convert_grey_to_black_or_transparent(image, threshold=110) 

        image_base64 = image_to_base64(image)

        # print(word, end=' ')
        print(labels[i], " = base64.decode(\""+image_base64+"\")")

# image = create_image_from_text(numbers[7], font_path, font_size=15, height=14)
# image = convert_grey_to_black_or_transparent(image, threshold=100) 
# image.show()
# image_base64 = image_to_base64(image)
# print(image_base64)

print_star_format(numbers, KW_HOURS, font_path)
print_star_format(digits, KW_MINUTES, font_path)
print_star_format([hour, minute], KW_WORDS, font_path)


