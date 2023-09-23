def write_to_file(file_name, content, mode):
    with open(file_name, mode) as file:
        file.write(content)
