d = {"one": "madhu one", 2: " Twoooo", "three" :  3}
d1 = {} ## empty dict

for key in d:
    print(key, ":", d[key])


print(d["one"])
d[2] = "Two"
print(d[2])

del d["one"]
print(d)
print(len(d))

print("one" not in d)

print(d.keys())
print(d.values())
print(d)
d.popitem()
print(d)

c = {1: "madhuu", 2: "meeeee", "one": "twojjbjhbhh"}
print(c.get("one"))
c.pop("one")
print(c)

c = {1: "madhuu", 2: "meeeee", "one": "twojjbjhbhh"}
for key in c:
    print(key, c[key])