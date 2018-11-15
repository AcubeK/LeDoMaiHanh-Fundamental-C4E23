def get_even_list(l):
    lst = []
    for x in l:
        if x%2 ==0:
            lst.append(x)
    return lst

l_even = get_even_list([1, 4, 5, -1, 10])
print (l_even)

#tester
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")