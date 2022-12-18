from textwrap import indent
from winrt.windows.ui.notifications.management import UserNotificationListener
from winrt.windows.ui.notifications import KnownNotificationBindings
from pushbullet import PushBullet
import os

def check(mass):
    if "+60" in mass:
        check.name= " TRYKE"

    else:
        check.name="" 

def handler(getNotif, getUsernotif):
        app=["WhatsApp","Google Chrome"]
        admin=["Yazan2","Yazan TRYKE"]
        access_token = "o.mBGplKdbbFig9RrbETUFXADRttI1iHpd"
        pb = PushBullet(access_token)
        unotification = getNotif.get_notification(getUsernotif.user_notification_id)
        #print(getUsernotif.user_notification_id)
        # print(dir(unotification))
        if hasattr(unotification, "app_info"):
            app_name=unotification.app_info.display_info.display_name

            if  app_name in app:
                #print("App Name: ",app_name)
                text_sequence = unotification.notification.visual.get_binding(KnownNotificationBindings.get_toast_generic()).get_text_elements()
                it = iter(text_sequence)
                #print("Notification title: ", it.current.text)
                title=it.current.text
                next(it, None)
                if it.has_current:
                        masg=it.current.text
                        if title in admin :
                            
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
    
                        else:
                            check(title)                          
                            pb.push_note(title+check.name,masg)
                            #print(title +"("+masg_name +masg)
                            
            

            else:
                #print(app_name)
                pass
        else:
            pass 

print("Runing..")  
listener = UserNotificationListener.get_current()
listener.add_notification_changed(handler)
x = input()
while True:
    if x=="ex":
        break
    else:
        x = input()
        pass
