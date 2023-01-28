def append(list1, list2):
    return [*list1,*list2]
    pass

def concat(lists):
    return [element for list in lists for element in list]
    pass

def filter(function, list):
    return [item for item in list if function(item)]
    pass

def length(list):
    count=0
    for i in list:
        count+=1
    return count
    pass

def map(function, list):
    return [function(item) for item in list]
    pass

def foldl(function, list, initial):
    accumulator=initial
    for item in list:
        accumulator=function(accumulator,item)
    return accumulator
    pass

def foldr(function, list, initial):
    accumulator=initial
    while list:
        item=list.pop()
        accumulator=function(item,accumulator)
    return accumulator
    pass

def reverse(list):
    new_list=[]
    while list:
        item=list.pop()
        new_list=append(new_list,[item])
    return new_list
    pass
