def extract_email_body(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    start_extracting = False
    extracted_lines = []

    for line in lines:
        if start_extracting:
            extracted_lines.append(line)
        if "X-FileName:" in line:
            start_extracting = True

    return ''.join(extracted_lines)

# Example
filename = 'maildir/arora-h/all_documents/1.'
print(extract_email_body(filename))
