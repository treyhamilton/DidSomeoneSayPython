'''
In this program, I have created several classes that will aid in the completion and
understanding of how various sorting algorithms work in python. The format of this program
is as follows:

-class 'SortingAlgorithms' --> stores all of the sorting functions. If there is another 
soring function you would like to add, you should add it here.

-class 'SortTesting(unittest.TestCase) --> this is where all of the various test cases you 
would like to develop for your sorting algorithms can go. Below, I have already wrote several
examples of how similar test cases may look. NOTE: un-comment out "if __name__  == '__main__'"
in order for the test case suite to run.

'''
import unittest
import time
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
+--------------------+
| Sorting Algorithms |
+--------------------+
Common Sorting Algorithms Include:
Bubble Sort
Selection Sort
Insertion Sort
Shell Sort
Merge Sort
Quick Sort
'''

class SortingAlgorithms:

    def bubbleSort(alist):
        for passnum in range(len(alist)-1, 0, -1): 
            for i in range(passnum):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]

        # print(alist)
        return alist

    def selectionSort(alist):
        for i in range(len(alist)):
            min_idx = i
            for n in range(i + 1, len(alist)):
                if alist[min_idx] > alist[n]:
                    min_idx = n
            alist[i], alist[min_idx] = alist[min_idx], alist[i]

        # print(alist)
        return alist

    def insertionSort(alist):
        for i in range(1, len(alist)):
            key = alist[i]
            n = i - 1 
            while n >= 0 and key < alist[n]:
                alist[n + 1] = alist[n]
                n -= 1
            alist[n + 1] = key

        # print(alist)
        return alist

    def shellSort(alist):
        n = len(alist)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = alist[i]
                n = i
                while n >= gap and alist[n - gap] > temp:
                    alist[n] = alist[n - gap]
                    n -= gap
                alist[n] = temp
            gap //= 2

        # print(alist)
        return alist 

    def mergeSort(alist):
        if len(alist) > 1:
            mid = len(alist) // 2 #Finding the middle of the list/array
            left = alist[:mid] #Dividing the elements from the beginning of the list to the middle
            right = alist[mid:] #Dividing the elements from the middle of the list to the end
            SortingAlgorithms.mergeSort(left) #Sorting the first half by recursion
            SortingAlgorithms.mergeSort(right) #Sorting the second half by recursion
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    alist[k] = left[i]
                    i += 1
                else:
                    alist[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                alist[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                alist[k] = right[j]
                j += 1
                k += 1

        # print(alist)
        return(alist)

    def partition(alist, low, high):
        i = low - 1
        pivot = alist[high]
        for j in range(low, high):
            if alist[j] <= pivot:
                i = i + 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i + 1], alist[high] = alist[high], alist[i + 1]
        return(i + 1)

    def quickSort(alist, low, high):
        if len(alist) == 1:
            return alist
        if low < high:
            pi = SortingAlgorithms.partition(alist, low, high)
            SortingAlgorithms.quickSort(alist, low, pi - 1)
            SortingAlgorithms.quickSort(alist, pi + 1, high)

        # print(alist)
        return(alist)

class SortTesting(unittest.TestCase):

    def test1_bubbleSort(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
        expected = [2, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.bubbleSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test2_bubbleSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.bubbleSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test3_bubbleSort_oddSize(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
        expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.bubbleSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test4_selectionSort(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
        expected = [2, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.selectionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test5_selectionSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.selectionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test6_selectionSort_oddSize(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
        expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.selectionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test7_insertionSort(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
        expected = [2, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.insertionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test8_insertionSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.insertionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test9_insertionSort_oddSize(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
        expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.insertionSort(unsortedList)
        self.assertEqual(sortedList, expected)

    # def test10_shellSort(self):
    #     unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
    #     expected = [2, 10, 12, 18, 18, 39, 72, 85]
    #     sortedList = SortingAlgorithms.shellSort(unsortedList)
    #     self.assertEqual(sortedList, expected)

    def test11_shellSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.shellSort(unsortedList)
        self.assertEqual(sortedList, expected)

    # def test12_shellSort_oddSize(self):
    #     unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
    #     expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
    #     sortedList = SortingAlgorithms.shellSort(unsortedList)
    #     self.assertEqual(sortedList, expected)

    def test13_mergeSort(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
        expected = [2, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.mergeSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test14_mergeSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.mergeSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test15_mergeSort_oddSize(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
        expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.mergeSort(unsortedList)
        self.assertEqual(sortedList, expected)

    def test16_quickSort(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18]
        expected = [2, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.quickSort(unsortedList, 0, len(unsortedList)-1)
        self.assertEqual(sortedList, expected)

    def test17_quickSort_empty(self):
        unsortedList = []
        expected = []
        sortedList = SortingAlgorithms.quickSort(unsortedList, 0, len(unsortedList)-1)
        self.assertEqual(sortedList, expected)

    def test18_bubbleSort_oddSize(self):
        unsortedList = [39, 12, 18, 85, 72, 10, 2, 18, 3]
        expected = [2, 3, 10, 12, 18, 18, 39, 72, 85]
        sortedList = SortingAlgorithms.quickSort(unsortedList, 0, len(unsortedList)-1)
        self.assertEqual(sortedList, expected)

# if __name__ == '__main__':
#     unittest.main()

def generateLists(length):

    randomList = [random.randrange(1, 100) for i in range(length)]
    return(randomList)

def main():

    print('Hello World')

main()

