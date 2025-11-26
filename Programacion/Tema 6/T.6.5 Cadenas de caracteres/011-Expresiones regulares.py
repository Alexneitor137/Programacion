import re

patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email_mal = "algo"
email_bien = "alex@gmail.com"

print(re.match(patron, email_mal))

print(re.match(patron, email_bien))
