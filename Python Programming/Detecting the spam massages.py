 Detecting the spam massages

 print("Write Your massage:")
 massage = str(input())
 spam = {"make a lots of money","buy now","subscribe this","click this"}
 for element in spam :
     # print(element)
     if(massage in element):
         print("This massage is a spam massage.")
