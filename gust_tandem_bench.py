import time
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys
from s_tree import SuffixTree  # Assuming SuffixTree is correctly implemented and available
from opti_gust_tandem import find_tandem_repeats as find_tandem_repeats_opti  # Import the tandem repeat detection function from opti_gust_tandem
from gust_tandem import find_tandem_repeats as find_tandem_repeats_gust  # Import the tandem repeat detection function from gust_tandem

# Set recursion limit
sys.setrecursionlimit(15000)

# Generate string of all 'A's
def generate_string_all_a(length):
    """Generate a string of 'A's of the given length"""
    return 'A' * length 

# Generate random string containing A, C, T, G
def generate_random_string(length):
    """Generate a random string of the given length containing the characters A, C, T, G"""
    return ''.join(random.choices('ACTG', k=length))

# Benchmark function for tandem repeat detection
def benchmark_tandem_repeat_detection():
    input_sizes = []
    detection_times_all_a_opti = []
    detection_times_random_opti = []
    detection_times_all_a_gust = []
    detection_times_random_gust = []
    
    # Define a range of input sizes to test
    for size in range(10, 10000, 100):  # From 10 to 15000 characters with step of 50
        # Generate strings
        string_all_a = generate_string_all_a(size)
        random_string = generate_random_string(size)
        
        # Create the suffix trees for both strings
        tree_all_a = SuffixTree(string_all_a)
        tree_random = SuffixTree(random_string)
        
        # Start the timer for the 'A' string with opti_gust_tandem
        start_time = time.time()
        _, _ = find_tandem_repeats_opti(tree_all_a)  # Detect tandem repeats with opti_gust_tandem
        end_time = time.time()
        elapsed_time_all_a_opti = end_time - start_time
        
        # Start the timer for the random string with opti_gust_tandem
        start_time = time.time()
        _, _ = find_tandem_repeats_opti(tree_random)  # Detect tandem repeats with opti_gust_tandem
        end_time = time.time()
        elapsed_time_random_opti = end_time - start_time
        
        # Start the timer for the 'A' string with gust_tandem
        start_time = time.time()
        _, _ = find_tandem_repeats_gust(tree_all_a)  # Detect tandem repeats with gust_tandem
        end_time = time.time()
        elapsed_time_all_a_gust = end_time - start_time
        
        # Start the timer for the random string with gust_tandem
        start_time = time.time()
        _, _ = find_tandem_repeats_gust(tree_random)  # Detect tandem repeats with gust_tandem
        end_time = time.time()
        elapsed_time_random_gust = end_time - start_time
        
        # Record the results
        input_sizes.append(size)
        detection_times_all_a_opti.append(elapsed_time_all_a_opti)
        detection_times_random_opti.append(elapsed_time_random_opti)
        detection_times_all_a_gust.append(elapsed_time_all_a_gust)
        detection_times_random_gust.append(elapsed_time_random_gust)
        
        # Print the results for each input size
        print(f"Input size: {size}, All 'A' Opti Detection time: {elapsed_time_all_a_opti:.6f} seconds, Random Opti Detection time: {elapsed_time_random_opti:.6f} seconds")
        print(f"Input size: {size}, All 'A' Gust Detection time: {elapsed_time_all_a_gust:.6f} seconds, Random Gust Detection time: {elapsed_time_random_gust:.6f} seconds")

    # Apply Seaborn theme for a polished look
    sns.set_theme(style="whitegrid")
    
    # Create the plot
    plt.figure(figsize=(12, 8))  # Set figure size
    plt.plot(input_sizes, detection_times_all_a_opti, marker='o', color='forestgreen', label="All 'A' Opti Detection Time", linewidth=2, markersize=5)
    plt.plot(input_sizes, detection_times_random_opti, marker='o', color='dodgerblue', label="Random Opti Detection Time", linewidth=2, markersize=5)
    plt.plot(input_sizes, detection_times_all_a_gust, marker='o', color='darkorange', label="All 'A' Gust Detection Time", linewidth=2, markersize=5) 
    plt.plot(input_sizes, detection_times_random_gust, marker='o', color='crimson', label="Random Gust Detection Time", linewidth=2, markersize=5) 
    
    # Add labels and title
    plt.xlabel('Input Size (Length of String)', fontsize=12, labelpad=10)
    plt.ylabel('Detection Time (Seconds)', fontsize=12, labelpad=10)
    plt.title('Tandem Repeat Detection Time Benchmark (Opti vs Gust)', fontsize=14, pad=15)
    
    # Enhance the legend
    plt.legend(fontsize=12, loc="upper left", frameon=True, shadow=True, borderpad=1)
    
    # Tweak grid and axis
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()  # Adjust layout for better spacing
    
    # Save the plot as an image
    plt.savefig("opti_vs_gust_tandem_benchmark_combined.png", dpi=300)  # Save with high resolution
    plt.show()

if __name__ == "__main__":
    # Run the benchmark
    benchmark_tandem_repeat_detection()
