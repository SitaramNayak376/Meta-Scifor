def replace_word_in_file(file_path, incorrect_word, correct_word):

    with open("D:\\bbb.txt", 'r') as file:
        content = file.read()

    updated_content = content.replace(incorrect_word, correct_word)
    with open(file_path, 'w') as file:
        file.write(updated_content)

    print(f"The word '{incorrect_word}' has been replaced with '{correct_word}' successfully.")

file_path = 'programming_text_file.txt'
incorrect_word = 'languge'
correct_word = 'language'
replace_word_in_file(file_path, incorrect_word, correct_word)
