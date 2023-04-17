import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animation(arr):
    fig, ax = plt.subplots()
    ax.set_title('Bogo Sort Visualization')

    bar_rects = ax.bar(range(len(arr)), arr, align='edge')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr))

    def update_fig(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)

    def bogo_sort(arr):
        while not is_sorted(arr):
            random.shuffle(arr)
            yield arr

    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
        return True

    func = FuncAnimation(fig, func=update_fig, fargs=(bar_rects,),
                         frames=bogo_sort(arr), repeat=False)
    plt.show()

my_array = [3, 5, 2, 8, 1, 4]
animation(my_array)
