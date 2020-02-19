"""
十大排序算法
written by lxm
2020.2.18
"""


# 冒泡排序
# 稳定性：稳定
# 原理：最大或最小数往后或者往前冒，直至所有元素排序完毕
# 时间复杂度分析：O(n^2)，空间复杂度O(1)
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 选择排序
# 稳定性：稳定
# 每次在无序区中选择最小的元素，与无序区的第一个元素交换位置，则有序区扩展一；以此类推，直至所有元素排序完毕。
# 时间复杂度分析：O(n^2)，空间复杂度O(1)
def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        minIdx = i
        for j in range(i + 1, length):
            if arr[minIdx] > arr[j]:
                minIdx = j
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]


# 插入排序
# 稳定性:稳定
# 原理：对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 时间复杂度分析：O(n^2)，空间复杂度O(1)
def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):
        preIdx = i - 1
        cur = arr[i]
        while preIdx >= 0 and arr[preIdx] > cur:
            arr[preIdx + 1] = arr[preIdx]
            preIdx -= 1
        arr[preIdx + 1] = cur
    return arr


# 希尔排序
# 稳定性：不稳定
# 原理：希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 时间复杂度：最坏O(n^2) 最好 O(n) 空间复杂度：O(1)
def shell_sort(arr):
    length = len(arr)
    n = len(arr)
    gap = n >> 1  # gap是长度的一半
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                j -= gap
        gap = gap >> 1


# 快速排序
# 稳定性：不稳定
# 原理：选“基准”，小在左，大在右，分区操作，递归完成排序
# 时间复杂度：nlog n  空间复杂度：递归需要栈辅助 nlog n
def quick_sort(arr, low, high):
    def partition(arr, low, high):
        i, j = low, high
        pivot = arr[low]
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            while i < j and arr[i] <= pivot:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] > pivot:
            i -= 1
        arr[low], arr[i] = arr[i], arr[low]
        return i

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# 归并排序
# 稳定性：稳定
# 原理：分治法，将已有序的子序列合并，得到完全有序的序列
# 时间复杂度：nlog n 空间复杂度：O（n）
def merge_sort(arr):
    def merge(left, right):
        l, r = 0, 0
        res = []
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                res.append(right[r])
                r += 1
            else:
                res.append(left[l])
                l += 1
        res.extend(left[l:])
        res.extend(right[r:])
        return res

    length = len(arr)
    if len(arr) <= 1:
        return arr
    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# 堆排序
# 稳定性：稳定
# 原理：通过堆的特性，父节点始终比子节点大，进行排序
# 时间复杂度：nlog n 空间复杂度 O(1)
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 换下来的节点，仍要递归进行heapify
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # 构建最大堆，从最后开始构建，其实从最后非叶子节点开始构建即可
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)
    # 一个个交换元素到最后，最后的元素不参与堆构建（已保证是最大）
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # 所以只要前i个元素，对第0节点进行堆化
        heapify(arr, i, 0)


# 计数排序
# 稳定性：稳定
# 原理：计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
# 时间复杂度： O（n + k）  空间复杂度： O(n + k)
def count_sort(arr, Max):
    bucket = [0] * (Max + 1)
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    idx = 0
    for i in range(Max + 1):
        while bucket[i] > 0:
            arr[idx] = i
            idx += 1
            bucket[i] -= 1


# 桶排序
# 稳定性：稳定
# 原理：分桶后用其他排序处理
# 时间复杂度：平均O（n + k) 最坏O（n^2）空间复杂度 O（n + k)
def bucketSort(arr, bucketSize):
    if not arr: return arr
    minVal = min(arr)
    maxVal = max(arr)
    bucketsCount = (maxVal - minVal) // bucketSize + 1
    buckets = [[]] * bucketsCount
    for i in range(len(arr)):
        ind = (arr[i] - minVal) // bucketSize
        buckets[ind] = buckets[ind] + [arr[i]]
    arr = []
    for i in range(len(buckets)):
        buckets[i] = insert_sort(buckets[i])
        for j in range(len(buckets[i])):
            arr.append(buckets[i][j])
    return arr


# 基数排序


if __name__ == '__main__':
    array = [3, 4, 5, 1, 7, 3, 8, 1, 100]
    # bubble_sort(array)
    # selection_sort(array)
    # insert_sort(array)
    # shell_sort(array)
    # quick_sort(array, 0, len(array)-1)
    # print(merge_sort(array))
    # heap_sort(array)
    # count_sort(array, 100)
    #print(bucketSort(array, 3))

    # print(array)
