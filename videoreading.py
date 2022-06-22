import cv2

class ReadVideo():
    def __init__(self,videopath):
        self.videopath=videopath

    def getallfaces(self):
        img = cv2.imread(self.imgpath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('face.xml')
        results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
        for (x,y,w,h) in results:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), thickness=3)
        cv2.imshow("Result",img)
        cv2.waitKey(0)
    
    def readvideofaces(self):
        cap = cv2.VideoCapture(self.videopath)
        #cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #img = cv2.Canny(gray,100,140)
            faces = cv2.CascadeClassifier('face.xml')
            results = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            for (x,y,w,h) in results:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), thickness=3)
            cv2.imshow("Result",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            