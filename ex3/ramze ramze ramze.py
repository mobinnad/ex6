def process_and_print_sorted_items(user_input):
    items = user_input.split(' ')
    sorted_items = sorted(items, key=lambda x: int(x[1:]))
    for item in sorted_items:
        print(item[0], end='')

def get_user_input():
    return input()


user_input = get_user_input()
process_and_print_sorted_items(user_input)
