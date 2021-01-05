def collatz(number):
    while(not(number==1)):
        print (number)
        if (number %2==0):
            number=number//2
        else:
            number=3*number + 1

    print(number)
n=int(input())
collatz(n)
