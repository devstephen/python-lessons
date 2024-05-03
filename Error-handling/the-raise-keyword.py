def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("Both number must be positive")
        return a + b
    except ValueError as e:
        return f"Exception caught {e}"
    
print(add_positive_numbers(1, 15))
print(add_positive_numbers(1, -3))