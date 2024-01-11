import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][A-z'-]{0,1}[a-z'-]{0,}[\s]{0,1}[A-Z]{0,}[a-z'-]{0,}[A-Z]{0,}[a-z'-]{0,}"
name_regex = re.compile(name)

phone_number = r"[(]{0,1}[0-9]{3}[)]{0,1}[\s-]{0,1}[0-9]{3}[-]{0,1}[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z]{1,}[\w\.]{0,}@[\w]{0,}\.com"
email_regex = re.compile(email_address)
