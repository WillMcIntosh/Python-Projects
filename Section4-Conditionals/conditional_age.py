def age_foo(age):
    new_age = (age) + 50
    return new_age

age_asked = int(input("Enter your age: "))

if age_asked > 50:
    print("In 50 years, you will be dead probably.  :-(" )
elif age_asked == 50:
    print("In 50 years, you might be 100. Good luck!")
else:
    print ("In 50 year, you will be" , int(age_foo(age_asked)))
