def fact(a):
    num = 1
    for i in range(1, a + 1):
        num = num*i
    
    print("the factorial of ", a, "is ", num)

fact(4)
