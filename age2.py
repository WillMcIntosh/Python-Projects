#! /usr/bin/python

def age_foo(age):
    new_age = float(age) + 50
    return new_age

age_asked = input("Enter your age: ")
print ("In 50 year, you will be" , int(age_foo(age_asked)))
