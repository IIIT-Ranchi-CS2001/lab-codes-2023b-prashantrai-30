import ast

numbers = ast.literal_eval(input("Enter Numbers:"))
sum = sum(numbers)
count = len(numbers)
mean = sum/count

sorted_numbers = sorted(numbers)
mid = count // 2
if count % 2 == 0:
    median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
else:
    median = sorted_numbers[mid]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_frequency = max(frequency.values())
mode = [num for num, freq in frequency.items() if freq == max_frequency]

if len(mode) == len(numbers):
    mode = "No unique mode found"
elif len(mode) == 1:
    mode = mode[0]

print("Numbers:",numbers)
print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)