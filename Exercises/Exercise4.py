def CtoF(temp_C):
    if temp_C > -273.15:
        temp_F = (temp_C * 9/5) + 32
        return temp_F
    else:
        return "That Temperature is literally impossible."

temperatures=[10,-20,-289,100]

for temp in temperatures:
        print(CtoF(temp))
