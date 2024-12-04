def my_max(*args):
    max_value = None    
    if len(args) != 1:
        raise ValueError("Only one argument is allowed")
    
    container = args[0]
    if isinstance(container, (list, set, tuple)):
        if len(container) == 0:
            raise ValueError("Container is empty")
        
        max_value = next(iter(container))  
        
        for item in container:
            if item > max_value:
                max_value = item
    else:
        raise ValueError("Input must be a list, set, or tuple")
    
    return max_value
lst = [3, 5, 7, 2, 8]
print("Max value in list:", my_max(lst))
s = {3, 5, 7, 2, 8}
print("Max value in set:", my_max(s))
t = (3, 5, 7, 2, 8)
print("Max value in tuple:", my_max(t))