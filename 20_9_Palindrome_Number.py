class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        x = str(x)
        i = 0
        j = len(x) - 1

        while i < j:
            if int(x[i]) != int(x[j]):
                return False
            else:
                i += 1
                j -= 1

        return True

if __name__ == "__main__":

    s = Solution()
    ans = s.isPalindrome(10)
    print(ans)