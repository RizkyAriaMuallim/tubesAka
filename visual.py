from tkinter import *
from tkinter import ttk
from selectionSort import selectionSort
from QuickSort import quick_sort
import numpy as np
import timeit
np.random.seed(42) ## pseudo random agar 

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()

def Generate():
    global data

    minVal = minEntry.get()
    maxVal = maxEntry.get()
    size = sizeEntry.get()

    data = np.random.randint(low = minVal, high = maxVal, size = size)
    # for _ in range(size):
    #     data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])
def startAlgorithm():
    global data
    
    start = timeit.default_timer()
    if algMenu.get() == "Selection Sort":
        selectionSort(data, drawData)
    elif algMenu.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, drawData)
        drawData(data, ['green' for x in range(len(data))])
    end = timeit.default_timer()

    print(f"Running time of {algMenu.get()}: {end - start}")


#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=100, pady=5)

#User Interface Area
##Row[0]##
# drop down menu buat milih algoritma
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Selection Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
# buat tombol generate --> kalo dipencet entar dia ngegenerate data
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text="Sort", command = startAlgorithm,bg="blue", fg = "white").grid(row = 0, column = 3, padx=5, pady=5)

#Row[1]
Label(UI_frame, text="Size ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Scale(UI_frame, from_=3, to = 25, resolution=1, orient="horizontal", label="Size")
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Scale(UI_frame, from_= 0, to = 10, resolution=10, orient="horizontal", label="Min value")
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Scale(UI_frame, from_=10, to = 60, resolution=1, orient= "horizontal",label="Max Value")
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

root.mainloop()