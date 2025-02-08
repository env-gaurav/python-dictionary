# python-dictionary

## Dictionary Practice Questions with Solutions

### 1. Create a dictionary with the names of five students and their marks. Retrieve the marks of a student named "John".
```python
students = {"Gaurav": 90, "Rahul": 80, "Palak": 80, "Ajay": 70, "John": 90}
print(students["John"])  # Output: 90
```

### 2. Add a new student to the dictionary with their marks.
```python
students["bhim"] = 80
print(students)  
# Output: {'Gaurav': 90, 'Rahul': 80, 'Palak': 80, 'Ajay': 70, 'John': 90, 'bhim': 80}
```

### 3. Update the marks of an existing student.
```python
students["Rahul"] = 70
print(students)
# Output: {'Gaurav': 90, 'Rahul': 70, 'Palak': 80, 'Ajay': 70, 'John': 90, 'bhim': 80}
```

### 4. Remove a student from the dictionary.
```python
students.pop("Ajay")
del students["John"]
del students["Palak"]
print(students)
# Output: {'Gaurav': 90, 'Rahul': 70, 'bhim': 80}
```

### 5. Check if a key (student name) exists in the dictionary.
```python
print(students.get("Gaurav", "Not found"))  # Output: 90
print(students.get("Aman", "Not found"))   # Output: Not found
```

### 6. Get all the keys, values, and items from the dictionary.
```python
for key in students:
    print(key)
    
for value in students.values():
    print(value)
    
for item in students.items():
    print(item)

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())
```
#### Output:
```
Gaurav
Rahul
bhim
90
70
80
('Gaurav', 90)
('Rahul', 70)
('bhim', 80)
Keys: dict_keys(['Gaurav', 'Rahul', 'bhim'])
Values: dict_values([90, 70, 80])
Items: dict_items([('Gaurav', 90), ('Rahul', 70), ('bhim', 80)])
```

### 7. Create a dictionary with numbers as keys and their squares as values for numbers 1 to 10.
```python
nums = {}
for i in range(1, 11):
    nums[i] = i ** 2
print(nums)
```
#### Output:
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

