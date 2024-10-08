class RedBlackNode:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color  # 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(value=None, color='black')  
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, value):
        new_node = RedBlackNode(value, color='red', left=self.NIL, right=self.NIL)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == self.NIL:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        steps = self.fix_insert(new_node)
        return steps

    def fix_insert(self, z):
        steps = []
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
            steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        self.root.color = 'black'
        steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        return steps

def generate_latex_red_black_tree(node, rb_tree, is_root=False):
    if node == rb_tree.NIL:
        return ""

    color = node.color.lower()
    text_color = 'white'  # Color of the text
    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node [fill={color}, text={text_color}] {{{node.value}}}"
    
    children = []
    if node.left != rb_tree.NIL or node.right != rb_tree.NIL:
        if node.left != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.left, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.right, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
    
    return f"{latex_code} {' '.join(children)}"
class RedBlackNode:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color  # 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(value=None, color='black')  # Sentinel node
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, value):
        new_node = RedBlackNode(value, color='red', left=self.NIL, right=self.NIL)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == self.NIL:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        steps = self.fix_insert(new_node)
        return steps

    def fix_insert(self, z):
        steps = []
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
            steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        self.root.color = 'black'
        steps.append(generate_latex_red_black_tree(self.root, self, is_root=True))
        return steps

def generate_latex_red_black_tree(node, rb_tree, is_root=False):
    if node == rb_tree.NIL:
        return ""

    color = node.color.lower()
    text_color = 'white'  # Color of the text
    node_prefix = "\\" if is_root else ""
    latex_code = f"{node_prefix}node [fill={color}, text={text_color}] {{{node.value}}}"
    
    children = []
    if node.left != rb_tree.NIL or node.right != rb_tree.NIL:
        if node.left != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.left, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
        if node.right != rb_tree.NIL:
            children.append(f"child {{{generate_latex_red_black_tree(node.right, rb_tree)}}}")
        else:
            children.append(f"child[fill=none] {{edge from parent[draw=none]}}")
    
    return f"{latex_code} {' '.join(children)}"


def generate_latex_document_steps_red_black(steps):
    latex_code = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{tikz}
\usepackage[margin=1cm]{geometry}
\begin{document}
\section*{Introduction}
The Red-Black tree is a self-balancing binary search tree where each node is either red or black. The tree maintains balance through several properties that ensure it remains approximately balanced.

\subsection*{Step-by-Step Process}
The following figures illustrate the Red-Black tree at various stages of the insertion and balancing process:

"""
    num_steps = len(steps)
    for i in range(0, num_steps, 4):
        latex_code += r"""
\begin{figure}[h!]
\centering
"""
        for j in range(i, min(i + 4, num_steps)):
            latex_code += r"""
\begin{minipage}{0.8\textwidth}
    \centering
    \begin{tikzpicture}[level distance=15mm, sibling distance=20mm]
        \tikzstyle{every node}=[circle,inner sep=1pt, minimum size=8mm]
        \tikzstyle{level 1}=[sibling distance=60mm]
        \tikzstyle{level 2}=[sibling distance=30mm]
        \tikzstyle{level 3}=[sibling distance=15mm]
        \tikzstyle{level 4}=[sibling distance=10mm]
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

def main_red_black():
    rb_tree = RedBlackTree()
    
    predefined_values = [20, 15, 25, 10, 5]  
    for value in predefined_values:
        rb_tree.insert(value)

    steps = [generate_latex_red_black_tree(rb_tree.root, rb_tree, is_root=True)]
    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break

        try:
            value = int(user_input)
            step_result = rb_tree.insert(value)
            steps.extend(step_result)
            print(f"Node {value} added to the Red-Black tree.")

            with open("red_black_tree_steps.tex", "w") as f:
                f.write(generate_latex_document_steps_red_black(steps))
            print("LaTeX file 'red_black_tree_steps.tex' has been generated.")

        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

if __name__ == "__main__":
    main_red_black()


def main_red_black():
    rb_tree = RedBlackTree()
    
    predefined_values = [20, 15, 25, 10, 5]  
    for value in predefined_values:
        rb_tree.insert(value)

    steps = [generate_latex_red_black_tree(rb_tree.root, rb_tree, is_root=True)]
    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break

        try:
            value = int(user_input)
            step_result = rb_tree.insert(value)
            steps.extend(step_result)
            print(f"Node {value} added to the Red-Black tree.")

            with open("red_black_tree_steps.tex", "w") as f:
                f.write(generate_latex_document_steps_red_black(steps))
            print("LaTeX file 'red_black_tree_steps.tex' has been generated.")

        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

if __name__ == "__main__":
    main_red_black()
