#tuple - collection of items
my_tuple=(1,4,9,16,25)
#my_tuple[3]=64

#tuple are immutable in nature
#in tuple object assignment is not possible

my_shopping_list=['bread','butter','jam','milk']
my_shopping_list[2]="panneer"
print(my_shopping_list)

# Tuple is used when item list are fixed and not
my_api_list=list(my_shopping_list)
print(my_api_list)

my_api_list_rev=tuple(my_shopping_list)
print(my_api_list_rev)