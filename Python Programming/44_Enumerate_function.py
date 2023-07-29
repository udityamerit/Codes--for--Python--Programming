l1  = [ "Bhindi", "Aloo","chopsticks","chowmein"]

# i = 1 
# for item in l1:
#     if i%2 != 0:
#         print(f"jarvis please buy {item}")
#         i = i+1


for index, item in enumerate(l1):
    if index%2==0:
        print(f"jarvis please buy {item}")
