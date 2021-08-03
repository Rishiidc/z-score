import cv2
import time
import random
import dropbox

starttime = time.time()
def webCam():
    r = random.randint(0,5)
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        ret , frame = vco.read()
        print(ret) 
        cv2.imwrite("Person1"+str(r)+".jpg",frame)
        starttime = time.time
        result = False
        uploadfile("Person1"+str(r)+".jpg")
    vco.release()
    cv2.destroyAllWindows()

def uploadfile(img):
    accesstoken = "sl.AzOQZyoVWfE1CVXR4jtcf7Rs5Izns0b2Wayw7_KcBmJ3seukpVSjOCQ3Mtt_WzV4eGB2yQf9PnNPTXhjJGbcTEh1uFnNstxXoaTZTZwFsruFOHt197uHSRxOLaKrI26O_mB5yMlynQo"
    db1 = dropbox.Dropbox(accesstoken)
    dest = "/images/"+img
    src = img
    with open(src,'rb') as f:
        db1.files_upload(f.read(),dest,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")
    

def main():
    while(True):
        if(time.time()-starttime>=1):
            webCam()

main()
     
        
