import os


def clean(filepath):
    # lists all files in that directory
    for filename in os.listdir(source_deleting):
        # gets filepath of that file
        filetype1 = filename[-n:]
        if (filetype1 == file_type):
            file = os.path.join(source_deleting, filename)
            if os.path.isfile(file):
                os.remove(file)


print("Welcome to Cleaner\n")
print("CAUTION: IT PERMANENTLY DELETES ALL FILES WITH THE FILE TYPE YOU MENTION.\n")
# filepath from where you want to delete
source_deleting = input(
    "Enter the filepath of folder you want to delete from: ")
# filetype you want to delete
file_type = input(
    "Filetype of the files you want to delete (including the dot)(like .jpg, etc): ")
n = len(file_type)  # length of file_type1
if os.path.isdir(source_deleting):
    clean(source_deleting)
    print("Cleaning Complete.\n")
else:
    print("Not a Directory.")
