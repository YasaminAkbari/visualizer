from collections import deque

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def breadth_first_traversal(root, steps):
    if not root:
        return
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        steps.append(generate_latex_binary_tree(root, target=node.value, is_root=True))

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def generate_latex_binary_tree(node, target=None, is_root=False):
    if not node:
        return ""

    node_prefix = "\\" if is_root else ""

    if node.value == target:
        latex_code = f"{node_prefix}node[fill=lime!60] {{{node.value}}}"
    else:
        latex_code = f"{node_prefix}node {{{node.value}}}"
    
    children = []
    if node.left or node.right:
        if node.left:
            children.append(f"child {{{generate_latex_binary_tree(node.left, target=target)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right:
            children.append(f"child {{{generate_latex_binary_tree(node.right, target=target)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
    
    return f"{latex_code} {' '.join(children)}"

def generate_latex_document_steps(steps):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}

\section*{Binary Serach Tree Traversal Algorithms}
In this document, we illustrate the process of traversing a binary search tree using different traversal algorithms. The traversal methods covered are:
The main idea of level order traversal is to traverse all the nodes of a lower level before moving to any of the nodes of a higher level.

\section*{Detailed Traversal Steps}
The following figures illustrate the binary search tree at various stages of traversal. Each figure shows the state of the tree with the current node being processed highlighted.

"""

    for i in range(0, len(steps), 4):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 4, len(steps))):
            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=10mm]
        \tikzstyle{every node}=[fill=green!75,circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=40mm, set style={{every node}+=[fill=green!60]}]
        \tikzstyle{level 2}=[sibling distance=20mm, set style={{every node}+=[fill=green!45]}]
        \tikzstyle{level 3}=[sibling distance=15mm, set style={{every node}+=[fill=green!30]}]
        \tikzstyle{level 4}=[sibling distance=10mm, set style={{every node}+=[fill=green!15]}]
        """ + steps[j] + ";" + r"""
    \end{tikzpicture}
    \caption{Step """ + str(j + 1) + r"""}
\end{minipage}
\vspace{1cm}
"""
        
        latex_code += r"""
\end{figure}
\newpage
"""

    latex_code += r"""
\end{document}
"""
    return latex_code

def main():
    # Define a Binary Search Tree (BST)
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(20)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(25)

    steps = []
    breadth_first_traversal(root, steps)

    latex_document = generate_latex_document_steps(steps)
    filename = "bst_bfs_steps.tex"

    with open(filename, "w") as file:
        file.write(latex_document)

    print(f"LaTeX code for binary search tree BFS steps has been generated and saved to {filename}")

if __name__ == "__main__":
    main()
