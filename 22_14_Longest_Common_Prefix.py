class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        ret = ""

        # 這個zip(*variable)的用法，如果已經到達最短的字串，那它就不會再繼續往下loop
        for vals in zip(*strs):
            if len(set(vals)) == 1:
                ret += vals[0]
            else:
                return ret
        return ret


    def second_method(self, stars: List[str]) -> str:
        """
        可以觀察這個寫法，怎麼處理：
        1. 當比較的i，已經到了最短string的out of bound時，它怎麼handle這個例外
        2. 在這邊，它先pick up 一個隨機的字串，從中提取字母來比較
        """
        ret = ""

        for i in range(len(strs[0])):

            for s in strs:
                if (i == len(s)) or (s[i] != strs[0][i]):
                    return ret
            ret += strs[0][i]
        return ret

