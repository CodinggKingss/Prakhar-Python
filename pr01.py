#  Write a program to accept an integer.Print the largest and smallest digit present in the number.
#  example (1): if n=4623,the the output should be : Largest digit=6,Smallest digit =2
#  example(2) : if n= 2045,then the output should be : Largest digit =5 , smallest digit =0
print("Enter The Number :")
n=input()
n=int(n)
large =0
small =9
temp=n
while (temp>0):
      digit=temp%10
      if(digit>large):
        large=digit
      elif(digit<small):
        small=digit
temp=temp/10
print("The Number is = ", n) 
print("The Lrgest Digit is = ", large)
print("The Smallest Digit is = ", small)
