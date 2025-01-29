info = {
  "name":"Bayajid",
  "age": 15,
  "Country":"Nigeria",
  "Hobbies":["Reading","Gardening"],
  "Friends":["John","Jane"]
}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))

new_info = {
  "full_name":"Bayajid Alam Joyel"
}

info.update(new_info)
print(info)