import cv2
import json
import os 

def jsontoimg(img,jsonfile,m):
	img = cv2.imread(img)
	file = open(jsonfile,encoding='utf-8')
	setting = json.load(file)
	objects = setting['objects']#list
	top_left=[]
	bottom_right = []
	for i in range(len(objects)):
		sphere = objects[i]
		bounding_box = sphere['bounding_box']
		top_left.append(bounding_box['top_left'])
		bottom_right.append(bounding_box['bottom_right'])
	#swap a & y
	for j in range(len(objects)):
		top_left[j] = [int(i)-3 for i in top_left[j]]
		bottom_right[j] = [int(i)+3 for i in bottom_right[j]]
		cv2.rectangle(img,tuple(top_left[j][::-1]),tuple(bottom_right[j][::-1]),(0,255,0),2)
		cv2.imwrite("./output/"+str(m)+".jpg",img)

def read_json_img():
	path = './ndds/source/'
	lists = os.listdir(path)
	lists.sort()
	file_length = len(lists)-1
	lists.remove(lists[0])
	for i in range(int(file_length/2)):
		jsonfile = path+lists[2*i]
		imgfile = path+lists[2*i+1]
		jsontoimg(imgfile,jsonfile,i)

def main():
	read_json_img()

if '__name__' == '__main__':
	main()




