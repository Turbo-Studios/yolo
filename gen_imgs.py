import cv2
import os

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
if not cap.isOpened():
    print("can't open the webcam")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("pix:".format(width, height))
output_dir='output_images'
os.makedirs(output_dir,exist_ok=True)
img_counter=0
while True:
    ret,frame=cap.read()  
    if not ret:
        break
    cv2.imshow('Webcam',frame)
    k=cv2.waitKey(1)
    if k%256==27:
        print("Escape hit,closing...")
        break
    elif k%256==ord('s') : #s save frame
        img_name=os.path.join(output_dir,"opencv_frame_{}.png".format(img_counter))
        cv2.imwrite(img_name,frame)
        print("{} 已儲存".format(img_name))
        img_counter+=1 
cap.release()
cv2.destroyAllWindows()
