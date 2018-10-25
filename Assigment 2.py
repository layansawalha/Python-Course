#!/usr/bin/env python
# coding: utf-8

# In[8]:


print ("wrtie 1 to convert Turkish Lira to Jordanian Dinar")
print ("write 2 to convert Jordanian Dinar to Turkish Lira")
print ("write 3 to convert Turkish Lira to US dollars")
print ("Write 4 to convert Us Dollars to Turkish Lira")
print ("write 5 to convert Us Dollars to Jordanian Dinar")
print ("Write 6 to convert Jordanian Dinar to Us Dollars")
choice=input("Choose from 1-6 ")
if choice == "1":
    TL = float(input("Enter Turkish Lira "))
    print ("Jordanian Dinar=:" , TL*0.12424)
elif choice == "2":
    JD = float(input("Enter Jordanian Dinar"))
    print ("Tukrish Lira=" , JD*8.04917)
elif choice == "3":
    TL = float(input("Enter Turkish Lira "))
    print("US Dollars=" , TL*0.175156)
elif choice == "4":
    USD= float(input("Enter Dollars"))
    print("Turkish Lira=" , USD*5.71)
elif choice == "5":
    USD= float(input("Enter Dollars"))
    print("Jordanian Dinar=" , USD*0.71)
elif choice == "6":
    JD= float(input("Enter JOD"))
    print("US Dollars=" , JD*1.41)
else:
    print ("input error")


# In[ ]:





# In[ ]:




