import cv2
import pytesseract
import string
from imutils import contours

#pip install opencv-python &&
#sudo apt-get install tesseract-ocr &&
#pip install pytesseract

class GetImageText:
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    config = r'--oem 3--psm 6'
    def __init__(self,imagepath):
        self.imagepath = imagepath
    
    def get_text(self):
        img = cv2.imread(self.imagepath)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img,config=self.config).strip()
    
    car_number = [
"AA","BA","CA","EA","HA","IA","KA","MA","OA","PA","TA","XA",
"AB","BB","CB","EB","HB","IB","KB","MB","OB","PB","TB","XB",
"AC","BC","СС","EC","HC","IC","KC","MC","OC","PC","TC","XC",
"AE","BE","CE","EE","HE","IE","KE","ME","OE","PE","TE","XE",
"AH","BH","CH","EH","HH","IH","KH","MH","OН","PH","TH","XH",
"AI","BI","CI","EI","HI","II","KI","MI","OI","PI","TI","XI",
"AK","BK","CK","EK","HK","IK","KK","MK","OK","PK","TK","XK",
"AM","BM","CM","EM","HM","IM","КМ","MM","OM","PM","TM","XM",
"AO","BO","CO","EO","HO","IO","KO","MO","OO","PO","TO","XO",
"AP","ВР","CP","EP","HP","IP","KP","MP","OP","PP","TP","XP",
"AT","BT","CT","ET","HT","IT","KT","MT","OT","PT","TT","XT",
"AX","BX","CX","EX","HX","IX","KX","MX","OX","PX","TX","ХХ"
    ]
    def get_car_number(self):
        img = cv2.imread(self.imagepath)
        height, width, _ = img.shape
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts, _ = contours.sort_contours(cnts[0])
        for c in cnts:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            if area > 1000:
                sector = img[y:y+h, x:x+w]
                dirty = pytesseract.image_to_string(sector,config=self.config).strip()
                result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                cv2.rectangle(result,(x,y),(x+w,y+h),(0,0,255),thickness=3)
                cv2.imshow("perfect",result)
                cv2.waitKey(0)
                if dirty != "": print(dirty)
                if len(dirty) < 8:
                    continue
                else:
                    clear = ""
                    for i in dirty:
                        if i in string.ascii_uppercase or i in string.digits:
                            clear += i
                        else:
                            dirty.replace(i,"")
                    while True:
                        if str(clear[0]+clear[1]) in self.car_number and clear[2] in string.digits:
                            cv2.imshow("Number",sector)
                            result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                            cv2.rectangle(result,(x,y),(x+w,y+h),(0,0,255),thickness=3)
                            cv2.imshow("perfect",result)
                            cv2.waitKey(0)
                            return clear[0:8]
                        else:
                            clear = clear[1::]
        return "Can not found full number"
        
    def get_car_number_eagle(self, img = None):
        if img == None:
            img = cv2.imread(self.imagepath)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_filter = cv2.bilateralFilter(gray,11,15,15)
        edges = cv2.Canny(gray,30,200)
        cv2.imshow("None",edges)

    def get_car_numberm(self):
        img = cv2.imread(self.imagepath)
        height, width, _ = img.shape
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts, _ = contours.sort_contours(cnts[0])
        clear = ""
        numbers = []
        cntours = []
        for c in cnts:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            if area > 1000:
                sector = img[y:y+h, x:x+w]
                dirty = pytesseract.image_to_string(sector,config=self.config).strip()
                #if dirty != "": print(dirty)
                clear = clear + dirty
                if len(dirty) > 7:
                    cntours.append((x,y,w,h))
        if len(clear) >= 8:
            temp = clear
            clear = ""
            for c in cntours:
                result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                cv2.rectangle(result,(c[0],c[1]),(c[0]+c[2],c[1]+c[3]),(0,0,255),thickness=3)
                cv2.imshow("perfect",result)
                cv2.waitKey(0)
            for i in range(0,len(temp)):
                if temp[i] in string.ascii_uppercase or temp[i] in string.digits:
                    clear += temp[i]
            if len(clear) > 7:
                while True:
                    if str(clear[0]+clear[1]) in self.car_number and clear[2] in string.digits:
                        numbers.append(clear[0:8])
                        if len(clear[8::]) > 7:
                            clear = clear[8::]
                        else:
                            break
                    else:
                        clear = clear[1::]
            else:
                pass
        else:
            numbers.append("Can not found full number")
        result = []
        for i in numbers:
            if not i in result:
                result.append(i)
        return result