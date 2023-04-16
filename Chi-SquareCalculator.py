print("|a|b|\n----\n|c|d|")
while 1:
    a = float(input("请输入a:"))
    b = float(input("请输入b:"))
    c = float(input("请输入c:"))
    d = float(input("请输入d:"))
    Ka = ((a*d-b*c)*(a+b+c+d))**2/((a+c)*(b+d)*(a+b)*(c+d)) 
    print("卡方 =",Ka)