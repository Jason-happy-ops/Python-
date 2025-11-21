def collatz(number):
    while True:
        if number%2==0:
            number=number//2
            print(number)
        else:
            number=3*number+1
            print(number)
        if number==1:
            break
    return number

try:
    num = int(input("请输入数字："))

except ValueError:
    print("你可能输入的不是整数")

else:
    collatz(num)