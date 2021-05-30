from PIL import Image

mac = Image.open('D:\\BheemtalTrip2019\\BNHA5839.jpg')

mac.show()

print(mac.filename)

#Cropping Images

mac1 = mac.crop((0,0,100,100))

mac1.show()


print(mac.size)

halfway = 960/2

x = halfway - 300
w = halfway + 300

y = 300
h = 1280

img_final = mac.crop((x,y,w,h))

img_final.show()

mac.paste(im=img_final,box=(0,0))
mac.show()

img_final.resize((2000,2000))
img_final.rotate(180)
img_final.show()

img_final.putalpha(128)
img_final.show()

img_final.save('new.png')