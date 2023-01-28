def distance(strand_a, strand_b):
    count=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for a_piece,b_piece in zip(strand_a,strand_b):
            if not a_piece==b_piece:
                count+=1
    return count
    pass
