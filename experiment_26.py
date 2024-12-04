def my_sort(data, key):
    n = len(data)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if key == 0:
                if data[j][0] > data[j+1][0]:
                    data[j], data[j+1] = data[j+1], data[j]
            elif key == 1:
                if data[j][1] > data[j+1][1]:
                    data[j], data[j+1] = data[j+1], data[j]
            elif key == 2:
                if data[j][2] > data[j+1][2]:
                    data[j], data[j+1] = data[j+1], data[j]
    
    return data

names = ["Anil", "Bank", "Chai"]
ids = [103, 102, 101]
points = [1000, 1500, 1200]

zipped_data = my_zip(names, ids, points, strct=True)

sorted_by_name = my_sort(zipped_data, 0)
print("Sorted by Name:", sorted_by_name)

sorted_by_id = my_sort(zipped_data, 1)
print("Sorted by ID:", sorted_by_id)

sorted_by_points = my_sort(zipped_data, 2)
print("Sorted by Points:", sorted_by_points)