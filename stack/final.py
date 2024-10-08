from pylatex import Document, Section, NoEscape, TikZ, MiniPage, Package

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

def draw_stack(tikz, stack, caption, width, item_height, total_items, base_color, highlight_index=None, highlight_color='#a5e6e2'):
    height = total_items * item_height
    font_size = item_height * 10
    
    # Fill the stack items
    for i in range(total_items):
        fill_color = base_color
        if i < len(stack):
            if i == highlight_index:
                fill_color = highlight_color
            tikz.append(NoEscape(r'\fill[fill={rgb,255:red,%d;green,%d;blue,%d}] (0, %f) rectangle (%f, %f);' % (
                int(fill_color[1:3], 16),
                int(fill_color[3:5], 16),
                int(fill_color[5:7], 16),
                i * item_height, width, (i + 1) * item_height)))
            item = stack[i]
            tikz.append(NoEscape(r'\node[font=\fontsize{%f}{%f}\selectfont] at (%f, %f) {%s};' % (font_size, font_size * 1.2 ,width / 2, (i + 0.5) * item_height, item)))
    
    # Draw the stack border and separators
    tikz.append(NoEscape(r'\draw[thick] (0, 0) rectangle (%f, %f);' % (width, height)))
    for i in range(total_items - 1):
        tikz.append(NoEscape(r'\draw[thick] (0, %f) -- (%f, %f);' % ((i + 1) * item_height, width, (i + 1) * item_height)))
    
    # Adjust font size for caption
    caption_font_size = item_height * 10
    tikz.append(NoEscape(r'\node[font=\fontsize{%f}{%f}\selectfont] at (%f, -0.5) {%s};' % (caption_font_size, caption_font_size * 1.2, width / 2, caption)))

def create_latex_document(elements, width, item_height, total_items, base_color, highlight_color, images_per_row):
    geometry_options = {
        "top": "3cm",
        "bottom": "2cm",
        "left": "2cm",
        "right": "2cm"
    }

    doc = Document(geometry_options=geometry_options)
    doc.packages.append(Package('float'))

    with doc.create(Section('Stack Operations')):
        doc.append(NoEscape(r"""
        \section*{Introduction}
        In programming and computer science, Stack is one of the important data structures that operate as a "last in, first out" (LIFO) structure. In other words, the last element added to the stack is the first element removed.
        """))
        doc.append(NoEscape(r'\vspace{1cm}'))
        stack = Stack()

        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\begin{tabular}{' + 'c' * images_per_row + '}'))
        max_stack_height = (total_items + 1) * item_height
        for i, element in enumerate(elements):
            stack.push(str(element))
            with doc.create(MiniPage(width=NoEscape(r'0.2\textwidth'), height=NoEscape(f'{max_stack_height}pt'), align='c')) as minipage:
                minipage.append(NoEscape(r'\centering'))
                with minipage.create(TikZ()) as tikz:
                    draw_stack(tikz, stack.items, f'Pushed: {element}', width, item_height, total_items, base_color, highlight_index=i, highlight_color=highlight_color)
                    doc.append(NoEscape(r'\vspace{1cm}'))
            if (i + 1) % images_per_row == 0:
                doc.append(NoEscape(r'\\[2ex]'))
                doc.append(NoEscape(r'\vspace{1cm}'))
            else:
                doc.append(NoEscape(r' & '))
        doc.append(NoEscape(r'\end{tabular}'))
        doc.append(NoEscape(r'\end{center}'))
        
        doc.append(NoEscape(r'\vspace{2cm}'))

        doc.append(NoEscape(r'\begin{center}'))
        doc.append(NoEscape(r'\begin{tabular}{' + 'c' * images_per_row + '}'))
        i = 0
        while not stack.is_empty():
            popped_element = stack.pop()
            with doc.create(MiniPage(width=NoEscape(r'0.2\textwidth'), height=NoEscape(f'{max_stack_height}pt'), align='c')) as minipage:
                minipage.append(NoEscape(r'\centering'))
                with minipage.create(TikZ()) as tikz:
                    draw_stack(tikz, stack.items, f'Popped: {popped_element}', width, item_height, total_items, base_color)
                    doc.append(NoEscape(r'\vspace{1cm}'))
            if (i + 1) % images_per_row == 0:
                doc.append(NoEscape(r'\\[2ex]'))
                doc.append(NoEscape(r'\vspace{1cm}'))
            else:
                doc.append(NoEscape(r' & '))
            i += 1
        doc.append(NoEscape(r'\end{tabular}'))
        doc.append(NoEscape(r'\end{center}'))

    doc.generate_pdf('stack_operations', clean_tex=False)

if __name__ == "__main__":
    user_input = input("Enter the elements separated by spaces: ")
    elements = user_input.split()
    
    width = float(input("Enter the width of the rectangle: "))
    item_height = float(input("Enter the height of each item: "))
    total_items = len(elements)

    base_color = input("Enter the base color in HEX (e.g., #ffffff): ")
    highlight_color = input("Enter the highlight color in HEX (e.g., #a5e6e2): ")
    images_per_row = int(input("Enter the number of images per row: "))

    create_latex_document(elements, width, item_height, total_items, base_color, highlight_color, images_per_row)
