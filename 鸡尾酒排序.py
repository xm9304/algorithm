def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """
      高质量冒泡排序(搅拌排序、鸡尾酒排序)
      原理：第一轮：保证每轮两端必定最大最小，两边紧逼到中间
     """
    items = origin_items[:]

    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                print(items)
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    print(items)
                    swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    item = [54, 12, 98, 1, 56]
    print(item)
    print(bubble_sort(item))
