# Problem 1
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def adds_up(list, k):
    for i in range(len(list)):
        for j in range(i+1, len(list)):

            if list[i] + list[j] == k:
                return True

    return False


