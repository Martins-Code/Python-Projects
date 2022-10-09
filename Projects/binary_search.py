def binary_search(list, target):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Steps", steps, ":", str(list[start:end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        elif target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = list(map(int, input("Enter Number separated by space: ").split()))

target = int(input("Enter Target: "))

if target in my_list:
    binary_search(sorted(my_list), target)
else:
    print("Number is not in List")
