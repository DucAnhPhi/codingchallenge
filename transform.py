class Transform(object):
    def palindrome(self, n):
        if self.is_palindrome(n):
            return n
        
        tempN = n

        while tempN < 1000000000:
            tempN = tempN + self.reverse(tempN)
            if self.is_palindrome(tempN):
                return tempN

        return -1
    
    def palindrome_w_cycles(self, n):
        if self.is_palindrome(n):
            return (n, 0)
        
        tempN = n
        cycles = 0

        while tempN < 1000000000:
            cycles += 1
            tempN = tempN + self.reverse(tempN)
            if self.is_palindrome(tempN):
                return (tempN, cycles)
        
        return (-1, cycles)
    
    def reverse(self, n):
        rev = 0
        while n > 0:
            rev = (10 * rev) + n % 10
            n //= 10
        return rev
    
    def is_palindrome(self, n):
        return n == self.reverse(n)