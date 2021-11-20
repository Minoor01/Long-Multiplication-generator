multiplicand = input("Enter the multiplicand: ").split(" ")
multiplier = input("Enter the multiplier: ").split(" ")
product = "0"*len(multiplicand)

def leftshift(string):
    temp = "0"
    for i in range(len(string)-1):
        string[i] = string[i+1]
    string[len(string)-1] = temp
    my_lst_str = ''.join(map(str, string))
    return my_lst_str

def rightshift(string):
    temp = "0"
    for i in range(len(string)-1,-1,-1):
        string[i] = string[i - 1]
    string[0] = temp
    my_lst_str = ''.join(map(str, string))
    return my_lst_str

def binaryadd(a,b):
    res = ""
    carry = 0
    a,b = a[::-1],b[::-1]

    for i in range(max(len(a),len(b))):
        digitA = ord(a[i])-ord("0") if i < len(a) else 0
        digitB= ord(a[i])-ord("0") if i < len(a) else 0
        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2
        if carry:
            res = "1" + res
    return res

def multiplifcation(multiplicand1, multiplier1, product1):
    for i in range(len(multiplier1)):
        print("******Iteration {}******".format(i+1))
        if multiplier1[len(multiplier1)-1] == 0:
            print("Before shift multiplicand: "+''.join(map(str, multiplicand1)))
            print("Before shift multiplier: "+"".join(map(str, multiplier1)))
            leftshift(multiplicand1)
            print("After shift multiplicand: "+"".join(map(str, multiplicand1)))
            rightshift(multiplier1)
            print("After shift multiplier: "+"".join(map(str, multiplier1)))
        else:
            product1 = binaryadd(multiplicand1,product1)
            print("Product is: "+product1)
            print("Before shift multiplicand: "+"".join(map(str, multiplicand1)))
            print("Before shift multiplier: "+"".join(map(str, multiplier1)))
            leftshift(multiplicand1)
            print("After shift multiplicand: "+"".join(map(str, multiplicand1)))
            rightshift(multiplier1)
            print("After shift multiplier: "+"".join(map(str, multiplier1)))

multiplifcation(multiplicand,multiplier,product)

