# Find user id and domain name of imail address

email_add = input("enter the email address of a person:")

aterate = email_add.find('@')
domain_name = email_add[aterate + 1:]
user_id = email_add[:aterate:]

print(f"The domain name of person {domain_name}")
print(f"The user id of person {user_id}")
