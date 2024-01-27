def generate_pascal_row(row_number):
    row = [1]

    for i in range(1, row_number):
        next_number = row[i - 1] * (row_number - i) // i
        row.append(next_number)
    
    return row

def display_pascal_triangle(rows):
    for i in range(1, rows + 1):
        row = generate_pascal_row(i)
        print(" ".join(map(str, reversed(row))))

num_rows = int(input())
display_pascal_triangle(num_rows)