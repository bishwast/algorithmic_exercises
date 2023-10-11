"""
Find if a number is present in a sorted array that has been circularly rotated.
For example, in array [4,5,6,7,0,1,2,3].
Solution:
1- Start in the middle of the list and compare the middle number to the one you are looking for.
2. If the number matches, it's done.
3. If the number doesn't match, check if the left or right of the list is sorted. This can be done
    by comparing the middle number to the first number in the list.
4. If the left half is sorted and the target number is within the range of the left half, search in the left half.
    Else, search in the right half.
5. If the right half is sorted and the target number is within the range of the right half, search in the right half.
    Else, search in the left half.
6. Repeat these steps in the selected half of the list until the desired number is found, or determined that it's
    not there.
"""

def num_in_rotated_sorted_array(arr, target_num):
    lower_num, higher_num = 0, len(arr)-1

    while lower_num <=higher_num:
        mid_num = (lower_num + higher_num) // 2

        if arr[mid_num] == target_num:
            return mid_num

        if arr[mid_num] >= arr[lower_num]:
            if target_num >= arr[lower_num] and target_num < arr[mid_num]:
                higher_num = mid_num - 1
            else:
                lower_num = mid_num + 1
        else:
            if target_num > arr[mid_num] and target_num <= arr[higher_num]:
                lower_num = mid_num + 1
            else:
                higher_num = mid_num -1
    return -1

arr = [4,5,6,7,0,1,2]
# 3 is not in the list so output is -1.
target_num = 3
result = num_in_rotated_sorted_array(arr, target_num)
if result !=-1:
    print(f"Field Element {target_num} found at position {result}.")
else:
    print(f"Field element {target_num} not found in the array.")