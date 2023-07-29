import time

initial = time.time()

k = 0
while(k<5):
    print("this is anuj")
    k+=1
print(f"time to run the while loop: {time.time()-initial}")

initial2  = time.time()
for i in range(5):
    print("this is anuj")

print(f"time to run the for loop: {time.time()-initial2}")

localtime = time.asctime(time.localtime(time.time()))
print(localtime) #for print the current time 

time.sleep(1) # it is use for the stop the run time in seconds to the given argument in the sleep: