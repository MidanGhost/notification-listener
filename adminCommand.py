import os
from pushbullet import PushBullet

def adminCommand(masg):
    access_token = "o.mBGplKdbbFig9RrbETUFXADRttI1iHpd"
    pb = PushBullet(access_token)
    if masg =="/remote":

        print(masg)
        os.startfile("C:\Program Files (x86)\TeamViewer\TeamViewer.exe")
        pb.push_note("System","Remote access has been activated ✔️\nAccess ID: 1691180062")

    elif masg=="/off":
            print("Turnd Off")
            pb.push_note("System","Script has been Turned off 😴")
            os._exit(0)

    elif masg=="/test":
        pb.push_note("System","Working ✔️")
        print("Testing")  

    elif masg=="/info":
        pb.push_note("System","1-remote\n2-off")

    else:
          pb.push_note("Dev",masg)
        # pb.push_note("WhatsApp","🤬")
