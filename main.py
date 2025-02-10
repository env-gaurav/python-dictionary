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

'''
Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
def keytoDict(n):
    data = {}
    base_value = 10
    for i in range(n+1):
        data[i] = base_value * i + base_value
    print(data)
keytoDict(5)

'''
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for i in (dic1,dic2,dic3):
    dic1.update(i)
print(dic1)

'''
Write a Python script to check whether a given key already exists in a dictionary.
'''
employee= {"emp_id":101, "emp_name":"Rahul", "emp_dept":"HR"}
print(employee.get("emp_id","not exist"))
print(employee.get("emp_salary","not exist"))

'''
Write a Python program to iterate over dictionaries using for loops.
'''
flight= {"IATA":["AI","6E","QP"], "airline":["Air_India","Indigo","Akasa_air"]}
length= len(flight["IATA"])
for i in range(length):
    print(flight["IATA"][i],">-" , flight["airline"][i])