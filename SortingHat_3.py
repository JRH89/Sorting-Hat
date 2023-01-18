import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import re
import collections

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val/exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i]/exp1)
        count[int(index%10)] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[count[int(index%10)]-1] = arr[i]
        count[int(index%10)] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

def sort_numbers():
    try:
        input_string = input_field.get()
        numbers = list(map(int, re.findall(r'\d+', input_string)))
        bin_size = int(bin_size_input.get()) if bin_size_input.get() != "" else 10
        sorted_numbers = radix_sort(numbers)
        output_field.delete("1.0", tk.END)
        output_field.insert(tk.END, str(sorted_numbers))
        if graph_var.get() == "Line":
            plt.plot(sorted_numbers)
        elif graph_var.get() == "Bar":
            counts = collections.Counter(sorted_numbers)
            keys = list(counts.keys())
            values = list(counts.values())
            plt.bar(keys, values)
            plt.xlabel('Data Value')
            plt.ylabel('# of Occurrences')
        elif graph_var.get() == "Scatter":
            plt.scatter(range(len(sorted_numbers)), sorted_numbers)
            plt.xlabel("Sorted Array Index Position")
            plt.ylabel("Value")
            plt.xticks(range(len(sorted_numbers)), range(len(sorted_numbers)))


        elif graph_var.get() == "Histogram":
            plt.hist(sorted_numbers, bins=bin_size, range=(min(sorted_numbers), max(sorted_numbers)), color='orange', edgecolor='blue')
            plt.xlabel('Values')
            plt.ylabel('Frequency')
        elif graph_var.get() == "Pie":
            counts = collections.Counter(sorted_numbers)
            labels = [str(x) for x in counts.keys()]
            sizes = counts.values()
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')
            plt.legend(title="Data Value")
            
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear_input():
    input_field.delete(0, tk.END)
    output_field.delete("1.0", tk.END)
    graph_var.set("Line")
    bin_size_input.delete(0, tk.END)

root = tk.Tk()
root.title("Sorting Hat 3.0")

input_label = tk.Label(root, text="Enter data to be extracted and sorted:")
input_label.pack(pady=15)

input_field = tk.Entry(root)
input_field.pack()
input_field.configure(width=70)



output_label = tk.Label(root, text="Sorted numbers:")
output_label.pack(pady=10)

output_field = tk.Text(root, height=20, width=50)
output_field.pack()

graph_var = tk.StringVar(value="Choose Graph Type")
graph_dropdown = tk.OptionMenu(root, graph_var, "Line", "Bar", "Scatter", "Histogram", "Pie")
graph_dropdown.pack(pady=10)

bin_size_label = tk.Label(root, text="# of Bins for Histogram:")
bin_size_label.pack()

bin_size_input = tk.Entry(root)
bin_size_input.pack(pady=10)

sort_button = tk.Button(root, text="Sort and Graph", command=sort_numbers)
sort_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=10)

root.geometry("500x630")
root.mainloop()


