import os
from parse_individual_email import extract_email_body
from output_cleaned_email import out_cleaned_email

output_path = 'cleaned_mail'
if not os.path.exists(output_path):
    os.makedirs(output_path)

input_path = 'maildir'

for person in os.listdir(input_path):
    # Layer one: person
    person_path = os.path.join(input_path, person)
    if not os.path.isdir(person_path):
        continue

    person_output_path = os.path.join(output_path, person)
    if not os.path.exists(person_output_path):
        os.makedirs(person_output_path)

    for folder in os.listdir(person_path):
        # Layer two: person's folders
        person_folder_path = os.path.join(person_path, folder)
        if not os.path.isdir(person_folder_path):
            continue
        person_folder_output_path = os.path.join(person_output_path, folder)
        if not os.path.exists(person_folder_output_path):
            os.makedirs(person_folder_output_path)

        for email in os.listdir(person_folder_path):
            # Layer three: each email. Clean and store.
            email_path = os.path.join(person_folder_path, email)
            if not os.path.isdir(email_path):
                email_output_path = os.path.join(person_folder_output_path, email)
                content = extract_email_body(email_path)
                out_cleaned_email(email_output_path, content=content)
            else: 
                # Layer four:
                for email_email in os.listdir(email_path):
                    content = extract_email_body(os.path.join(email_path, email_email))
                    out_cleaned_email(os.path.join(email_path, email_email), content=content)





        
    # if os.path.isdir(full_path):
    #     print(full_path)
