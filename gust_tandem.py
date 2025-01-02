from s_tree import SuffixTree

def find_tandem_repeats(tree):
    """
    Identifies all tandem repeats and classifies them into branching and non-branching.
    """
    btr_results = []
    nbtr_results = []

    def process_node(node):
        """Process a single node to detect tandem repeats."""
        if not node.children:
            return  # Skip leaves

        min_dfs, max_dfs, string_depth = node.min_dfs, node.max_dfs, node.string_depth

        if string_depth == 0:
            return

        for dfs_i in range(min_dfs, max_dfs + 1):
            suffix_i = tree.get_suffix_from_dfs(dfs_i)
            if suffix_i is None:
                continue

            suffix_j = suffix_i + string_depth
            dfs_j = tree.get_dfs_from_suffix(suffix_j)

            if not (min_dfs <= dfs_j <= max_dfs):
                continue

            # Check if it's branching or non-branching
            if tree.text[suffix_i + string_depth] != tree.text[suffix_i + 2 * string_depth]:
                btr_results.append((suffix_i, string_depth))  # Branching Tandem Repeat (BTR)
            else:
                nbtr_results.append((suffix_i, string_depth))  # Non-Branching Tandem Repeat (NBTR)

    def dfs_process(node):
        """Perform a DFS traversal to process all nodes."""
        for child in node.children.values():
            dfs_process(child)
        process_node(node)

    dfs_process(tree.root)

    def expand_left_rotations():
        """Expand NBTRs by checking left rotations of each tandem repeat."""
        expanded_nbtr_results = set(nbtr_results)

        for (i, l) in btr_results:
            while i > 0 and tree.text[i - 1] == tree.text[i + l - 1]:
                i -= 1
                expanded_nbtr_results.add((i, l))

        return list(expanded_nbtr_results)

    expanded_nbtr_results = expand_left_rotations()  # Add left rotations for NBTRs
    return btr_results, expanded_nbtr_results


if __name__ == "__main__":
    text = "ABAABAABBBA"
    tree = SuffixTree(text)  # Construct the suffix tree

    # Find tandem repeats and classify them
    btr_results, nbtr_results = find_tandem_repeats(tree)

    # Print all the detected BTRs and NBTRs
    print(f"\nBranching Tandem Repeats (BTRs) detected: {btr_results}")
    print(f"\nNon-Branching Tandem Repeats (NBTRs) with Left Rotations: {nbtr_results}")
