import os
from pushbullet import PushBullet

def adminCommand(masg):
    access_token = "******"
    pb = PushBullet(access_token)

    # Open TeamViewer to access to pc 
    if masg =="/remote":

        print(masg)
        os.startfile("C:\Program Files (x86)\TeamViewer\TeamViewer.exe")
        pb.push_note("System","Remote access has been activated ✔️\nAccess ID: **********")

    # Turn off the script 
    elif masg=="/off":
            print("Turnd Off")
            pb.push_note("System","Script has been Turned off 😴")
            os._exit(0)

    # testing the notifications 
    elif masg=="/test":
        pb.push_note("System","Working ✔️")
        print("Testing")  

    # send command list 
    elif masg=="/info":
        pb.push_note("System","1-remote\n2-off")

    # For fun :)
    else:
          pb.push_note("Dev",masg)
        # pb.push_note("WhatsApp","🤬")
