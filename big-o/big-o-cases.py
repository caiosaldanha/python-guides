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
[1, 2, 3, 4]  # 1st step
[1, 2]  # 2nd step
[1]  # 3rd step


# Different terms = O(a + b) = O(a) + O(b)
def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


# Big O list
# =======================================================

my_list = [11, 3, 23, 7]

my_list.append(17)  # O(1)
# >> my_list = [11,3,23,7,17] => no reindexing

my_list.pop()  # O(1) = remove 17
# >> my_list = [11,3,23,7]

my_list.pop(0)  # O(n) = remove 11
# >> my_list = [3,23,7] => reindexing

my_list.insert(0, 11)  # O(n) = insert 11
# >> my_list = [11,3,23,7] => reindexing

my_list.insert(1, 'Hi')  # O(n) = insert 'Hi'
# >> my_list = [11,'Hi',3,23,7] => reindexing


# Cheat Sheets
# =======================================================
# << https://www.bigocheatsheet.com/ >>