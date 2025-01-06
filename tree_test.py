import unittest
from tree import SuffixTree 

class TestSuffixTree(unittest.TestCase):
    def setUp(self):
        """Initialize a SuffixTree for the string 'banana$'."""
        self.string = "banana$"
        self.tree = SuffixTree(self.string) 

    def test_number_of_leaves(self):
        """Verify that the number of leaves matches the length of the string."""
        def count_leaves(node):
            if not node.children:  # Node is a leaf
                return 1
            return sum(count_leaves(child) for child in node.children.values())

        num_leaves = count_leaves(self.tree.root)

        # The number of leaves in a suffix tree should match the number of suffixes, i.e., the string length.
        self.assertEqual(num_leaves, len(self.string))

    def test_dfs_order(self):
        """Check that DFS order covers all leaves with sequential DFS numbers."""
        def collect_dfs_numbers(node, dfs_numbers):
            """Recursive DFS collection for leaf nodes with their assigned DFS numbers."""
            if node.dfs_number is not None: 
                dfs_numbers.append(node.dfs_number)
            for child in node.children.values():
                collect_dfs_numbers(child, dfs_numbers)

        dfs_numbers = []
        collect_dfs_numbers(self.tree.root, dfs_numbers)

        # DFS numbers should be sequential integers starting from 1 to the number of leaves.
        expected_dfs_numbers = list(range(1, len(dfs_numbers) + 1))
        self.assertEqual(dfs_numbers, expected_dfs_numbers)

    def test_unique_edge_symbols(self):
        """Ensure that each internal node has unique edge symbols for its children."""
        def check_edge_symbols(node):
            edge_symbols = set(node.children.keys())
            self.assertEqual(len(edge_symbols), len(node.children), "Duplicate edge symbols found.")
            for child in node.children.values():
                check_edge_symbols(child)

        check_edge_symbols(self.tree.root)

    def test_min_max_dfs(self):
        """Check if min_dfs and max_dfs are correctly calculated for all nodes."""
        def validate_dfs_ranges(node):
            if node.leaf_index is not None:  # This is a leaf node
                # For leaves, min_dfs and max_dfs should both equal dfs_number
                self.assertEqual(node.min_dfs, node.dfs_number)
                self.assertEqual(node.max_dfs, node.dfs_number)
            else:  # This is an internal node
                min_dfs = float('inf')
                max_dfs = float('-inf')
                for child in node.children.values():
                    validate_dfs_ranges(child)  # Recursive validation for children
                    min_dfs = min(min_dfs, child.min_dfs)
                    max_dfs = max(max_dfs, child.max_dfs)
                # Check that the current node's min/max match its children's ranges
                self.assertEqual(node.min_dfs, min_dfs)
                self.assertEqual(node.max_dfs, max_dfs)

        # Start validation from the root
        validate_dfs_ranges(self.tree.root)

if __name__ == "__main__":
    unittest.main()
