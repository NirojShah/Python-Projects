

def remove_same_word(l1,l2):
    
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                rem = l1[i]
                l1.remove(rem)
                l2.remove(rem)

                together = l1+["*"]+l2
                return [together,True]
    
    together = l1+["*"]+l2
    return [together,False]



name_1 = input("Please, Enter your name :- ").lower()
name_2 = input("Please, Enter your name :- ").lower()

l1 = name_1.replace(" ","")
l2 = name_2.replace(" ","")

l1 = list(name_1)
l2 = list(name_2)


proceed = True

while proceed:

    ret_list = remove_same_word(l1,l2)
    con_list = ret_list[0]
    proceed = ret_list[1]

    star_index = con_list.index("*")

    first = con_list[:star_index]
    second = con_list[star_index+1:]


counter = len(first)+len(second)

result = ['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(result) > 1:
    split_index = (counter%len(result)-1)

    if split_index >= 0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = left+right
    else:
        result = result[:len(result)-1]

print(result[0])