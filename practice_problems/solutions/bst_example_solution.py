class BST:

    class Node:

        def __init__(self, value):

            self.left = None
            self.right = None

            self.value = value
 


    def __init__(self):

        self.root = None

    
    def add_value(self, new_value):

        if self.root == None:

            self.root = self.Node(new_value)

        else:

            # Recurses to find a place for the new value
            self._add_value(self.root, new_value)
 

    def _add_value(self, cur_node, new_value):


        # Handles going left
        if new_value < cur_node.value:

            # Checks if this is empty
            # If it is, then set the left 
            # as the value
            if cur_node.left is None:
                cur_node.left = self.Node(new_value) 

            # Since it is not none, we recurse
            else:

                self._add_value(cur_node.left, new_value)

        # For going right
        else:

            # checks if right is None
            if cur_node.right is None:
                cur_node.right = self.Node(new_value)

            # Recurses if right is something
            else:

                self._add_value(cur_node.right, new_value)

    def to_list(self):

        """
            This should return a list of all the items
            in the BST.

            HINT: Use recursion, and reference the
            __str__ method.
        """

        if self.root is None:
            return []

        else:

            return self._arr_helper(self.root) 

    def _arr_helper(self, cur_node, arr=None):

        # Initialize the array if it wasn't passed in
        if arr is None:
            arr = []

        # Check if cur_node is the end of a branch
        if cur_node is None:
            return

        else:

            # Recurse left, append cur_node.value, recurse right, then return the arr
            # Notice that when we recurse, we don't save the returned arr. The returned
            # arr is only saved when we pass it back to to_array() and thus returned back
            # to the initial call
            self._arr_helper(cur_node.left, arr)
            arr.append(cur_node.value)
            self._arr_helper(cur_node.right, arr)
            return arr

    def find_item(self, value):
        """
            This should return the Node object
            of that Item. 

            HINT: Use recursion, and reference the
            __str__ method.
        """

        if self.root is None:
            return "Item Not Found"

        else:

            return self._find_helper(self.root, value)


         

    def _find_helper(self, cur_node, value):


        if cur_node.value == value:
            return cur_node

        else:

            if value < cur_node.value:
                # Recurses left
                return self._find_helper(cur_node.left, value)

            else:
                # Recurses right
                return self._find_helper(cur_node.right, value)



    def __str__(self):

        # Checks if the tree is none
        if self.root is None:
            return "Tree is empty!"

        # Else call helper method
        else:
            return self._str_helper(self.root)

    def _str_helper(self, cur_node):

        if cur_node is None:
            return ""

        else:


            # Recurses with left, self, then right
            left_branch_str = self._str_helper(cur_node.left)
            this_node_val = str(cur_node.value)
            right_branch_str = self._str_helper(cur_node.right)

            full_str = left_branch_str + " " + this_node_val + " " + right_branch_str

            return full_str



# Test
bst = BST()

bst.add_value(5)
bst.add_value(3)
bst.add_value(7)
bst.add_value(2)
bst.add_value(4)
bst.add_value(5)


print(bst) # Should print  2  3  4  5  5  7 

print(bst.to_list()) # Should print [2, 3, 4, 5, 5, 7]

print(bst.find_item(5).value) # Should print a 5