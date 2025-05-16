#lecture number 4 exercise.
#lets goo im coidng on arch linux it take me 1 day to fully setup this so lets code lets fucking goo!!
#In this code we have to Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N. The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. Hint: use a loop that increments a counter—you decide when the counter should stop.

N = int(input("Type the integer which u want cube root: "))

Guess = 0

while Guess**3 < N:
    Guess += 1

if Guess**3 == N:
    print("Root of " , N ,"is" , Guess);
else:
    print("this is not a vaild cube" , N);