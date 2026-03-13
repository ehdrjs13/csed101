# ----------------------------------------------------
# Student ID: 20260792
# Name: 김동건
# ----------------------------------------------------

# ----------------------------------------------------
# Practice 1: Complete the function
def calc_score(score_list):
    pass # remove 'pass' and write your code here

def problem1(): # do not modify
    score_list1 = [85, 90, 78] 
    score_list2 = [99, 55, 77, 66, 88]

    avg1, max1 = calc_score(score_list1)
    print("Average: %.1f, Max: %d" % (avg1, max1)) # Average: 84.3, Max: 90

    avg2, max2 = calc_score(score_list2)
    print("Average: %.1f, Max: %d" % (avg2, max2)) # Average: 77.0, Max: 99


# ----------------------------------------------------
# Practice 2: Complete the function
def merge_list(L1, L2):
    pass # remove 'pass' and write your code here

def problem2(): # do not modify
    L = [3, 5, 9, 1, 2]
    ml1 = merge_list(L, [2, 1])
    ml2 = merge_list([6, 9, 4], L)

    print(ml1) # [1, 1, 2, 2, 3, 5, 9]
    print(ml2) # [1, 2, 3, 4, 5, 6, 9, 9]


# ----------------------------------------------------
# Practice 3: Using the random module
# use the random module
# write your code here
import random

def problem3(): # complete the function
    menu = ["Pizza", "Burger", "Pasta", "Ramen", "Salad", "Sandwich", "Chicken"]
    ans = random.choice(menu)
    print(f"Today's lunch is {ans}. ")


# ----------------------------------------------------
if __name__ == "__main__":
    #problem1() # Practice 1
    #problem2() # Practice 2
    problem3() # Practice 3
