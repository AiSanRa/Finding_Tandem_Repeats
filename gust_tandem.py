from tree import SuffixTree

def find_tandem_repeats(tree):
    """
    Identifies all tandem repeats and classifies them into branching and non-branching.
    """
  
    btr_results = []
    nbtr_results = []

    def process_node(node):
        if not node.children:
            return  # Skip leaves

        min_dfs = node.min_dfs
        max_dfs = node.max_dfs
        string_depth = node.string_depth

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

            # Ensure the two suffixes are valid and compare substrings
            # Check branching condition: S[i(suf)] != S[i(suf) + 2 * alpha(v)]
            if tree.text[suffix_i + string_depth] != tree.text[suffix_i + 2 * string_depth]:
                # It's a Branching Tandem Repeat (BTR)
                btr_results.append((suffix_i, string_depth))
            else:
                # It's a Non-Branching Tandem Repeat (NBTR)
                nbtr_results.append((suffix_i, string_depth))

    # Perform DFS to process all nodes in the tree
    def dfs_process(node):
        for child in node.children.values():
            dfs_process(child)
        process_node(node)

    dfs_process(tree.root)

    # Expand left rotations at the end
    def expand_left_rotations():
        """Expand NBTRs by checking left rotations of each tandem repeat."""
        expanded_nbtr_results = set(nbtr_results)

        for (i, l) in btr_results:
            # Check if a left-rotation can expand the repeat
            while i > 0:
                # Check if the previous character is the same as the last character
                if tree.text[i - 1] == tree.text[i + l - 1]:
                    # Expand the NBTR to the left
                    i -= 1
                    expanded_nbtr_results.add((i, l))
                else:
                    break

        return list(expanded_nbtr_results)

    expanded_nbtr_results = expand_left_rotations()  # Add left rotations for NBTRs
    return btr_results, expanded_nbtr_results


# Enhancing the SuffixTree class to include depth assignment
class EnhancedSuffixTree(SuffixTree):
    def assign_depths(self):
        """Assign depths to all nodes in the suffix tree."""
        def dfs(node, depth):
            node.depth = depth

            # Recursively assign depths to all children
            for child in node.children.values():
                dfs(child, depth + 1)
        
        dfs(self.root, 0)


if __name__ == "__main__":
    text = "ABAABAABBBA"
    tree = EnhancedSuffixTree(text)  # Construct the enhanced suffix tree
    tree.assign_depths()  # Assign depths to all nodes

    # Find tandem repeats and classify them
    btr_results, nbtr_results = find_tandem_repeats(tree)

    # Print all the detected BTRs and NBTRs
    print(f"\nBranching Tandem Repeats (BTRs) detected: {btr_results}")
    print(f"\nNon-Branching Tandem Repeats (NBTRs) with Left Rotations: {nbtr_results}")
