from PIL import Image, ImageFilter

img = Image.open('images/tiger.jpg')
# вывести формат
# print(img.format)
# вывести размер
# print(img.size)
# filters
# filtered_image = img.filter(ImageFilter.SHARPEN)
# filtered_image.save("outputImages/sharpen.png", 'png')
# grey scale
# filtered_image = img.convert('L')
# filtered_image.save("outputImages/grey.png", 'png')
# показать картинку
# filtered_image.show()
# rotate
# rotated = img.rotate(90)
# rotated.save("outputImages/rotated.png", 'png')
# resize
# resized = img.resize((300, 300))
# resized.save("outputImages/resized.png", 'png')
# crop
# box = (50, 50, 100, 100)
# cropped = img.crop(box)
# cropped.save("outputImages/cropped.png", 'png')
# thumbnail
# img.thumbnail((100, 100))
# img.save("outputImages/thumbnail.png", 'png')
