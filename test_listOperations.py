import unittest
from listOperations import filter_list

class TestFilterList(unittest.TestCase):

    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        expected_filtered_list = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]
        filtered_list = filter_list(input_list)
        self.assertListEqual(filtered_list, expected_filtered_list)

    def test_invalid_input_length(self):
        input_list = list(range(1, 26))
        with self.assertRaises(ValueError) as context:
            filter_list(input_list)
        self.assertEqual(str(context.exception), 'Input list length must be a multiple of 10')

    def test_empty_input(self):
        input_list = []
        filtered_list = filter_list(input_list)
        self.assertListEqual(filtered_list, [])

if __name__ == '__main__':
    unittest.main()
