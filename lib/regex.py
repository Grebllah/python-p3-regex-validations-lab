import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][A-z'-]{0,1}[a-z'-]{0,}[\s]{0,1}[A-Z]{0,}[a-z'-]{0,}[A-Z]{0,}[a-z'-]{0,}"
name_regex = re.compile(name)

phone_number = r""
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
