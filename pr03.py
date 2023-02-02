print("Press 1 for Laptops ")
print("Press 2 for Desktops")
ch=input()
ch=int(ch)
if(ch==1):
     print("Enter Marked Price of The Item")
     mp=input()
     mp=int(mp)
     if(mp>=0 and mp<=25000):
         dis=0.0*mp
         fp=mp-dis
         print("Discount Given is :", dis)
         print("Final Price of the item is :", fp)
     elif(mp>25000 and mp<=57000):
         dis=0.05*mp
         fp=mp-dis
         print("Discount is :", dis)
         print("Final Price of the item is : ", fp)
     elif(mp>57000 and mp<=100000):
         dis=0.75*mp
         fp=mp-dis
         print("Discount is :", dis)
         print("Final Price of the Item is :", fp)
     elif(mp>100000):
         dis=0.1*mp
         fp=mp-dis
         print("Discount is :", dis)
         print("Final Price of the item is : ", fp)
         breakpoint
if(ch==2):
      print("Enter Marked Price of The Item")
      mp=input()
      mp=int(mp)
      if(mp>=0 and mp<=25000):
         dis=0.05*mp
         fp=mp-dis
         print("Discount Given is :", dis)
         print("Final Price of the item is :", fp)
      elif(mp>25000 and mp<=57000):
         dis=0.075*mp
         fp=mp-dis
         print("Discount is :", dis)
         print("Final Price of the item is : ", fp)
      elif(mp>57000 and mp<=100000):
         dis=0.1*mp
         fp=mp-dis
         print("Discount is :", dis)
         print("Final Price of the Item is :", fp)
      elif(mp>100000):
        dis=0.15*mp
        fp=mp-dis
        print("Discount is :", dis)
        print("Final Price of the item is : ", fp)
      else:
        print("Wrong Choice......Please recheck your choice and try again")