import OpenEXR


def read_exr_tree(file_path):
    # Open the EXR file
    exr_file = OpenEXR.InputFile(file_path)

    # Get the root node
    root_node = exr_file.header()['dataWindow']

    # Extract the tree structure
    tree_structure = {}
    _traverse_tree(exr_file, root_node, tree_structure)

    # Close the EXR file
    exr_file.close()

    return tree_structure


def _traverse_tree(exr_file, node, tree_structure):
    node_name = f"{node.xMin}-{node.yMin}_{node.xMax}-{node.yMax}"
    tree_structure[node_name] = {}

    # Check if the current node has children
    if node.hasChildren():
        child_nodes = node.children()
        for child_node in child_nodes:
            _traverse_tree(exr_file, child_node, tree_structure[node_name])


# Specify the path to your EXR file
file_path = './input.exr'

# Read the EXR file tree structure
tree_structure = read_exr_tree(file_path)

# Print the tree structure


def print_tree_structure(tree, indent=0):
    for key, value in tree.items():
        print(f"{'  ' * indent}Node: {key}")
        print_tree_structure(value, indent + 1)


print_tree_structure(tree_structure)
