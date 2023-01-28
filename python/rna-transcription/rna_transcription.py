def to_rna(dna_strand):
    dna_to_rna={'G':'C','C':'G','T':'A','A':'U',' ':''}
    rna=""
    for nucleotide in dna_strand:
        rna+=(dna_to_rna[(nucleotide)])
    return rna
    pass