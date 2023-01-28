def find(search_list, value):
    sorted_list=sorted(search_list)
    try:
        return binary(0,len(search_list)-1,sorted_list,value)
    except:
        raise ValueError("value not in array")
    
def binary(start,end,sorted_list,value):
    mid=(end-start)//2+start
    if sorted_list[mid]==value:
        return mid 
    if not start<end:
         raise ValueError("value not in array")
    return binary(mid+1,end,sorted_list,value) if sorted_list[mid]<value else binary(start,mid-1,sorted_list,value)