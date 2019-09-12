import pytest
from index import sum_of_metadata, children_tree_mapping


class TestLicense():
    """ Test cases to check different input value for license file"""

    def test_sum_of_metadata(self):
        """ """
        license_num_list = iter([
            2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2
        ])
        assert sum_of_metadata(
            children_tree_mapping(license_num_list)
        ) == 138

    def test_sum_of_metadata_2(self):
        """ """
        license_num_list = iter([
            2, 2, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2
        ])
        assert sum_of_metadata(
            children_tree_mapping(license_num_list)
        ) == 136

    def test_children_tree_mapping(self):
        """ """
        license_num_list = iter([
            2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2
        ])
        assert children_tree_mapping(
            license_num_list
        ) == ([([], [10, 11, 12]), ([([], [99])], [2])], [1, 1, 2])

    def test_children_tree_mapping_2(self):
        """ """
        license_num_list = iter([
            2, 2, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2
        ])
        assert children_tree_mapping(
            license_num_list
        ) == ([([], [10, 11, 12]), ([([], [99])], [2])], [1, 1])
