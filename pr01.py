print("Enter Your Marks in Physics : ")
phy = input()
phy=int(phy)
print("Enter Your Marks in Chemistry :")
chem= input()
chem=int(chem)
print("Enter Your Marks in Biology :")
bio= input()
bio= int(bio)
print("Enter Your Marks in Mathematics :")
maths=input()
maths=int(maths)
total = phy+chem+bio+maths
average = (total/400)*100
print("Your Marks in Physics are : " , phy)
print("Your Marks in Chemistry are :", chem)
print("Your Marks in Biology are :", bio)
print("Your Marks in Mathematics are :", maths)
print("Your Total Marks Are : ", total)
print("Your Percentage is :", average)
if(total>(0.40*400) and phy>33 and maths>33 and bio>33 and chem>33):
    print("Congrats You are Passed in The Examination !")
else:
    print("Better Luck Next Time ! :)")