import re
# pattern = r"[a-z]+"
# print(re.match(pattern,"qabc123ABCabcd"))

# print(re.findall(pattern,"qabc123ABCabcd"))

# print(re.search(pattern,"qabc123ABCabcd"))

# pattern2 = r"[0-9]+"

email_patt = r"^[a-z]+.?[a-z]*[0-9]*.?[a-z]*@[a-z]+.[a-z]+"

text = """I am eshikhon, My ID is 15067. I love python. my phone number is 017233

aUc893939

abdul.2019.mia@gmail.com

asm@gmail.com

eshikhon.python@yahoo.com

2129.nasim@yahoo.com"""
valid_email = []

lines = text.split("\n")
for line in lines:
    if len(re.findall(email_patt,line)) != 0:
        valid_email+=re.findall(email_patt,line)

print(valid_email)

