def out_cleaned_email(fileName, content):
    with open(fileName, 'w') as file:
        file.write(content)


# out_cleaned_email("testfile.txt", "blablablab")