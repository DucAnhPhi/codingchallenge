from transform import Transform
from database import Database

if __name__ == '__main__':
    t = Transform()
    db = Database("palindromes.db")
    try:
        db.create_palindrome_table()
    except:
        print("'palindromes' table was already created")
    while True:
        num = int(input("Enter a number to compute a palindrome: "))
        p = t.palindrome_w_cycles(num)
        print("Palindrome: {}".format(p[0]))
        print("Cycles: {}".format(p[1]))
        save = input("Save results to the database? Type in 'y' or 'n': ")
        if save == "y":
            db.add_palindrome(num = num, palindrome = p[0], cycles= p[1])
            print("successful save")
        show = input("Show all palindromes in database? Type in 'y' or 'n': ")
        if show == "y":
            db.show_all()