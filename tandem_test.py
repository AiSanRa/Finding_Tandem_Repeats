import unittest
from tree import SuffixTree 
from gust_tadem import find_tandem_repeats  

class TestTandemRepeats(unittest.TestCase):
    """
    A collection of tests to verify the functionality of the tandem repeats detection
    in a suffix tree. This class contains tests for various cases including simple, 
    overlapping, branching, and edge cases.
    """

    def test_simple_repeats(self):

        text = "AACTGCAACTG"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        self.assertIn((0, 1), btr)  # "AA" is a non-branching repeat at the start
        self.assertIn((6, 1), btr)  # "AA" in the second half is non-branching

    def test_branching_repeats(self):

        text = "ACTGACTGACTTG"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        self.assertIn((3, 4), btr)  # "GACT" is a branching repeat
        self.assertIn((10, 1), btr)  # "TT" is a branching repeat
        self.assertIn((2, 4), nbtr)  # "TGAC" is non-branching
        self.assertIn((0, 4), nbtr)  # "ACTG" is non-branching
        self.assertIn((1, 4), nbtr)  # "CTGA" is non-branching

    def test_overlapping_repeats(self):

        text = "ABAABAABBBA"
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

        text = "ACGT"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        self.assertEqual(btr, [])
        self.assertEqual(nbtr, [])

    def test_for_fun(self):

        text = "mississippi"
        tree = SuffixTree(text)
        btr, nbtr = find_tandem_repeats(tree)

        self.assertIn((1, 3), nbtr)  # "mis" is a non-branching repeat
        self.assertIn((2, 1), btr)  # "i" is a branching repeat
        self.assertIn((2, 3), btr)  # "iss" is a branching repeat
        self.assertIn((5, 1), btr)  # "s" is a branching repeat
        self.assertIn((8, 1), btr)  # "p" is a branching repeat

if __name__ == "__main__":
    unittest.main()
