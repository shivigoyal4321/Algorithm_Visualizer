import tkinter as tk
import random
import time

# Animation speed, the lower the value, the faster the animation
SPEED_OF_ANIMATION = 0.1

# Create a Tkinter window for the user interface
app_window = tk.Tk()
app_window.title("Sorting Algorithm Visualizer - Created by Shivi Goyal")
app_window.config(bg="lavender")  # Updated background color to lavender

# Set dimensions for the canvas
canvas_width = 800
canvas_height = 400
canvas_area = tk.Canvas(app_window, width=canvas_width, height=canvas_height, bg="lavender")  # Canvas background set to lavender
canvas_area.pack()

# Generate a list of random values to be sorted
def generate_random_values():
    return [random.randint(10, canvas_height) for _ in range(50)]

# Function to draw the bars representing the array
def render_array(arr, highlight_indices=[]):
    canvas_area.delete("all")  # Clear the canvas before redrawing
    bar_width = canvas_width // len(arr)
    
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - value
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        
        # Color bars based on their status:
        # Green if sorted, Red if in wrong order, Blue while sorting
        if i in highlight_indices:
            color = "red"  # Elements being compared or swapped
        else:
            color = "blue"  # Default color while doing the sorting steps
        
        # Once fully sorted, turn the bars green
        if arr == sorted(arr):  # The array is fully sorted
            color = "green"

        canvas_area.create_rectangle(x0, y0, x1, y1, fill=color)
    
    app_window.update()
    time.sleep(SPEED_OF_ANIMATION)

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            render_array(arr, highlight_indices=[j, j+1])  # Highlighting the pair being compared
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                render_array(arr)  # Show the swap action
    render_array(arr)  # Final rendering after sorting

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            render_array(arr)  # Show the array with the shifting action
        arr[j + 1] = key
        render_array(arr)  # Show the array after inserting the key
    render_array(arr)

# Selection Sort Implementation
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        render_array(arr)  # Show the array after each swap
    render_array(arr)

# Merge Sort Implementation
def merge_sort(arr):
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left)
        merged.extend(right)
        return merged

    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return merge(left, right)

    sorted_array = divide(arr)
    render_array(sorted_array)

# Quick Sort Implementation
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                render_array(arr)  # Show the array with the swapped elements
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        render_array(arr)
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    render_array(arr)

# Algorithm map to their corresponding complexities
algorithm_data = {
    "Bubble Sort": {
        "function": bubble_sort,
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)"
    },
    "Insertion Sort": {
        "function": insertion_sort,
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)"
    },
    "Selection Sort": {
        "function": selection_sort,
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)"
    },
    "Merge Sort": {
        "function": merge_sort,
        "time_complexity": "O(n log n)",
        "space_complexity": "O(n)"
    },
    "Quick Sort": {
        "function": quick_sort,
        "time_complexity": "O(n log n) (avg), O(n²) (worst)",
        "space_complexity": "O(log n)"
    }
}

# Function to handle the sorting visualization
def start_sorting_process():
    selected_algo = algorithm_selection.get()
    random_array = generate_random_values()
    render_array(random_array)  # Initial array rendering
    algorithm_data[selected_algo]["function"](random_array)  # Execute the selected algorithm
    
    # Update complexity labels
    time_label.config(text=f"Time Complexity: {algorithm_data[selected_algo]['time_complexity']}")
    space_label.config(text=f"Space Complexity: {algorithm_data[selected_algo]['space_complexity']}")

# Dropdown menu to select the sorting algorithm
algorithm_selection = tk.StringVar(app_window)
algorithm_selection.set("Bubble Sort")  # Default selection

algo_menu = tk.OptionMenu(app_window, algorithm_selection, *algorithm_data.keys())
algo_menu.config(font=("Arial", 14))
algo_menu.pack(pady=20)

# Button to start the sorting visualization
sort_button = tk.Button(app_window, text="Start Sorting", command=start_sorting_process, font=("Arial", 16))
sort_button.pack(pady=20)

# To display the time and space complexities
time_label = tk.Label(app_window, text="Time Complexity: ", font=("Arial", 14))
time_label.pack(pady=10)

space_label = tk.Label(app_window, text="Space Complexity: ", font=("Arial", 14))
space_label.pack(pady=10)

# Footer Label with name
footer_label = tk.Label(app_window, text="Created by Shivi Goyal", font=("Arial", 10, "italic"), fg="gray")
footer_label.pack(side="bottom", pady=20)

# Run the Tkinter event loop
app_window.mainloop()
