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
            return self._str_helper(cur_node.left) + " " + str(cur_node.value) + " " + self._str_helper(cur_node.right)



        

    
                
            



# Test
bst = BST()

bst.add_value(5)
bst.add_value(3)
bst.add_value(7)
bst.add_value(2)
bst.add_value(4)
bst.add_value(5)

#print(bst.find_value(5).value)

print(bst)