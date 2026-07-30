print ("enter the subject marks out of 100 :  ")
math = int (input("math : "))
science = int (input("science :  "))
english = int (input("english :  "))
ss = int (input("social science :  "))

total = math + science + english + ss 
average =  int(total / 4)
print(" the average is" , average)
if average in range(81, 100):

    print("Grade A")            

elif average in range(61, 80):

    print("Grade B")

elif average in range(41, 60):

    print("Grade C")

else:

    print("Grade F")