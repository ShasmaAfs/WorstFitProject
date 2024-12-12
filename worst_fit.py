# worst_fit.py

# Step 1: Define the memory block structure
class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.allocated = False  # Initially, blocks are not allocated

# Step 2: Define the process structure
class Process:
    def __init__(self, pid, size):
        self.pid = pid  # Process ID
        self.size = size  # Memory required by the process
        self.allocated_block = None  # Initially, no block is allocated

# Step 3: Simulate the Worst Fit Algorithm
def worst_fit(memory_blocks, processes):
    print("Simulating Worst Fit Memory Allocation...")
    for process in processes:
        largest_block = None  # Find the largest block that fits
        for block in memory_blocks:
            if not block.allocated and block.size >= process.size:
                if largest_block is None or block.size > largest_block.size:
                    largest_block = block

        # Allocate the process to the largest block if found
        if largest_block:
            largest_block.allocated = True
            process.allocated_block = largest_block
            print(f"Process {process.pid} (Size: {process.size}) allocated to block of size {largest_block.size}.")
        else:
            print(f"Process {process.pid} (Size: {process.size}) could not be allocated.")

# Step 4: Display final allocation
def display_allocation(processes):
    print("\nFinal Allocation Results:")
    for process in processes:
        if process.allocated_block:
            print(f"Process {process.pid} allocated to block of size {process.allocated_block.size}.")
        else:
            print(f"Process {process.pid} could not be allocated.")

# Step 5: Main Function to Run the Program
if __name__ == "__main__":
    # Define memory blocks
    memory_blocks = [MemoryBlock(100), MemoryBlock(500), MemoryBlock(200), MemoryBlock(300), MemoryBlock(600)]

    # Define processes
    processes = [Process(1, 212), Process(2, 417), Process(3, 112), Process(4, 426)]

    # Run the Worst Fit Algorithm
    worst_fit(memory_blocks, processes)

    # Display the final allocation
    display_allocation(processes)
