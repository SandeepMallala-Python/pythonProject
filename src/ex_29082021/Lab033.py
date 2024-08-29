my_list=["sandeep","akki","shanmukh","sravani"]
print (my_list[0])
print (my_list[1])
print (my_list[2])
print (my_list[3])
print("--------------------------------------")
for i in (my_list):
    print(i)
#append
my_list.append("shannu")
my_list.append("bannu")

print("-----")
print(my_list)

#extend
my_list.extend([7,8,9,"johnny"])
print("-----")
print(my_list)

#insert - insert objects before any object
my_list.insert(1,"Python")
print("-----")
print(my_list)

# if we want to replace we need to resasign
my_list[1]="pycharm"
print("-----")
print(my_list)

# if we want insert in reverse direction
# positive and negative direction
my_list.insert(-2,"reversescenario")
print("-----")
print(my_list)

# remove
my_list.remove("reversescenario")
print("-----")
print(my_list)

#copying list
my_copy_list=my_list.copy()
print("-----")
print(my_copy_list)

my_list.clear()
print("-----")
print(my_list)
print(my_copy_list)

#my_copy_list.sort()  # to sort same datatype
my_copy_list.reverse()
print(my_copy_list)

