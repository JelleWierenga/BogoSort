# Bogo Sort Visualization

This Python code demonstrates how to visualize the Bogo Sort algorithm using `matplotlib`. The program generates a random list of numbers, sorts it using Bogo Sort, and animates the sorting process.

## Requirements

- Python 3.x
- matplotlib

## Usage

To run the program, save the code in a file, and run it using Python:
`python Bogo_Sort.py`

The program generates a list of random numbers, sorts it using Bogo Sort, and displays an animation of the sorting process.

## Code Explanation

The `animation` function creates a `matplotlib` figure and initializes a bar chart with the input list of numbers. It then defines two inner functions: `update_fig` and `bogo_sort`. 

`update_fig` updates the heights of the bars in the chart to match the current state of the list during the sorting process.

`bogo_sort` is a generator function that yields the current state of the list during the sorting process. It uses the `random.shuffle` method to shuffle the list until it is sorted.

Finally, the `FuncAnimation` class is used to animate the chart, by repeatedly calling `update_fig` with the current state of the list. The `plt.show()` method is called to display the animation.

The `Sorting_Numbers` list is created with some example values and is passed to the `animation` function to visualize the Bogo Sort algorithm.

## Output

Running the program will display a window showing the animated sorting process of the `Sorting_Numbers` list using the Bogo Sort algorithm. The animation will stop once the list is sorted.
