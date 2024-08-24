# Linear search
def linear_search():
    print("Linear search algorith:")
    data = [2, 21, 9, 33, 1, 14, 5, 4, 11, 8, 7]
    target = int(input("target = "))
    steps = 0

    for i in data:
        if i == target:
            steps += 1
            print(f"Siz qidirgan son {i}")
            print(f"{steps} ta qadam bilan topildi")
            break
        else:
            steps += 1


# Binary search
def binary_search():
    print("Binary search algorith:")
    data = [3, 1, 6, 8, 12, 4, 9, 11, 2, 10]
    target = int(input("target = "))

    long = len(data) - 1
    print("len: ", long)
    low = 0
    print("low: ", low)
    i = 0
    data.sort()
    print(data)

    while True:
        middle = (long + low) // 2
        print("middle: ", middle)
        if data[middle] == target:
            print(f"bu son {middle}-indexda joylashgan")
            i += 1
            break

        elif data[middle] < target:
            low = middle + 1

        elif data[middle] > target:
            long = middle - 1

        i += 1

    print("Qadamlar soni: ", i)