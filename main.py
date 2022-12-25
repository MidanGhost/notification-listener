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
        #access token from pushbullet
        access_token = "******"
        pb = PushBullet(access_token)
    
        app=["WhatsApp","Google Chrome"]
        admin=["Yazan2","Yazan TRYKE"]
        
        unotification = getNotif.get_notification(getUsernotif.user_notification_id)
        #print(getUsernotif.user_notification_id)
        # print(dir(unotification))
        if hasattr(unotification, "app_info"):
            #Get the app name 
            app_name=unotification.app_info.display_info.display_name
            if  app_name in app:

                #Get the title of notification
                text_sequence = unotification.notification.visual.get_binding(KnownNotificationBindings.get_toast_generic()).get_text_elements()
                it = iter(text_sequence)
                title=it.current.text
                
                #Get notification text 
                next(it, None)
                #check if the notification text is null or not
                if it.has_current:
                        masg=it.current.text
                        #check if the sender is admin 
                        if title in admin :
                            adminCommand(masg)
                        else:
                            #Check if the title is number 
                            check(title)
                            #Send the notification to pushbullet account                            
                            pb.push_note(title + check.name ,masg)
                       
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
    #Cmd command 
    if x=="ex":
        break

    if "/" in x:
        adminCommand(x)
        x=""
    else:
        x = input()
        pass
