from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

ttext = input("Введите верхнюю строку мема")
btext = input("Введите нижнюю строку мема")

print("Список картинок")
print("1. Кот в очках")
print("2. Кот в ресторане")

numb = int(input("Введи номер картинки"))

if numb == 1:
    imnum = "Кот в очках.png"
elif numb == 2:
    imnum = "Кот в ресторане.png"

image=Image.open(imnum)
width,height=image.size

draw=ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf',size=70)

text=draw.textbbox((0,0),ttext, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10),ttext,font=font, fill='black')

text=draw.textbbox((0,0),btext,font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2,height - text_height - 10,),btext,font=font, fill = 'black')

image.save('new meme.jpg')