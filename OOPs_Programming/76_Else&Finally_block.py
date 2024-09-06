try:
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        c = a/b
        print("The result is: ", c)

# run only one either except or else:

except Exception as e:
        print("Error:", str(e))

else:
        print("The operation is successful.")

finally:
        print("upper programms are executed!")
        print("Program is terminated!")