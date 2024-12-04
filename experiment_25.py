def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            raise ValueError("All lists must have the same length when strct is True")
    else:
        min_length = min(len(names), len(ids), len(points))
        return list(zip(names[:min_length], ids[:min_length], points[:min_length]))

names = ["Anil", "BANK", "Chai"]
ids = [101, 102, 103]
points = [1000, 1500, 1200]

print(my_zip(names, ids, points, strct=True))

names_short = ["Alice", "Bob"]
print(my_zip(names_short, ids, points, strct=False))