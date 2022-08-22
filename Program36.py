import re
string = "My name is Haritha sree and my id is 2100030386"
word_list = re.split(r"\s+", string)
print(word_list)