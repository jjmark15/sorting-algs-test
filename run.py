from methods import quickSort, mergeSort, insertionSort, bubbleSort
from random import shuffle
from time import clock


def timer(method, m_name, arr):
    ts = clock()  # start timer

    method(arr)  # run method

    te = clock()  # end timer
    td = te - ts  # time delta
    print('{}\nCalc Time: {}s\n'.format(m_name, round(td, 5)))


def main():
    arr = list(range(int(5e5)))
    shuffle(arr)
    timer(sorted, 'TimSort', arr)
    timer(quickSort, 'QuickSort', arr)
    timer(mergeSort, 'MergeSort', arr)
    # timer(insertionSort, 'InsertionSort', arr)
    # timer(bubbleSort, 'BubbleSort', arr)


if __name__ == '__main__':
    main()
