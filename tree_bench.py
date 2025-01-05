import time
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys
sys.setrecursionlimit(10000)

from s_tree import SuffixTreeNode
from s_tree import SuffixTree

def generate_random_string(length):
    """Generate a random string of the given length containing the characters A, C, T, G, and a terminating '$'"""
    return ''.join(random.choices('ACTG', k=length)) + '$'

def benchmark_suffix_tree_construction():
    input_sizes = []
    construction_times = []
    
    # Define a range of input sizes to test
    for size in range(10, 10000, 50):  # From 10 to 10000 characters with step of 50
        random_string = generate_random_string(size)
        
        # Start the timer
        start_time = time.time()
        
        # Create the suffix tree
        tree = SuffixTree(random_string)
        
        # End the timer
        end_time = time.time()
        
        # Calculate the time taken to construct the tree
        elapsed_time = end_time - start_time
        
        # Record the result
        input_sizes.append(size)
        construction_times.append(elapsed_time)
        print(f"Input size: {size}, Construction time: {elapsed_time:.6f} seconds")

    # Apply Seaborn theme for a polished look
    sns.set_theme(style="whitegrid")
    
    # Create the plot
    plt.figure(figsize=(10, 6))  # Set figure size
    plt.plot(input_sizes, construction_times, marker='o', color='royalblue', label="Construction Time", linewidth=2, markersize=5)
    
    # Add labels and title
    plt.xlabel('Input Size (Length of String)', fontsize=12, labelpad=10)
    plt.ylabel('Construction Time (Seconds)', fontsize=12, labelpad=10)
    plt.title('Suffix Tree Construction Time Benchmark', fontsize=14, pad=15)
    
    # Enhance the legend
    plt.legend(fontsize=12, loc="upper left", frameon=True, shadow=True, borderpad=1)
    
    # Tweak grid and axis
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()  # Adjust layout for better spacing
    
    # Save the plot as an image
    plt.savefig("bench_tree.png", dpi=300)  # Save with high resolution
    plt.show()

if __name__ == "__main__":
    benchmark_suffix_tree_construction()
