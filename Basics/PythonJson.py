addressbook={}

addressbook["John"]={
    "Name":"John",
    "Address":"1 Mercer ST,WA",
    "Ph":123456789
}

addressbook["Sam"]={
    "Name":"Sam",
    "Address":"1 Smith ST,WA",
    "Ph":987456123
}

import json

s=json.dumps(addressbook)

print(s)
print(type(s))

with open("E:\\PythonDataScience\\Files\\addressbook.txt","w") as f:
    f.write(s)