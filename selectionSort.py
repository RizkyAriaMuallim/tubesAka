import time

def selectionSort(data, drawData):
    for i in range(len(data)):
        min_idx = i
        for j in range(min_idx+1, len(data)):
            drawData(data, ["green" if x<i else "blue" if x == min_idx else "purple" if x == j else "red" for x in range(len(data))])
            time.sleep(0.2)
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ["green" if x <= i else "red" for x in range(len(data))])
        time.sleep(0.2)