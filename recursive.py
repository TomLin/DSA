
def my_recur(root, letters):

    if len(root) >= 3:
        print("Final")
        return

    for i, val in enumerate(letters):
        if val == None:
            print(val)
            print(root)
            continue
        else:
            print(val)
            root.append(val)
            print(root)
            tmp = letters[i]
            letters[i] = None
            print("Before", letters)

            my_recur(root, letters)
            print("After", letters)

if __name__ == "__main__":

    root = []
    letters = ["a","b","c","d"]
    my_recur(root, letters)






