class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        在這邊使用slide window的作法，這是蠻重要的技巧。
        slide window有可能會有兩種情況:
        1) "abc" 之後先遇到a，這個時候，就是把slide window給減去頭
        2) "abcde" 之後遇到c，這個時候，就是把slide window給減去到d的位置，仔細思考，abcde是目前遇到最大的unique substring了，
        之後就是要再從現在d的位置開始算，也就是"decxxxxx"這樣下去比較。
        """
        ret = 0
        slide_window = ""

        for letter in s:

            while letter in slide_window:
                if len(slide_window) > ret:
                    ret = len(slide_window)
                slide_window = slide_window[1:]

            slide_window = slide_window + letter

        return len(slide_window) if len(slide_window) > ret else ret


if __name__ == "__main__":
    ret = Solution().lengthOfLongestSubstring("aab")
    print(ret)