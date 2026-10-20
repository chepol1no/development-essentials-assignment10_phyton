
items = ["Python", 42, 3.14, True, "GitHub", None, 100, "Data"]
string_count = 0

for item in items:
    if isinstance(item, str):
        string_count += 1

print(f"Number of string elements: {string_count}")
