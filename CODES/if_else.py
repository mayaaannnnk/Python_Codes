#if else statement...

age=input("enter your Age:")

if int(age)>=18:
    print("you can vote")

elif int(age)<18 and int(age)>=3:
    print("you can not vote")
    
else:
    print("you dumb..")