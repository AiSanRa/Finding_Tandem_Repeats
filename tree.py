class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.leaf_index = None
        self.min_dfs = None
        self.max_dfs = None
        self.dfs_number = None
        self.string_depth = 0  


class SuffixTree:
    def __init__(self, text):
        self.text = text + "$"
        self.root = SuffixTreeNode()
        self.dfs_counter = 0
        self.suffix_to_dfs = {}
        self.dfs_to_suffix = {}
        self.build_suffix_tree()
        self.prune_tree()
        self.assign_dfs_numbers()

    def build_suffix_tree(self):
        """Construct the suffix tree."""
        for i in range(len(self.text)):
            current_node = self.root
            depth = 0
            for char in self.text[i:]:
                if char not in current_node.children:
                    current_node.children[char] = SuffixTreeNode()
                current_node = current_node.children[char]
                depth += 1
                current_node.string_depth = depth  # Update string depth
            current_node.leaf_index = i

    def prune_tree(self):
        """Merge redundant nodes."""
        def prune(node):
            # Recursively prune the children
            for child in list(node.children.values()):
                prune(child)

            # Merge the node if it has exactly one child and no leaf_index
            if len(node.children) == 1 and node.leaf_index is None:
                # Get the only child
                child = next(iter(node.children.values()))
                # Merge the child into the current node
                node.children = child.children
                node.leaf_index = child.leaf_index
                node.string_depth = child.string_depth
                node.min_dfs = child.min_dfs
                node.max_dfs = child.max_dfs
        # Start pruning from the root node
        prune(self.root)


    def assign_dfs_numbers(self):
        """Assign DFS numbers to leaves and compute min/max DFS for internal nodes."""
        def dfs(node):
            if node.leaf_index is not None:
                self.dfs_counter += 1
                node.min_dfs = node.max_dfs = self.dfs_counter
                node.dfs_number = self.dfs_counter
                self.suffix_to_dfs[node.leaf_index] = node.dfs_number
                self.dfs_to_suffix[node.dfs_number] = node.leaf_index
            else:
                min_dfs, max_dfs = float('inf'), float('-inf')
                for child in node.children.values():
                    dfs(child)
                    min_dfs = min(min_dfs, child.min_dfs)
                    max_dfs = max(max_dfs, child.max_dfs)
                node.min_dfs, node.max_dfs = min_dfs, max_dfs

        dfs(self.root)

    def get_dfs_from_suffix(self, suffix_number):
        """Return the DFS number corresponding to the given suffix number."""
        return self.suffix_to_dfs.get(suffix_number, None)

    def get_suffix_from_dfs(self, dfs_number):
        """Return the suffix number corresponding to the given DFS number."""
        return self.dfs_to_suffix.get(dfs_number, None)
