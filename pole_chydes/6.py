def write_to_file(file_name):
    try:
        user_input = input("Enter your text: ")
        with open(file_name, 'w') as file:
            file.write(user_input)
        print(f"Text was successfully written to file '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")


file_name = "output.txt"
write_to_file(file_name)