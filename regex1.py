import re
s = " my number is 121 3455556 123"
match = re.search(r'\d\d\d', s)
print("Match is:",match)
print("Group is:", match.group())