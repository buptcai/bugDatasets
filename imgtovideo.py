import cv2

path = './output/'
fps = 10
size = (512,512)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('output.mp4',fourcc,fps,size)

for i in range(30):
    frame = cv2.imread(path+str(i)+'.jpg')
    videoWriter.write(frame)
videoWriter.release()