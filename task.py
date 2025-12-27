from PIL import Image, ImageDraw, ImageFont
from num2words import num2words

num = int(input("Enter a number: "))
text = num2words(num).title()

img = Image.new("RGB", (600, 200), "white")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]

x = (600 - w) // 2
y = (200 - h) // 2

draw.text((x, y), text, fill="black", font=font)
img.save("number_word.png")

print("Image saved as number_word.png")
