"""
Recursion
- Is a way of solving a problem by having a function call itself.
- Such problems can generally be solved by iteration itself.
 Characteristics of recursions
 a. Performing the same operation multiple times with different inputs.
 b. In every step, we try smaller inputs to make the problem smaller.
 c. Base condition is needed to stop recursion else we have an infinite loop.

 Example
def openRussionDoll(doll):
    if doll == 1: # base condition
        print("All russion dolls are opened")
    else:
        openRussionDoll(doll - 1) 

When to choose recursion?
a. Can the problem be divided into smaller sub problems?
- the sub problems must be similar
b. Problems begining with;
- Design an algorithm to compute the nth..
- Write code to list the nth..
- Implement a method to compute all
c. Recusrion has also been used in other data structures such as trees and graphs
d. It is used in many other algorithms such as divide and conquer, greedy and dynamic programming.

How recursive method is stored in memory
- Stack Memory is normally used to manage function calls
- It works in a LIFO (i.e. First In Last Out) manner, using push() to insert at the top of the stack
and pop() to remove from the top of the stack.
- Every time a recursive method calls itself, the system stores it in the stack for coming back because there are other execution points left in the method
i.e. the system should remember where it stopped to call the recursive method.

"""

# non recursive method execution


def method1():
    method2()
    print("Method 1 was called") # executed last


def method2():
    method3()
    print("method 2 was called") # executed third


def method3():
    method4()
    print("method 3 was called") # executed second


def method4():
    print("Method 4 has been called") # executed first


method1()

# recursive method
def addNumbers(n):
    if n == 1:
        print(f"The value of n is {n}") # printed last
    else:
        addNumbers(n - 1)
        print(f"The value of n is {n}") # other execution points that make the function added to the stack

addNumbers(4)
# The value of n is 1 -> The value of n is 2 -> The value of n is 3 -> The value of n is 4
