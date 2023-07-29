user_floor = 6
current_floor =0
difference = user_floor - current_floor
 
if difference < 0 : 
    current_floor = user_floor
    print ( " Move down ")
     
if difference > 0 : 
    current_floor = user_floor
    print ( " Move up ")