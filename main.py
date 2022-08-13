from typing import Optional

class Node():
    def __init__(self, lft, rgt, val):
        self.lft: Optional[Node] = lft
        self.rgt: Optional[Node] = rgt
        self.val: int = val

    def __str__(self):
        if self.lft == None and self.rgt == None:
            return f"{self.val}"
        else:
            return f"[\n   value:{self.val}\n   left:{str(self.lft)}\n   right:{str(self.rgt)}\n]"

class Tree():
    def __init__(self, depth):
        self.root: Node = Node(None, None, 0)
        self.build_tree(self.root, depth)

    def __str__(self) -> str:
        return str(self.root)

    def build_tree(self, rel_node: Node, depth: int, val: int = 1) -> None:
        if depth == 1:
            rel_node.lft = Node(None, None, val)
            rel_node.rgt = Node(None, None, val)
            return None
        
        rel_node.lft = Node(None, None, val)
        self.build_tree(rel_node.lft, depth-1, val+1)
        rel_node.rgt = Node(None, None, val)
        self.build_tree(rel_node.rgt, depth-1, val+1)

    
    def _remove_children(self, node):
        if node.lft != None:
            self._remove_children(node.lft)
            # free(node.lft)
            node.lft = None
        if node.rgt != None:
            self._remove_children(node.rgt)
            # free(node.rgt)
            node.rgt = None

        
    def remove(self, val: int, node: Optional[Node] = None) -> bool:
        if node == None:
            node = self.root
        if node.val == val:
            return False
        if node.lft != None and node.lft.val == val:
            self._remove_children(node.lft)
            # free(node.lft)
            node.lft = None
            return True
        if node.rgt != None and node.rgt.val == val:
            self._remove_children(node.rgt)
            # free(node.rgt)
            node.rgt = None
            return True
        if (node.lft != None and self.remove(val, node.lft)) or \
           (node.rgt != None and self.remove(val, node.rgt)):
            return True
        else:
            return False
        
    def print_tree(self, tree = None, depth = 0):
        if tree == None:
            tree = self.root


        if tree.lft != None:
            self.print_tree(tree.lft, depth+1)
        else:
            print(" ", end="")

        for _ in range(depth):
            print("   ", end="")
        print(tree.val)

        if tree.rgt != None:
            self.print_tree(tree.rgt, depth+1)
        else:
            print(" ", end="")


        
def main():
    tree: Tree = Tree(3)
    tree.print_tree()
    tree.remove(2)
    tree.remove(3)
    print("")
    print("-------------------------------------------------------------")
    print("")
    tree.print_tree()

if __name__ == "__main__":
    main()
