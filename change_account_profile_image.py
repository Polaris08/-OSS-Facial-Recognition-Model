#�� ����

import os
import shutil
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('./templates/haarcascade_frontalface_default.xml')

def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces ==():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

def face_setting(userName):

    print("Start face recognition. Align your face to the front cam.")
    video = cv2.VideoCapture(0)
    count = 0

    while True:
    	ret, frame = video.read()

 	if face_extractor(frame) is not None:
   	   count += 1
  	   print("Face Founded!")
   	   face = cv2.resize(face_extractor(frame),(200,200))
   	   face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

     	   file_name_path = './users/' + userName + '.jpg'
     	   cv2.imwrite(file_name_path,face)

   	else:
    	   print("Face not Found")
     	   pass
	
    	if cv2.waitKey(1)==13 or count == 1:
   	   video.release()
     	   cv2.destroyAllWindows()
      	   break

    video.release()
    cv2.destroyAllWindows()

while True:
	user = input("������ ������ �̸��� �����ּ��� : ")
	userJpg = 'users/'+ user + '/' + user + '.jpg'
	pin = int(input("pin�� �����ּ��� : "))

	if os.path.isdir('users/' + user):
		pinFile = open('users/' + user + '/pin.txt', "r")
		pinCheck = int(pinFile.readline())

		if pinCheck == pin:
			if os.path.isfile(userJpg):
				print(user, "�� ������ �缳���˴ϴ�.")
				os.remove(userJpg)
				face_setting(user)
			else:
				print(user, "�� ������ �������� �ʾ�, ���� ����մϴ�.")
				face_setting(user)
		else:
			print('pin�� ��ġ ���� �ʽ��ϴ�.')
	else:
		print(user, '�� ������ �������� �ʽ��ϴ�. ����� ���� ���ֽʽÿ�.')