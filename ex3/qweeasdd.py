input_text = list(input())  
index = 0  

while index < len(input_text):
    if input_text[index] == '@':
        temp_index = index + 1  
        while temp_index < len(input_text):
            if input_text[temp_index] == '#':
                input_text.pop(temp_index)
                break
            else:
                temp_index += 1
        index += 1
    else:
        index += 1

formatted_text = ''.join(input_text)
formatted_text = ' '.join(formatted_text.split())
formatted_text = formatted_text.replace("\\n", "\n")
formatted_text = formatted_text.replace("\\t", "\t")

print(f"Formatted Text: {formatted_text}")
