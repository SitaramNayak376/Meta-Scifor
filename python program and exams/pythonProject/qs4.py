def add_serial_numbers():
    with open("D:\\bbb.txt", 'r') as file:
        lines = file.readlines()

    numbered_lines = [f"{index + 1}: {line}" for index, line in enumerate(lines)]

    with open(file_path, 'w') as file:
        file.writelines(numbered_lines)

    print("Serial numbers added successfully.")

