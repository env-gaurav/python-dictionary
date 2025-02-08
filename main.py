students = {"Gaurav":90,"Rahul":80,"Palak":80,"Ajay":70,"John":90}
print(students["John"])
students["bhim"]=80
print(students)
students["Rahul"]=70
for value in students.values():
    print(value+2)
print(students)
students.pop("Ajay")
del(students["John"])
del students["Palak"]
print(students)
print(students.get("Gaurav","Not found"))
print(students.get("aman","not found"))
for key in students:
    print(key)
for value in students.values():
    print(value)
for item in students.items():
    print(item)
print("keys: ", students.keys())
print("values", students.values())
print("items", students.items())
squares={"1":1, "2":4, "3":9, "4":16
,"5":25,"6":36,"7":49,"8":64,"9":81,"10":100}
print(squares)
def square(num):
    return num**2
    
nums={}
for i in range(1,11):
    nums[i]=i**2
print(nums)
