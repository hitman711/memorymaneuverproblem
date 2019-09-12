import os
import fileinput


def children_tree_mapping(license_num_list):
    """ As metioned in the above problem, the condition for the tree is

    A header, which is always exactly two numbers:
        1. The quantity of child nodes.
        2. The quantity of metadata entries.
        3. Zero or more child nodes (as specified in the header).
        4. One or more metadata entries (as specified in the header).
        5. Each child node is itself a node that has its own header,
        child nodes, and metadata.

    Parameters
    ----------
    <license_num_list> : <iterable object>
        License number list

    Returns
    -------
    (children, metadata) : <tuple>
        Tuple of children and list of metadata value
    """
    # First value of the list is always no. of children
    num_of_children = next(license_num_list)
    # Second value of the list id alwasy no. of metadata
    num_of_metadata = next(license_num_list)
    # Iterate to get tuple of metadata and children
    children = [
        children_tree_mapping(
            license_num_list) for i in range(num_of_children)]
    # Iterate to get list of metadata
    metadata = [
        next(license_num_list) for i in range(num_of_metadata)]
    # print(num_of_children, num_of_metadata)
    # print(children, metadata)
    return (children, metadata)


def sum_of_metadata(children_tree_mapping_list):
    """
    Sum of all metadata for each children

    Parameters
    ----------
    <children_tree_mapping_list> : <list>
        List of tuple, each tuple contain 2 values
        1. children value
        2. list of metadata entries

    Returns
    -------
    result: <int>
        Sum of all metadata entries
    """
    children, metadata = children_tree_mapping_list
    return sum(metadata) + sum(sum_of_metadata(i) for i in children)


# License number input
license_num_list = map(
    int,
    next(fileinput.input(os.getcwd() + '/license.txt')).split()
)

print(
    "Sum of metadata entries -> ",
    sum_of_metadata(
        children_tree_mapping(license_num_list)
    )
)
