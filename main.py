from getcarbynumber import GetCar
from findtextinimage import GetImageText
from getfacefromimage import GetFace
from videoreading import ReadVideo

 
"""
print("==============================")
a = GetImageText('images/nomer2.jpg')
print(a.get_car_numberm())
#print(GetCar(a.get_car_numberm()[0]).getInfo())
print("==============================")
a = GetImageText('images/nomer.jpeg')
print(a.get_car_numberm())
#print(GetCar(a.get_car_numberm()[0]).getInfo())
print("==============================")
a = GetImageText('images/nomer4.jpg')
print(a.get_car_numberm())
print("==============================")
a = GetImageText('images/nomer5.jpg')
print(a.get_car_numberm())
print("==============================")
a = GetImageText('images/nomer6.jpg')
print(a.get_car_numberm())
print("==============================")"""
a = GetImageText('images/nomer7.jpg')
print(a.get_car_numberm())
print(GetCar(a.get_car_numberm()[0]).getInfo())
"""
print("==============================")
a = GetImageText('images/nomer8.png')
print(a.get_car_numberm())
print("==============================")
a = GetImageText('images/nomer9.jpg')
print(a.get_car_numberm())
print("==============================")
a = GetFace('images/faces1.webp')
a.getallfaces()
print("==============================")
a = ReadVideo("images/video1.mp4")
a.readvideofaces()"""