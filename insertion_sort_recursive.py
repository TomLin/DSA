"""
參考資源：https://www.geeksforgeeks.org/recursive-insertion-sort/
改寫成recursive的形式，需要備齊下面幾個element:
1. base case 停止條件，當arr的長度是1時，或換言之，index是0時
2. recursively sorting first n-1 elements
3. 每次向上一層的recursion，就是arr的element，多放一個進來(而前面的已經sorted好了)
"""

def recursive_insert_sort(arr, n):

    # 終止條件(n就是這個array的長度)
    if n-1 == 0:  # 當遞迴到了第0個index時，換言之長度是1時
        return

    recursive_insert_sort(arr, n-1)  # n-1這邊指的是arr往前少一個element的長度

    insert_value = arr[n-1]  # 這邊是要找index下的value，所以長度是2時，index值是1
    current_idx = n-1

    while (current_idx > 0) and arr[current_idx -1] > insert_value:
        arr[current_idx] = arr[current_idx -1]
        current_idx -= 1

    arr[current_idx] = insert_value


if __name__ == "__main__":

    arr = [4,8,2,5,1,3]
    n = len(arr)
    recursive_insert_sort(arr, n)
    print(arr)

