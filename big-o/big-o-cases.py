# Big O Notation
# Author: Caio Saldanha
# =======================================================
# Big O Notation is a way to measure the efficiency of an algorithm
# It describes how the runtime of an algorithm grows as the input grows
# It is used to compare the efficiency of different approaches to a problem
# =======================================================
# O(1) = constant
# O(n) = linear / proportional
# O(n**2) = quadratic / loop within a loop
# O(log n) = logarithmic / halving the input / divide and conquer
# =======================================================

# O(n) = proportional = linear time

def print_items(n):
    for i in range(n):
        print(i)


# Simplification techniques
# =======================================================

# Drop Constants = (n + n = 2n) = O(2n) => O(n)
def print_items(n):
    for i in range(n):
        print(i) 

    for j in range(n):
        print(j)


# O(n**2) = n squared = quadratic time => less efficient
def print_items(n):
    for i in range(n): 
        for j in range(n):
            print(i, j)


# Drop Non-Dominant = O(n + n**2) = O(n**2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

        for k in range(n):
            print(k)


# O(1) = constant time
def add_items(n):
    return n + n


# O(log n) = logarithmic time
# Ex. 8 elements in sorted list = 3 steps => log2(8) = 3 => 2**3 = 8
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
# find 1
[1,2,3,4] # 1st step
[1,2] # 2nd step
[1] # 3rd step


# Different terms = O(a + b) = O(a) + O(b)
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


# Big O list
# =======================================================

my_list = [11,3,23,7]

my_list.append(17) # O(1)
# >> my_list = [11,3,23,7,17] => no reindexing

my_list.pop() # O(1) = remove 17
# >> my_list = [11,3,23,7] 

my_list.pop(0) # O(n) = remove 11
# >> my_list = [3,23,7] => reindexing

my_list.insert(0, 11) # O(n) = insert 11
# >> my_list = [11,3,23,7] => reindexing

my_list.insert(1, 'Hi') # O(n) = insert 'Hi'
# >> my_list = [11,'Hi',3,23,7] => reindexing



# Cheat Sheets
# =======================================================
# << https://www.bigocheatsheet.com/ >>



# Other references
# =======================================================
# << https://en.wikipedia.org/wiki/Big_O_notation >>
'''
Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. Big O is a member of a family of notations invented by German mathematicians Paul Bachmann, Edmund Landau, and others, collectively called Bachmann-Landau notation or asymptotic notation. The letter O was chosen by Bachmann to stand for Ordnung, meaning the order of approximation.
In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem. Big O notation is also used in many other fields to provide similar estimates.
Big O notation characterizes functions according to their growth rates: different functions with the same asymptotic growth rate may be represented using the same O notation. The letter O is used because the growth rate of a function is also referred to as the order of the function. A description of a function in terms of big O notation usually only provides an upper bound on the growth rate of the function.
Associated with big O notation are several related notations, using the symbols o, Ω, ω, and Θ, to describe other kinds of bounds on asymptotic growth rates.
'''