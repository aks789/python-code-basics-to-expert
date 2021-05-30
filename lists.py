friends = ["Akriti", "Akshay", "Shivani"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[1:])
print(friends[1:2])
friends[1] = "Mike"
print(friends)

luck_numbers = [4, 8, 16, 23, 42]

friends = ["akriti","akshay"]
friends.extend(luck_numbers)
friends.append("creep")
friends.insert(1,"wainan do")
friends.remove("creep")
#friends.clear()
friends.pop();
friends.index("akriti")
print(friends)

my_list=['STRING',1,1.2]

my_list2 = my_list*3
print(my_list2)

print(len(my_list))
print(my_list[0])
print(my_list[1:])

another_list = ['4','5'];

new_list=my_list+another_list;

print(new_list);

## Lists are mutable
new_list[0]='Akshay';

print(new_list);

new_list.append(6);

print(new_list);

new_list.pop();

print(new_list);

new_list.pop(-1);

print(new_list);

new_list=['a','e','b'];

num_list = [3,2,1];

## Does not return anything to assign
new_list.sort();

new_list1 = sorted(new_list);

print(new_list1);

print(type(new_list.sort()));

print(new_list);

num_list.sort();

print(num_list);

num_list.reverse();

print(num_list);

num_list=[1,[1,2]];
print(num_list[1][1]);

a = 1 < 2  and 2 < 3

print(not(a))