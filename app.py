from transform import Transform

if __name__ == '__main__':
    t = Transform()
    while True:
        num = int(input("Enter a number to compute a palindrome: "))
        p = t.palindrome_w_cycles(num)
        print("Palindrome: {}".format(p[0]))
        print("Cycles: {}".format(p[1]))