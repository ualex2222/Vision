import cv2

class GetFace:
    def __init__(self,imgpath):
        self.imgpath = imgpath
    
    def getallfaces(self):
        img = cv2.imread(self.imgpath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('face.xml')
        results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
        for (x,y,w,h) in results:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), thickness=3)
        cv2.imshow("Result",img)
        cv2.waitKey(0)

    