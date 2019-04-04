import easygui
import object_detection_inImage
import object_detection_webcam

a=0
while(a==0):
    msg ="select 1 to detect object in a specific image and 2 for webcam?"
    title = "WELCOME TO PICTORIAL ANALYSIS"
    choices = ["1","2"]
    c = easygui.choicebox(msg, title, choices)
    if(c=="1"):
        object_detection_inImage.inImage()
    elif(c=="2"):
        object_detection_webcam.web()
    else:
        easygui.msgbox("Wrong choice")
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if easygui.ccbox(msg, title):
        a=0# show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        a=1# user chose Cancel
easygui.msgbox("Thank You for using pictorial analysis")   

    
