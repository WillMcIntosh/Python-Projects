"""
Exercise 5 from Udemy python course. This is a doc string created by 3 quotes and accessed by typing
Exercise5.__doc__ in the interactive shell
"""


temperatures=[10,-20,-289,100]

def CtoF(temp_C):
    temp_F = (temp_C * 9/5) + 32
    return temp_F

with open('/home/will/projects/Udemy_python/files/Exercise5.txt','a+') as file:
    for temp in temperatures:
        if temp > -273.15:
            file.write(str(CtoF(temp)) + '\n')
