import re

result=dir(re)


#Regular Expression
str= "Python kursu: Python Programlama Rehberiniz | 40 saat"
"""
[] arasındaki herşey aranır. 
"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)

result = re.findall("...",str)
result = re.findall("Py..on",str)

result=re.findall("^P",str)

result=re.findall("t$",str)

result = re.findall("sa*t",str)
result = re.findall("sa+t",str)
result = re.findall("sa?t",str)

result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)

result = re.findall("\APython",str)
result = re.findall("saat\Z",str)

#re modülü


#re.findall()

# result = re.findall("Python",str)
# result = len(result)

#re.split()
# result = re.split(" ",str)
# result = re.split("r",str)

#re.sub()

# result=re.sub(" ","-",str)

#re.search()

# result = re.search("Python",str)
# result = result.span()
# result = result.end()
# result = result.group()
# result = result.string
print(result)