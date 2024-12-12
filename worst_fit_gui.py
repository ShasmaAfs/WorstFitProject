import tkinter as tk
from tkinter import messagebox


# Memory Block and Process Classes
class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.allocated = False


class Process:
    def __init__(self, pid, size):
        self.pid = pid
        self.size = size
        self.allocated_block = None


# Worst Fit Algorithm
def worst_fit(memory_blocks, processes):
    for process in processes:
        largest_block = None
        for block in memory_blocks:
            if not block.allocated and block.size >= process.size:
                if largest_block is None or block.size > largest_block.size:
                    largest_block = block

        if largest_block:
            largest_block.allocated = True
            process.allocated_block = largest_block
        else:
            process.allocated_block = None


# GUI Functionality
def run_allocation():
    try:
        # Read input for memory blocks and processes
        blocks = [int(size.strip()) for size in memory_blocks_entry.get().split(',')]
        processes = [int(size.strip()) for size in processes_entry.get().split(',')]

        # Create memory block and process objects
        memory_blocks = [MemoryBlock(size) for size in blocks]
        process_objects = [Process(i + 1, size) for i, size in enumerate(processes)]

        # Run the Worst Fit Algorithm
        worst_fit(memory_blocks, process_objects)

        # Display results
        results = []
        for process in process_objects:
            if process.allocated_block:
                results.append(f"Process {process.pid} (Size: {process.size}) allocated to block of size {process.allocated_block.size}.")
            else:
                results.append(f"Process {process.pid} (Size: {process.size}) could not be allocated.")
        
        # Show results in the GUI
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "\n".join(results))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by commas.")


# GUI Application
root = tk.Tk()
root.title("Worst Fit Memory Allocation")
root.geometry("600x450")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Worst Fit Memory Allocation", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Registration Number and Author Label
author_label = tk.Label(
    root, text="Reg.No: 121427169 © ALF.Siysath Shasma", font=("Arial", 10, "italic"), fg="grey"
)
author_label.pack(pady=5)

# Memory Blocks Input
memory_blocks_label = tk.Label(root, text="Enter Memory Blocks (comma-separated):", font=("Arial", 12))
memory_blocks_label.pack(pady=5)
memory_blocks_entry = tk.Entry(root, width=50, font=("Arial", 12))
memory_blocks_entry.pack(pady=5)

# Processes Input
processes_label = tk.Label(root, text="Enter Process Sizes (comma-separated):", font=("Arial", 12))
processes_label.pack(pady=5)
processes_entry = tk.Entry(root, width=50, font=("Arial", 12))
processes_entry.pack(pady=5)

# Run Button
run_button = tk.Button(root, text="Run Allocation", font=("Arial", 12, "bold"), bg="green", fg="white", command=run_allocation)
run_button.pack(pady=10)

# Results Label
results_label = tk.Label(root, text="Allocation Results:", font=("Arial", 12))
results_label.pack(pady=5)

# Results Textbox
result_text = tk.Text(root, height=10, width=70, font=("Arial", 10))
result_text.pack(pady=10)

# Footer with Registration and Copyright
footer_label = tk.Label(
    root, text="© 2024 ALF.Siysath Shasma. All Rights Reserved.", font=("Arial", 10, "italic"), fg="grey"
)
footer_label.pack(side=tk.BOTTOM, pady=5)

# Run the main application loop
root.mainloop()
