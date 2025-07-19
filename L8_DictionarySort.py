#Sort a dictionary in ascending and descending order

d = {1: 'hello', 34: 'good morning', 5:'apple', 6: 'car'}

d_ascending_key = dict(sorted(d.items(), key=lambda item: item[0]))
print(f"Ascending wrt keys: {d_ascending_key.items()}")

d_ascending_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(f"Ascending wrt values: {d_ascending_value.items()}")

d_descending_key = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))
print(f"Descending wrt keys: {d_descending_key.items()}")

d_descending_value = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(f"Descending wrt values: {d_descending_value.items()}")