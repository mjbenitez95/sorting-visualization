def bubble_sort(arr): 
    bubbled = arr
    all_sorted = False

    while not all_sorted:
        all_sorted = True
        for i in range(1, len(bubbled)):
            if bubbled[i] < bubbled[i-1]:
                all_sorted = False
                bubbled[i-1], bubbled[i] = bubbled[i], bubbled[i-1]
    
    return bubbled

def insertion_sort(arr): 
    insertion_sorted = arr

    for i in range(1, len(insertion_sorted)): 
  
        key = insertion_sorted[i] 
        j = i-1

        while j >=0 and key < insertion_sorted[j] : 
                insertion_sorted[j+1] = insertion_sorted[j] 
                j -= 1
        insertion_sorted[j+1] = key  
    
    return insertion_sorted
    
def selection_sort(arr):
    selected = arr

    for i in range(len(selected)):
        min_index = i
        for j in range(i+1, len(selected)):
            if selected[min_index] > selected[j]:
                min_index = jumbled_array

        selected[i], selected[min_index] = selected[min_index], selected[i]
    
    return selected

def merge_sort(arr):
    merged = arr

    if(len(merged)) > 1:
        mid = len(merged)//2
        left = merged[:mid]
        right = merged[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            merged[k] = left[i]
            i += 1
            k += 1
   
        while j < len(right):
            merged[k] = right[j]
            j += 1
            k += 1

    return merged

if __name__== "__main__":
    jumbled_array = [2, 10, 1, 5, 9, 4, 6, 3, 8, 7]
    sorted_array = sorted(jumbled_array)
    bubble_sorted = bubble_sort(jumbled_array)
    insertion_sorted = insertion_sort(jumbled_array)
    selection_sorted = selection_sort(jumbled_array)
    merge_sorted = merge_sort(jumbled_array)

    print("standard_sort: ", sorted_array)
    print("bubble_sort:   ", bubble_sorted)
    print("insertion_sort:", insertion_sorted)
    print("selection_sort:", selection_sorted)
    print("merge_sort:    ", merge_sorted)