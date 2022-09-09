import re


password = "11231qweqry"
password = re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password)
if password:
    pass

email = "11231qweqry"
email = re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", string=email)
if email:
    pass

