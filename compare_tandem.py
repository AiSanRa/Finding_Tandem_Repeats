import random
from naive_tandem import find_tandem_repeats as find_tandem_repeats_basic
from gust_tandem import find_tandem_repeats as find_tandem_repeats_gust
from opti_gust_tadem import find_tandem_repeats as find_tandem_repeats_opti
from s_tree import SuffixTree as GustTree
from s_tree import SuffixTree as OptiTree

# Generate a random string using only ACTG with a length between 50 and 1000
def generate_random_string():
    length = random.randint(50, 1000)
    return ''.join(random.choices('ACTG', k=length))

# Comparison function
# Comparison function
def compare_tandem_repeats(input_string):
    print(f"Input String Length: {len(input_string)}")

    # Method 1: Basic String Method
    repeats_basic = find_tandem_repeats_basic(input_string)

    # Method 2: Gusfield Method
    gust_tree = GustTree(input_string)
    btr_results_gust, nbtr_results_gust = find_tandem_repeats_gust(gust_tree)

    # Method 3: Optimized Gusfield Method
    opti_tree = OptiTree(input_string)
    btr_results_opti, nbtr_results_opti = find_tandem_repeats_opti(opti_tree)

    # Print the results for each method
    print(f"Basic method results: {repeats_basic}")
    print(f"Gusfield method results (BTRs, NBTRs): {btr_results_gust}, {nbtr_results_gust}")
    print(f"Optimized Gusfield method results (BTRs, NBTRs): {btr_results_opti}, {nbtr_results_opti}")

    # Combine BTRs and NBTRs for Gusfield and Optimized Gusfield methods
    combined_gust_results = btr_results_gust + nbtr_results_gust
    combined_opti_results = btr_results_opti + nbtr_results_opti

    # Sort the results to ensure the order does not affect comparison
    repeats_basic_sorted = sorted(repeats_basic)
    combined_gust_results_sorted = sorted(combined_gust_results)
    combined_opti_results_sorted = sorted(combined_opti_results)

    # Check if all results are the same after sorting
    if (
        repeats_basic_sorted == combined_gust_results_sorted
        and combined_gust_results_sorted == combined_opti_results_sorted
    ):
        print("All methods returned the same results.")
    else:
        print("Methods returned different results.")
    print("-" * 40)


# Test with 50 random strings
for _ in range(50):
    random_string = generate_random_string()  # Generate a random string with a random length
    compare_tandem_repeats(random_string)
