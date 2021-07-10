#Take a user input as the email variable name
email = input("Enter Your Email: ").strip()
#Segregate the data into two parts one as username and other as  domain
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
#get this printed in slices form
print(f"Your username is {username} & domain is {domain}")
