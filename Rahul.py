def percentage(a,b,c,d,e,f):
    sum=a+b+c+d+e+f
    per=(sum/6)
    return per

english=int(input("Enter English marks:"))
hindi=int(input("Enter Hindi marks:"))
kannada=int(input("Enter Kannada marks:"))
maths=int(input("Enter Maths marks:"))
science=int(input("Enter Science marks:"))
social=int(input("Enter Social marks:"))

percent=percentage(english,hindi,kannada,maths,science,social)
print(percent)

if (percent >= 90 and percent <= 100):
    print("Excellent A grade")
elif (percent >= 80 and percent <= 90):
    print("Very Good B Grade")
elif (percent >= 70 and percent <= 80):
    print("Good C Grade")
elif(percent >=45 and percent <= 70):
    print("Pass ")
else:
    print("Failed")