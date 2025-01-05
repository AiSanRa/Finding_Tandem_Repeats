import time
import matplotlib.pyplot as plt
import seaborn as sns
from s_tree import SuffixTree  
from gust_tandem import find_tandem_repeats 
import random
import sys

sys.setrecursionlimit(10000)

def generate_random_string(length):
    """Generate a random string of the given length containing the characters A, C, T, G."""
    return ''.join(random.choices('ACTG', k=length))

def generate_string_all_a(length):
    """Generate a string of 'A's of the given length."""
    return 'A' * length

def benchmark_tandem_repeat_detection(use_all_a=False):
    input_sizes = []
    detection_times = []
    
    # Define a range of input sizes to test
    for size in range(10, 10000, 50):  # From 10 to 10000 characters with step of 50
        if use_all_a:
            # Generate string of 'A's
            input_string = generate_string_all_a(size)
        else:
            # Generate random string
            input_string = generate_random_string(size)
        
        # Create the suffix tree
        tree = SuffixTree(input_string)
        
        # Start the timer
        start_time = time.time()
        
        # Detect tandem repeats
        _, _ = find_tandem_repeats(tree)
        
        # End the timer
        end_time = time.time()
        
        # Calculate the time taken to detect repeats
        elapsed_time = end_time - start_time
        
        # Record the result
        input_sizes.append(size)
        detection_times.append(elapsed_time)
        print(f"Input size: {size}, Detection time: {elapsed_time:.6f} seconds")

    # Apply Seaborn theme for a polished look
    sns.set_theme(style="whitegrid")
    
    # Create the plot
    plt.figure(figsize=(10, 6))  # Set figure size
    plt.plot(input_sizes, detection_times, marker='o', color='teal', label="Detection Time", linewidth=2, markersize=5)
    
    # Add labels and title
    plot_title = 'Gusfield-Stoye Tandem Repeat Time Benchmark'
    if use_all_a:
        plot_title += ' (All "A"s)'
    plt.xlabel('Input Size (Length of String)', fontsize=12, labelpad=10)
    plt.ylabel('Detection Time (Seconds)', fontsize=12, labelpad=10)
    plt.title(plot_title, fontsize=14, pad=15)
    
    # Enhance the legend
    plt.legend(fontsize=12, loc="upper left", frameon=True, shadow=True, borderpad=1)
    
    # Tweak grid and axis
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()  # Adjust layout for better spacing
    
    # Save the plot as an image
    output_filename = "tandem_gust_benchmark.png" if not use_all_a else "a_tandem_gust_benchmark.png"
    plt.savefig(output_filename, dpi=300)  # Save with high resolution
    plt.show()

if __name__ == "__main__":
    # Run the benchmark for random strings (use_all_a=False)
    benchmark_tandem_repeat_detection(use_all_a=False)
    
    # Run the benchmark for strings of all 'A's (use_all_a=True)
    benchmark_tandem_repeat_detection(use_all_a=True)
