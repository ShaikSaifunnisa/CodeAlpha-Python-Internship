# CodeAlpha Internship - Task 3
# Email Address Extractor

import re

input_file = "sample.txt"
output_file = "extracted_emails.txt"

with open(input_file, "r") as file:
    text = file.read()

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed!")
print("Emails found:")

for email in emails:
    print(email)

print("\nResults saved to extracted_emails.txt")
