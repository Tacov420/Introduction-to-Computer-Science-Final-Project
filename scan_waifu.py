from PIL import Image

col = Image.open("TNT.jpg")
gray = col.convert('L')
threshold = 120
bw = gray.point(lambda x: 0 if x<threshold else 255, '1')
bw.save("tnt_.jpg")