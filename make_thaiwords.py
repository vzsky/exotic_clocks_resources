from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO, text_encoding

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
numbers = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ", "สิบเอ็ด", "สิบสอง"]
digits = ["", "เอ็ด", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

one = numbers[1]
sib = numbers[10]
mong = "โมง"
noon = "เที่ยง"
midnight = "เที่ยงคืน"
bai = "บ่าย"
yen = "เย็น"
tum = "ทุ่ม"
tee = "ตี"
natee = "นาที"
yee = "ยี่"
half = "ครึ่ง"

hours = [midnight] + [tee + num for num in numbers[1:6]] + [num + mong for num in numbers[6:12]] \
+ [noon, bai + mong] + [bai + num for num in numbers[2:4]] + [num + mong for num in numbers[4:7]] \
+ [num + tum for num in numbers[1:6]]

min = [num for num in numbers[1:10]] + [tens + sib + num for tens in ["", yee] + numbers[3:6] for num in digits]
minutes = [""] + [m + natee for m in min]
minutes[30] = half

numbers = [numbers[1]] + digits[1:10] + [sib] + [half, natee, yee]

# font_path = '/System/Library/Fonts/Supplemental/SukhumvitSet.ttc'
font_path = './ZF2ndPixelus.ttf'

TW_HOURS = ["TW_A0", "TW_A1", "TW_A2", "TW_A3", "TW_A4", "TW_A5", "TW_A6", "TW_A7", "TW_A8", "TW_A9", "TW_AA", "TW_AB", "TW_P0", "TW_P1", "TW_P2", "TW_P3", "TW_P4", "TW_P5", "TW_P6", "TW_P7", "TW_P8", "TW_P9", "TW_PA", "TW_PB"]
TW_NUMBERS = ["TW_NEUNG", "TW_1", "TW_2", "TW_3", "TW_4", "TW5", "TW_6", "TW_7", "TW_8", "TW_9", "TW_A", "TW_HALF", "TW_NATEE", "TW_YEE"]

def print_star_format (words, labels, font_path) :
    for i, word in enumerate(words) : 
        image = create_image_from_text(word, font_path, font_size=15, height=14)
        image = convert_grey_to_black_or_transparent(image, threshold=110) 

        image_base64 = image_to_base64(image)

        print(labels[i], " = base64.decode(\""+image_base64+"\")")


# image = create_image_from_text(hours[19], font_path, font_size=15, height=14)
# image = convert_grey_to_black_or_transparent(image, threshold=110) 
# image.show()

print_star_format(hours, TW_HOURS, font_path)
print_star_format(numbers, TW_NUMBERS, font_path)
