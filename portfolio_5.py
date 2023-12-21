#Task 1
import sys

def get_os_platform():
    return sys.platform

if __name__ == "__main__":
    platform = get_os_platform()
    print("Operating System Platform:", platform)

#Task 2
import sys

args = sys.argv[1:]

num_args = len(args)

print(f"Number of arguments provided: {num_args}")

#Task 3
import sys

args = sys.argv[1:]

if not args:
    print("No arguments provided.")
else:
    args.sort(key=len)

    shortest = args[0]

    print("Shortest argument:", shortest)



#Task 4
import sys
import requests

def check_website_status(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        is_working = check_website_status(url)

        if is_working:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} is not working or does not exist.")


# For task 4, I did not understand so I used chat gtp to help out


# Task 5

import sys

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperatures provided. Please enter temperature values.")
        return

    temperatures = list(map(float, temperatures))
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"Maximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Mean Temperature: {mean_temp}")

if __name__ == "__main__":
    command_line_arguments = sys.argv[1:]
    process_temperatures(command_line_arguments)


# Task 6

import sys
import shutil


def create_backup(original_file):
    try:
        backup_file = original_file + ".bak"

        shutil.copy2(original_file, backup_file)

        print(f"Backup created successfully: {backup_file}")
    except FileNotFoundError:
        print(f"Error: The file '{original_file}' does not exist.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python backup_creator.py <filename>")
    else:
        filename = sys.argv[1]
        create_backup(filename)
