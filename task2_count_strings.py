def count_strings(elements):
    count = 0

    for element in elements:
        if isinstance(element, str):
            count += 1

    return count


items = ["Python", 42, 3.14, True, "GitHub", None, 100, "Data"]

string_count = count_strings(items)

print(f"Number of string elements: {string_count}")
