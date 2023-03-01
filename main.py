from winrt.windows.ui.notifications.management import UserNotificationListener
from winrt.windows.ui.notifications import KnownNotificationBindings
from pushbullet import PushBullet
from adminCommand import *
from tokens import *
def check(mass):
    if "+" in mass:
        name = " TRYKE"

    else:
        name = "" 
    return name
    
   
def handler(getNotif, getUsernotif):
        
        
        """access token from pushbullet"""
        try:
            pb = PushBullet(access_token)
        except KeyError:
            print("Error: ACCESS_TOKEN environment variable not set.")
        

        app=["WhatsApp","Google Chrome","Snip & Sketch"] #,"Snip & Sketch"
        admin=["Yazan2","Yazan TRYKE"]
        
        unotification = getNotif.get_notification(getUsernotif.user_notification_id)
        #print(getUsernotif.user_notification_id)
        # print(dir(unotification))
        if hasattr(unotification, "app_info"):
            """Get the app name""" 
            app_name=unotification.app_info.display_info.display_name
            if  app_name in app:

                """Get the title of notification"""
                text_sequence = unotification.notification.visual.get_binding(KnownNotificationBindings.get_toast_generic()).get_text_elements()
                it = iter(text_sequence)
                title=it.current.text
                
                """Get notification text""" 
                next(it, None)
                """check if the notification text is null or not"""
                if it.has_current:
                        masg=it.current.text
                        """check if the sender is admin""" 
                        if title in admin :
                            adminCommand(masg)
                        else:
                            """Check if the title is number """
                            name = check(title)
                            """Send the notification to pushbullet account"""
                                                        
                            pb.push_note(title + name ,masg)
                            
            else:
                #print(app_name)
                pass
        else:
            pass 


"""Main function for the script."""
print("Listening for notifications...")  
listener = UserNotificationListener.get_current()
listener.add_notification_changed(handler)
x = input()

while True:

    """Cmd command""" 
    if x=="ex":
        break

    if "/" in x: 
        adminCommand(x)
        x=""
    else:
        x = input()
        pass
