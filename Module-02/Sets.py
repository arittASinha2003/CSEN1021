L = [2]
t = (3, )
s = {2}  #Empty will show 'dict'
print(type(L))
print(type(t))
print(type(s))

s = {20, 30, 15, 20}  #Set is immutable
print(s)

#Remove Duplicates from a List
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
#print(list(set(duplicate)))