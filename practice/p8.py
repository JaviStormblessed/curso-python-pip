lst = [2, 3, 5, 6, 33, 5, 44, 33, 29]

def maximun(x):
    max = x[0]
    for i in x:
        if i> max:
            max = i
    print("max=", max)            

maximun(lst)