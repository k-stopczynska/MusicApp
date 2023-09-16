def write_to_file(file_name, content):
    with open(file_name, "wb") as file:
        file.write(content)
        file.close()