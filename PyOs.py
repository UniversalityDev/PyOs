import osimport os

# ASCII art using fsymbols.com
prompt_ascii = """

╭━━━╮╱╱╱╭━━━╮
┃╭━╮┃╱╱╱┃╭━╮┃
┃╰━╯┣╮╱╭┫┃╱┃┣━━╮
┃╭━━┫┃╱┃┃┃╱┃┃━━┫
┃┃╱╱┃╰━╯┃╰━╯┣━━┃
╰╯╱╱╰━╮╭┻━━━┻━━╯
╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯
"""

# Dictionary of available commands 
commands = {
    "help": "Display available commands",
    "dir": "List files in the current directory",
    "create": "Create a new file",
    "edit": "Edit a text file",
    "exit": "Exit the program",
    "cls": "Clear the console screen"
}

# Main program loop we love a while true
while True:
    print(prompt_ascii)
    print("Type 'help' for a list of commands.")

    user_input = input("> ").lower()

    if user_input == "help":
        print("Available commands:")
        for cmd, explanation in commands.items():
            print(f"{cmd}: {explanation}")

    elif user_input == "dir":
        file_list = "\n".join(file for file in os.listdir() if os.path.isfile(file))
        print("Files in the current directory:")
        print(file_list)

    elif user_input == "create":
        new_file_name = input("Enter the name of the new file: ")
        with open(new_file_name, 'w') as new_file:
            print(f"File '{new_file_name}' created.")

    elif user_input == "edit":
        file_to_edit = input("Enter the name of the file to edit: ")
        if os.path.isfile(file_to_edit):
            with open(file_to_edit, 'r') as f:
                file_content = f.read()
            new_content = file_content.splitlines()
            print(f"Editing '{file_to_edit}'. Edit the content below. Type 'save' to save changes.")
            while True:
                for index, line in enumerate(new_content, start=1):
                    print(f"{index}: {line}")
                edit_line = input("Type line number or 'save': ")
                if edit_line.lower() == "save":
                    with open(file_to_edit, 'w') as f:
                        f.write("\n".join(new_content))
                    print(f"Changes saved to '{file_to_edit}'.")
                    break
                try:
                    line_number = int(edit_line) - 1
                    if 0 <= line_number < len(new_content):
                        new_content[line_number] = input(f"Edit line {edit_line}: ")
                    else:
                        print("Invalid line number.")
                except ValueError:
                    print("Invalid input. Type a line number or 'save'.")

        else:
            print(f"File '{file_to_edit}' not found.")

    elif user_input == "exit":
        print("Exiting the program.")
        break

    elif user_input == "cls":
        os.system("cls" if os.name == "nt" else "clear")  # Clear console 

    else:
        print("Invalid command. Type 'help' for a list of commands.")

