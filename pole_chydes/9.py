def remove_line(file_name, line_to_remove):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            for line in lines:
                if line.strip != line_to_remove.strip():
                    file.write(line)


    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")
