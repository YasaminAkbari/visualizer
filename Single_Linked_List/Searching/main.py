class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def generate_latex_for_state(self, highlight=None, highlight_color="red"):
        if not self.head:
            return ""
        
        latex_code = ""
        current = self.head
        node_counter = 1
        
        while current:
            if highlight == current:
                latex_code += f"    \\node[list,on chain,fill={highlight_color}] (N{node_counter}) {{\\nodepart{{second}} {current.value}}};\n"
            else:
                latex_code += f"    \\node[list,on chain] (N{node_counter}) {{\\nodepart{{second}} {current.value}}};\n"
            current = current.next
            node_counter += 1
        
        for i in range(node_counter - 2):
            latex_code += f"    \\path[*->] let \\p1 = (N{i+1}.three), \\p2 = (N{i+1}.center) in (\\x1,\\y2) edge [bend left] ($(N{i+2}.one)+(0.1,0.06)$);\n"
        
        return latex_code
    
    def generate_combined_latex(self, steps):
        latex_code = r"\documentclass[10pt,a4paper]{article}" + "\n"
        latex_code += r"\usepackage[T1]{fontenc}" + "\n"
        latex_code += r"\usepackage{tikz}" + "\n"
        latex_code += r"\usepackage[margin=1cm]{geometry}" + "\n"
        latex_code += r"\usetikzlibrary{calc,shapes.multipart,chains,arrows,positioning}" + "\n"
        latex_code += r"\tikzset{list/.style={very thick, rectangle split, rectangle split parts=3, draw, rectangle split horizontal, minimum size=18pt, inner sep=5pt, text=black, rectangle split part fill={blue!20, red!20, green!20}}, ->, start chain=going right, very thick}" + "\n"
        latex_code += r"\begin{document}" + "\n"
        
        for i, step in enumerate(steps):
            latex_code += f"\\section*{{Step {i + 1}}}\n"
            latex_code += r"\begin{tikzpicture}" + "\n"
            latex_code += step
            latex_code += r"\end{tikzpicture}" + "\n"
        
        latex_code += r"\end{document}"
        
        return latex_code

    def search(self, value):
        steps = []
        current = self.head
        
        while current:
            if current.value == value:
                steps.append(self.generate_latex_for_state(highlight=current, highlight_color="green"))
                print(f"Value {value} found in the list.")
                break
            else:
                steps.append(self.generate_latex_for_state(highlight=current, highlight_color="red"))
            current = current.next
        
        if not current:
            print(f"Value {value} not found in the list.")
        
        return steps

dll = SingleLinkedList()
steps = []

initial_values = [12, 99, 100, 250]
for value in initial_values:
    dll.append(value)
    #steps.append(dll.generate_latex_for_state())

search_value = int(input("Enter a value to search in the Single linked list: "))
search_steps = dll.search(search_value)
steps.extend(search_steps)

combined_latex_code = dll.generate_combined_latex(steps)

with open("Single_linked_list_steps.tex", "w") as file:
    file.write(combined_latex_code)

print("Step-by-step LaTeX code generated and saved to Single_linked_list_steps.tex")
