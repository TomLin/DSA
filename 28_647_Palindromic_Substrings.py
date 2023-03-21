class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        ref: (neetcode youtube channel) https://youtu.be/4RACzI5-du8
        這個作者的解法思維，是分為以一個值為中心點，向左右擴散的palindrom，還有以二個值為中心點，向左右擴散的palindrom，的方式來解題。

        對我而言，我可以學習到：
        1) 雙指針的操作
        2) while的操作(更加彈性，不需要知道長度)
        3) 將複雜的問題，拆解成一個或是多個基本解，之後再依照各個基本解，加以處理
        """
        ret = 0

        # 針對單數的palindrom
        for idx, letter in enumerate(s):
            l_point = idx
            r_point = idx

            while l_point >= 0 and r_point < len(s):
                if s[l_point] != s[r_point]:
                    break
                else:
                    ret += 1
                    l_point -= 1
                    r_point += 1

        # 針對雙數的palindrom
        for idx, letter in enumerate(s):
            l_point = idx
            r_point = idx + 1

            while l_point >= 0 and r_point < len(s):
                if s[l_point] != s[r_point]:
                    break
                else:
                    ret += 1
                    l_point -= 1
                    r_point += 1
        return ret

if __name__ == "__main__":

    ret = Solution().countSubstrings("aaa")
    print(ret)