from pylatex import Document, Command, NoEscape

# لیستی برای ثبت مراحل و جابه‌جایی‌ها
steps = []
swaps = []  # لیستی برای ثبت جابه‌جایی‌ها

# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            update_steps(array, i, j)

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    update_steps(array, i + 1, high)

    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
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
    tikz_code = []
    num_steps = len(steps)
    
    # Calculate the width of the image based on the number of elements
    if steps:
        num_elements = len(steps[0])
        total_width = num_elements * square_size
    else:
        total_width = 0

    # Add TikZ code for each step
    for i, (step, swap) in enumerate(zip(steps, swaps)):
        tikz_code.append(f"% Step {i + 1}\n")
        tikz_code.append(r"\begin{tikzpicture}")
        
        for j, value in enumerate(step):
            # رنگ بر اساس مقدار
            color = base_color
            if swap:
                if j == swap[0]:
                    color = swap_color1
                elif j == swap[1]:
                    color = swap_color2

            color = f"{{rgb,255:red,{color[0]};green,{color[1]};blue,{color[2]}}}"
            
            # موقعیت افقی هر مربع
            position_x = j * square_size
            # موقعیت عمودی هر مربع
            position_y = 0
            # موقعیت عمودی برای اندیس‌ها
            index_y_position = square_size 
            # موقعیت عمودی برای لیبل pivot
            pivot_label_y_position = -0.5
            
            # اندازه فونت متن
            font_size = square_size * 0.5  # Adjust font size relative to square size
            
            tikz_code.append(f"\\node[draw=black, fill={color}, minimum size={square_size}cm] at ({position_x},{position_y}) {{{value}}};")
            tikz_code.append(f"\\node[font=\\fontsize{{{font_size}pt}}{{{font_size}pt}}] at ({position_x},{index_y_position}) {{{j}}};")  # اندیس‌ها بالای خانه‌های آرایه

            # اگر عنصر pivot است
            if swap and j == swap[1]:
                tikz_code.append(f"\\draw[black] ({position_x},{position_y}) circle[radius=0.5cm];")
                tikz_code.append(f"\\node[font=\\small, anchor=north] at ({position_x},{pivot_label_y_position}) {{pivot}};")
        
        tikz_code.append(r"\end{tikzpicture}")
        tikz_code.append(r"\vspace{0.5cm}")

    # Save the TikZ code to a file
    with open(filename, 'w') as f:
        f.write('\n'.join(tikz_code))

def generate_document_with_tikz(tikz_filename):
    doc = Document()
    
    # افزودن پکیج‌ها و تنظیمات
    doc.preamble.append(Command('usepackage', 'tikz'))  # اضافه کردن پکیج tikz برای نمودارها
    doc.preamble.append(Command('usepackage', 'xcolor'))  # اضافه کردن پکیج xcolor برای رنگ‌ها
    doc.preamble.append(Command('usepackage', 'float'))  # برای استفاده از [H] در محیط figure

    # افزودن کدهای TikZ به فایل LaTeX
    with open(tikz_filename, 'r') as f:
        tikz_code = f.read()
    doc.append(NoEscape(tikz_code))

    doc.generate_pdf('quick_sort_visualization', clean_tex=False)

# Main function to get user input and sort the array
if __name__ == "__main__":
    # Taking input from the user
    user_input = input("Enter numbers separated by spaces: ")
    data = list(map(int, user_input.split()))

    # Get square size from user
    square_size = get_square_size()

    # Get colors from user
    base_color, swap_color1, swap_color2 = get_colors()

    # Initial step
    update_steps(data, -1, -1)  # No swaps at the beginning
    quickSort(data, 0, len(data) - 1)

    # Save steps as TikZ
    tikz_filename = 'quick_sort_tikz.tex'
    save_steps_as_tikz(steps, swaps, tikz_filename, square_size, base_color, swap_color1, swap_color2)
    generate_document_with_tikz(tikz_filename)
