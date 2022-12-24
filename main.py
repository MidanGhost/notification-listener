from winrt.windows.ui.notifications.management import UserNotificationListener
from winrt.windows.ui.notifications import KnownNotificationBindings
from pushbullet import PushBullet
from adminCommand import *


def check(mass):
    if "+" in mass:
        check.name = " TRYKE"

    else:
        check.name = "" 

def handler(getNotif, getUsernotif):
        access_token = "*****"
        pb = PushBullet(access_token)
        app=["WhatsApp","Google Chrome"]
        admin=["Yazan2","Yazan TRYKE"]
        
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
                            adminCommand(masg)
                        else:
                            check(title)                          
                            pb.push_note(title + check.name ,masg)
                            #print(title +"("+masg_name +masg)
                       
            else:
                #print(app_name)
                pass
        else:
            pass 

print("Listening..")  
listener = UserNotificationListener.get_current()
listener.add_notification_changed(handler)
x = input()
while True:
    
    if x=="ex":
        break

    if "/" in x:
        adminCommand(x)
        x=""
    else:
        x = input()
        pass
