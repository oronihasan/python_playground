import re

# pattern = re.compile ( "[a-z A-Z/s 0-9]+" ) everething

pattern = re.compile ( "^[a-z]{3}[0-9]{3}$" )

print(pattern.search("rty456"))

print(pattern.search("HELLO WORLD"))

print(pattern.search("HELLOWORLD"))