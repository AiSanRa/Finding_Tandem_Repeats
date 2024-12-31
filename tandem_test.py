import unittest
from s_tree import SuffixTree # Import the SuffixTree class
from sent_gust_first import find_tandem_repeats  # Import the find_tandem_repeats function

class TestTandemRepeats(unittest.TestCase):
    """
    A collection of tests to verify the functionality of the tandem repeats detection
    in a suffix tree. This class contains tests for various cases including simple, 
    overlapping, branching, and edge cases.
    """

    def test_simple_repeats(self):
        """
        Test case for simple, non-branching repeats. In this case, the string has a 
        clear repeated pattern that does not branch.
        """
        text = "AACTGCAACTG"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        # Assert non-branching repeats are detected at expected positions
        self.assertIn((0, 1), btr)  # "AA" is a non-branching repeat at the start
        self.assertIn((6, 1), btr)  # "AA" in the second half is non-branching

    def test_branching_repeats(self):
        """
        Test case where there are branching repeats. The repeats can be found, 
        but they branch, i.e., multiple substrings share the same prefix.
        """
        text = "ACTGACTGACTTG"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        # Assert branching repeats are detected at expected positions
        self.assertIn((3, 4), btr)  # "TGAC" is a branching repeat
        self.assertIn((10, 1), btr)  # "TT" is a branching repeat
        self.assertIn((2, 4), nbtr)  # "TGAC" is non-branching
        self.assertIn((0, 4), nbtr)  # "ACTG" is non-branching
        self.assertIn((1, 4), nbtr)  # "CTGA" is non-branching

    def test_overlapping_repeats(self):
        """
        Test case for overlapping non-branching repeats where repeats share characters.
        """
        text = "ABAABAABB"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        self.assertIn((1, 3), nbtr)  # "BAA" is a non-branching repeat
        self.assertIn((0, 3), nbtr)  # "ABA" is a non-branching repeat
        self.assertIn((7, 1), nbtr)  # "B" is a non-branching repeat
        self.assertIn((2, 1), btr)  # "A" is a branching repeat
        self.assertIn((2, 3), btr)  # "AAB" is a branching repeat
        self.assertIn((5, 1), btr)  # "A" is a branching repeat
        self.assertIn((8, 1), btr)  # "A" is a branching repeat

    def test_no_repeats(self):
        """
        Test case with a string that has no tandem repeats.
        """
        text = "ACGT"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        # Assert no repeats are found in a string with no repetition

        self.assertEqual(btr, [])
        self.assertEqual(nbtr, [])


if __name__ == "__main__":
    unittest.main()