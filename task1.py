n = int(input("Enter number of keys: "))

dummy_dict = {}
for i in range(1, n + 1):
    dummy_dict[f"key{i}"] = f"value{i}"

print("Generated Dictionary:")
print(dummy_dict)
