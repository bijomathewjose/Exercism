def equilateral(sides):
    return not (degenerate(sides) or zero_side(sides))and sides[0]==sides[1]==sides[2]
    
def isosceles(sides):
    return not(degenerate(sides) or zero_side(sides))and (equilateral(sides) or (sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]))
    
def scalene(sides):
    return not (degenerate(sides) or zero_side(sides) or equilateral(sides) or isosceles(sides))
    
def zero_side(sides):
    return sides[0]==0 or sides[1]==0 or sides[2]==0

def degenerate(sides):
    return not (sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and  sides[2]+sides[0]>sides[1])


#Alternate method without ternary operator

# def equilateral(sides):
#     if not (degenerate(sides) or zero_side(sides))and sides[0]==sides[1]==sides[2]:
#         return True
#     return False
    
# def isosceles(sides):
#     if not(degenerate(sides) or zero_side(sides))and (equilateral(sides) or (sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2])):
#             return True
#     return False

# def scalene(sides):
#     if not (degenerate(sides) or zero_side(sides) or equilateral(sides) or isosceles(sides)):
#         return True
#     return False

# def zero_side(sides):
#     if sides[0]==0 or sides[1]==0 or sides[2]==0:
#         return True
#     return False

# def degenerate(sides):
#     if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and  sides[2]+sides[0]>sides[1]:
#         return False
#     return True