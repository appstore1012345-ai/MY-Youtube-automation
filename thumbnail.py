from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (1280,720), "black")
draw = ImageDraw.Draw(img)

draw.text((100,300), "MOTIVATION", fill="yellow")
img.save("thumbnail.jpg")
