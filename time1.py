from datetime import datetime

conti = ''

while True: 
    first_min = 15
    first_min_price =2
    price = 0.40
    print('1. Scooter \n2. Bike')
    type = input()
    if type == "1" :
        first_min = 0
        price = 0.50
        first_min_price = 0
    
    # start time and end time
    print('start time')
    st = input()
    print('End time')
    ed = input()
    if ":" in st and ":" in ed :
        start_time = datetime.strptime(st, "%H:%M")
        end_time = datetime.strptime(ed, "%H:%M")
        # get difference
        delta = end_time - start_time
        sec = delta.total_seconds()
        min = sec / 60
        
        trip_fare = (min - first_min)* price + first_min_price
        # minnm = minn * 0.40 + 2
        print('Difference in minutes:', min)
        print('trip cost', round(trip_fare,4) )
        print('Another one?')
        conti = input()
        if conti == "y" or conti == "Y":
            
            continue
            
        else:
            break
    else:
        print("wrong input")
        continue    
    # # get difference in hours
    # hours = sec / (60 * 60)
    # print('difference in hours:', hours )

