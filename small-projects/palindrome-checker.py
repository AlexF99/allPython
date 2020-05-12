#palindrome checker

def checker(string):
    right = []
    left = []

    if len(string) % 2 != 0:

        #right side of the string
        for n in range(len(string)//2):
            right.append(string[n])

        for x in range(len(string)):
            left.append(string[x])

        del (left[0:len(left) // 2 + 1])

        left.reverse()

        if(right == left):
            print("palindrome!")
        else:
            print("not a palindrome!")

    else:
        print("not a palindrome!")

checker(input("check if its a palindrome: "))

