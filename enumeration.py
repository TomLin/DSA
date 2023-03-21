"""
枚舉法，就是排列組合，在這邊會善用recursion in for loop.因此可以閱讀下面對recursion in for loop的觀念介紹：
https://stackoverflow.com/a/55783195

- For recursion, it's helpful to picture the call stack structure in your mind.
- If a recursion sits inside a loop, the structure resembles (almost) a N-ary tree.
- The loop controls horizontally how many branches at generated while the recursion decides the height of the tree.
- The tree is generated along one specific branch until it reaches the leaf (base condition) then expand horizontally to obtain other leaves and return the previous height and repeat.

下面，我們先嘗試print出abcd四個字母的排列組合。
"""

def permutatiaons(root, letters):

    if len(letters) == 0:
        print("FINAL:", root)
        return

    for i in range(len(letters)):
        root.append(letters[i])
        val = letters.pop(i)

        permutatiaons(root, letters)
        letters.insert(i, val)
        _ = root.pop()  # 這邊的root，就像是stack資料結構的概念，last in first out


if __name__ == "__main__":
    root = []
    letters = ["a","b","c"]

    permutatiaons(root, letters)


