khana = ['roti', 'sabzi', 'chawal', 'daal', 'aachar']

# else is use in for loop when and only when break is not present or if you want to use the break statement in your loop then you can use the break if the items is not present inside the khana list

for i in khana:
        print(i)

else:
        print("this for loop ended properly")


# else with for loop

for i in khana:
        if i=='paratha':
                break

else:
        print('pratha is not present in your khana')