from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server
from datetime import datetime

def time():
    while True:
       # Taking input from the user
        data = input_group("Trip Calculator", [
            input('Start Time', name='start', type=TIME,
                required=True, PlaceHolder=""),
            
            input('End Time', name='end', type=TIME,
                required=True, PlaceHolder=""),
                
            input('Type', name='type', type= TEXT, required=True, 
                PlaceHolder="Scooter/ Bike ",
                datalist=['scooter', 'bike']),

            input('Penalty RM (Optional)', name='penalty', value=0 ,min=0, type=NUMBER),
            
        ])


        #Bike pricing
        first_min = 15
        price = 0.40
        first_min_price = 2
        
        # Scooter pricing
        if data['type'] == 'scooter':
            first_min = 0
            price = 0.50
            first_min_price = 0

        

        start_time = datetime.strptime(data['start'], "%H:%M")
        end_time = datetime.strptime(data['end'], "%H:%M")
        # get difference
        delta = end_time - start_time
        
      
        # Convert the difference to sec
        sec = delta.total_seconds()
        mSec = sec/1000
        
        # sec to min
        min = sec / 60

        if min <=15 and str(data['type']) == "bike" :
            # First 15 min for RM2
            trip_fare =2
        else:
            trip_fare = (min - first_min)* price + first_min_price 
        
        if min <60:
            full_time=''
        elif min == 60:
            full_time = 'One Hour ||'   
        else:
            full_time=str(delta) +' ||' 

        if data['penalty'] >0:
            #calculat penalty
            fine= (data['penalty'] / price) + min
            fare_total= trip_fare + data['penalty']
            fine_text= 'Total min with penalty: ' + str(fine) + '\nTrip fare with penalty: RM' +str(round(fare_total,4))

        else:  
            fine_text= ''

        #result
        if str(data['type']) == "scooter" and min>0 or str(data['type']) == "bike" and min>0 : 
                popup("Trip Details",
                    f"Start time: {data['start']}\nEnd time: {data['end']}\
                    \nType: {str(data['type'])}\nDuration: {full_time} {min} min || {format(mSec, '.6f')} M-sec\nTrip Fare: RM{round(trip_fare,4)}\n{fine_text}",
                    closable=True )
        
        else:   
            #Validation for negative Time         
            if min <=0:
                 toast('Negative Time is not allowed', position='center', color='red', duration=2)
            else:
                #Validation for check the type 
                toast('Wrong Type please choose Scooter or Bike', position='center', color='red', duration=2)
                
    # put_button("Reload",onclick=lambda: run_js('window.location.reload()'))

if __name__ == '__main__':
    
    start_server(time, port=80)
    
    


    