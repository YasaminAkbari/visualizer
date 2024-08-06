from pylatex import Document, Command, NoEscape, Package, Section, Figure, TikZ
from pylatex.utils import italic

# لیستی برای ثبت مراحل و جابه‌جایی‌ها
steps = []
swaps = []  # لیستی برای ثبت جابه‌جایی‌ها

# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            update_steps(array, i, j)
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    update_steps(array, i + 1, high)
    return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# به‌روزرسانی مراحل و جابه‌جایی‌ها
def update_steps(array, index1, index2):
    steps.append(array.copy())
    if index1 >= 0 and index2 >= 0:
        swaps.append((index1, index2))
    else:
        swaps.append(None)  # برای عدم وجود جابه‌جایی معتبر

def get_square_size():
    while True:
        try:
            size = float(input("Enter the size of the squares (e.g., 1 or larger): "))  # Enter size in cm or any other unit
            if size <= 0:
                print("Size must be a positive number.")
            else:
                return size
        except ValueError:
            print("Please enter a valid number.")

def get_colors():
    base_color = input("Base color (in format r,g,b with values from 0 to 255): ")
    swap_color1 = input("Swap color 1 (in format r,g,b with values from 0 to 255): ")
    swap_color2 = input("Swap color 2 (in format r,g,b with values from 0 to 255): ")
    try:
        base_color = tuple(map(int, base_color.split(',')))
        swap_color1 = tuple(map(int, swap_color1.split(',')))
        swap_color2 = tuple(map(int, swap_color2.split(',')))
        if len(base_color) == 3 and len(swap_color1) == 3 and len(swap_color2) == 3:
            return base_color, swap_color1, swap_color2
        else:
            print("Please enter valid RGB values.")
            return get_colors()
    except ValueError:
        print("Please enter valid RGB values.")
        return get_colors()

def save_steps_as_tikz(steps, swaps, filename, square_size, base_color, swap_color1, swap_color2):
    doc = Document()
    doc.preamble.append(Package('tikz'))
    doc.preamble.append(Package('xcolor'))
    
    with doc.create(Section('Quick Sort Visualization')):
        num_steps = len(steps)
        if steps:
            num_elements = len(steps[0])
            total_width = num_elements * square_size
        else:
            total_width = 0

        for i, (step, swap) in enumerate(zip(steps, swaps)):
            with doc.create(Figure(position='h!')) as fig:
                with fig.create(TikZ()) as tikz:
                    for j, value in enumerate(step):
                        color = base_color
                        if swap:
                            if j == swap[0]:
                                color = swap_color1
                            elif j == swap[1]:
                                color = swap_color2
                        color = f"{{rgb,255:red,{color[0]};green,{color[1]};blue,{color[2]}}}"
                        position_x = j * square_size
                        position_y = 0
                        index_y_position = square_size 
                        pivot_label_y_position = -0.5
                        font_size = square_size * 0.5
                        
                        tikz.append(NoEscape(f"\\node[draw=black, fill={color}, minimum size={square_size}cm] at ({position_x},{position_y}) {{{value}}};"))
                        tikz.append(NoEscape(f"\\node[font=\\fontsize{{{font_size}pt}}{{{font_size}pt}}] at ({position_x},{index_y_position}) {{{j}}};"))
                        if swap and j == swap[1]:
                            tikz.append(NoEscape(f"\\draw[black] ({position_x},{position_y}) circle[radius=0.5cm];"))
                            tikz.append(NoEscape(f"\\node[font=\\small, anchor=north] at ({position_x},{pivot_label_y_position}) {{pivot}};"))
                fig.add_caption(f"Step {i + 1} of the quicksort algorithm")
                
    doc.generate_pdf(filename.replace('.tex', ''), clean_tex=False)

# Main function to get user input and sort the array
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    data = list(map(int, user_input.split()))

    square_size = get_square_size()
    base_color, swap_color1, swap_color2 = get_colors()

    update_steps(data, -1, -1)  # No swaps at the beginning
    quickSort(data, 0, len(data) - 1)

    tikz_filename = 'quick_sort_tikz.tex'
    save_steps_as_tikz(steps, swaps, tikz_filename, square_size, base_color, swap_color1, swap_color2)
