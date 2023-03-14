import os
import cv2

path="Images/"
img=[]

for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in [".png",".gif",".jpg","jpeg",".jfif"]:
        fileName=path+"/"+file
        img.append(fileName)

print(len(img)) 
count=len(img)
frame=cv2.imread(img[0])
height,width,layers=frame.shape
size=(width,height)
out=cv2.VideoWriter("name.avi",cv2.VideoWriter_fourcc(*'DIVX'),.8,size)

for i in range(0,count):
  print(img[i])
  frame=cv2.imread(img[i])
  out.write(frame)
out.release()
print("done")  