try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as fh:
    print(f"An error occurred: {fh}")


