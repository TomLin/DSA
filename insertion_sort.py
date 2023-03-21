"""
Insertion Sort 不錯的網路資源：

1. https://stackabuse.com/insertion-sort-in-python (它的程式碼寫得比較容易懂)
2. https://www.geeksforgeeks.org/insertion-sort/
3. https://www.baeldung.com/cs/insertion-vs-bubble-sort (說明insertion sort 和 bubble sort兩者的差異，
   其實兩者的time complexity一樣，但是bubble sort和insertion sort不一樣的地方在於，bubble sort牽涉到很多的swap的動作，
   這個其實是蠻耗運算資源的)
"""

def insertion_sort(arr):

    # 針對從一個unsorted element，進行sorting，最左邊(第0位)的不用比較，直接從第一個開始比
    for i in range(1, len(arr)):
        # 要進行比較的值與index
        insert_value = arr[i]
        current_idx = i

        while (current_idx > 0) and (arr[current_idx - 1] > insert_value):
            arr[current_idx] = arr[current_idx -1]
            current_idx -= 1

        arr[current_idx] = insert_value


if __name__ == "__main__":

    arr = [4,8,2,5,1,3]
    insertion_sort(arr)
    print(arr)



