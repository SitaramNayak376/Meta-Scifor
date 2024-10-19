def remove_duplicate_words():
    def remove_duplicates_from_line(line):
        words = line.split()
        seen = set()
        result = []
        for word in words:
            if word.lower() not in seen:
                seen.add(word.lower())
                result.append(word)
        return ' '.join(result)

    with open("D:\\aaa.txt", 'r') as file:
        lines = file.readlines()

    updated_lines = [remove_duplicates_from_line(line) for line in lines]

    with open("D:\\aaa.txt", 'w') as file:
        file.writelines(updated_lines)

    print("Duplicate words removed successfully.")



