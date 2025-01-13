from s_tree import SuffixTree

def find_tandem_repeats(tree):
    """
    Optimized Stoye and Gusfield algorithm for finding branching tandem repeats (BTRs)
    and non-branching tandem repeats (NBTRs).
    """
    btr_results = set()  # To store Branching Tandem Repeats (BTRs)
    nbtr_results = set()  # To store Non-Branching Tandem Repeats (NBTRs)

    marked_nodes = set()

    def process_node(v):
        """Process a node v and execute steps 2a, 2b, and 2c."""
        if v in marked_nodes:
            return  # Skip already marked nodes

        marked_nodes.add(v)

        # Step 2a: Identify Large(v) and Small(v)
        large_v = None
        small_v = []

        children_sorted = sorted(v.children.values(), key=lambda child: tree.text[child.min_dfs:], reverse=True)

        # The first child in the sorted list is the lexicographically largest
        if children_sorted:
            large_v = children_sorted[0]
            max_range = large_v.max_dfs - large_v.min_dfs + 1
            small_v = [
                idx
                for child in children_sorted[1:]
                for idx in range(child.min_dfs, child.max_dfs + 1)
            ]


        # Step 2b: For each leaf i in Small(v), check if i + D(v) is in LL(v) and if S[i] != S[i + 2 * D(v)]
        d_v = v.string_depth
        for i in small_v:
            suffix_i = tree.get_suffix_from_dfs(i)
            suffix_j = suffix_i + d_v

            dfs_j = tree.get_dfs_from_suffix(suffix_j)

            if dfs_j and v.min_dfs <= dfs_j <= v.max_dfs: # Check if j (suffix) is in LL(v)
                if tree.text[suffix_i] != tree.text[suffix_i + 2 * d_v]:
                    btr_results.add((suffix_i, d_v))  # Report BTR (i, d(v))

        # Step 2c: For each leaf j in Small(v), check if j - D(v) is in Large(v) and if S[i] != S[i + 2 * D(v)]
        for j in small_v:
            suffix_j = tree.get_suffix_from_dfs(j)
            suffix_i = suffix_j - d_v

            dfs_i = tree.get_dfs_from_suffix(suffix_i)

            # Check if i (suffix) is in Large(v)
            if dfs_i and large_v.min_dfs <= dfs_i <= large_v.max_dfs:
                if tree.text[suffix_i] != tree.text[suffix_i + 2 * d_v]:
                    btr_results.add((suffix_i, d_v))  # Report BTR (i, d(v))

    def expand_left_rotations():
        """Expand NBTRs by checking left rotations of each tandem repeat."""
        expanded_nbtr_results = set(nbtr_results)

        for (i, l) in btr_results:
            while i > 0 and tree.text[i - 1] == tree.text[i + l - 1]:
                i -= 1
                expanded_nbtr_results.add((i, l))

        return list(expanded_nbtr_results)

    # Step 2: Process all internal nodes of the suffix tree using efficient DFS traversal
    def dfs_process(node):
        if node in marked_nodes:
            return
        process_node(node)

        for child in node.children.values():
            dfs_process(child)

    # Start processing the root node
    dfs_process(tree.root)

    expanded_nbtr_results = expand_left_rotations()
    return list(btr_results), expanded_nbtr_results


if __name__ == "__main__":
    text = "ABAABAABBBA"
    tree = SuffixTree(text)

    btr_results, nbtr_results = find_tandem_repeats(tree)

    print(f"\nBranching Tandem Repeats (BTRs) detected: {btr_results}")
    print(f"\nNon-Branching Tandem Repeats (NBTRs) with Left Rotations: {nbtr_results}")
