Practice Questions


1. What are the two values of the Boolean data type? How do you write them?

A.True and False,we write True and False (T and F be capital).


2. What are the three Boolean operators?

A.and, or, not


3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to)

A. truth table of and
	T and F is false
	Fand Tis false
	F and F is false
	T and T is true
 truth table of or 
	T or F is true
	F or T is true
	T or T is true
	F or F is false
 truth table of not
	not T is false
	not F is true


4. What do the following expressions evaluate to?

	(5 > 4) and (3 == 5)
	not (5 > 4)
	(5 > 4) or (3 == 5)
	not ((5 > 4) or (3 == 5))
	(True and True) and (True == False)
	(not False) or (not True)

A.

	False

	False

	True

	False

	False

	True

5. What are the six comparison operators?

A.>,>=.<,<=,==,!=

6. What is the difference between the equal to operator and the assignment operator?

A.Equal to opertor evaluates whether the two values are same or not. And assignment operator stores a value in a variable


7. Explain what a condition is and where you would use one.

A.A condition is an expression which will evaluates to boolean value.It is used in flow control statements.

8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam'

A.The output will be spam (executes print('spam') because in any the block of if statements the conditation is not true so the statements is not executed in any the blocks.


9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

A.

if (spam==1):
    print('Hello')
elif (spam==2):
    print('Howdy')
else:
    print('Greetings!')


10. What keys can you press if your program is stuck in an infinite loop?

A.CTRL-C


11. What is the difference between break and continue?

A. Brings the Program control goes outside the flow control statements by skipping the rest of the statements within the block when break statement is used and when continue statement is used it brings the program control to the begining of the loop by skipping the rest of the statements within the block.


12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

A.The difference between these is what are the values are taken in range() and all have the same number of range. In range(10) it take values from 0 to 9 and in range(0,10) it takes the values from 0 to 9 (in python), and in range(0,10,1) it takes values from 0 and incremented values by 1 till 10.



13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop

A.

for i in range (1,11):
    print(i)


n=1
while n<=10:
     print(n)
     n+=1


14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

A.It can be called with spam.bacon()


	