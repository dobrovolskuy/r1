def copi_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            content = source.read()
            destination.write(content)
        print(f"file '{source_file}' successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"there's been a mistake: {e}")

