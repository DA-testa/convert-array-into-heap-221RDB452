
def sift_down(data, i, swaps):
    min_index = i
    left_child = 2 * i + 1
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)
def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps
def main():
   try:
    n = int(input())
    a = [int(x) for x in input().split() if x.isdigit()]
    assert n == len(a)
except ValueError:
    print("Error: input must contain only integers")
    return


    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)




        
if __name__ == "__main__":
    main()


