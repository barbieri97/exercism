""" solution to protein-translation exercise """

aminoacids= {
'Methionine': ('AUG'),
'Phenylalanine': ('UUU', 'UUC'),
'Leucine': ('UUA', 'UUG'),
'Serine': ('UCU', 'UCC', 'UCA', 'UCG'),
'Tyrosine': ('UAU', 'UAC'),
'Cysteine': ('UGU', 'UGC'),
'Tryptophan': ('UGG'),
'STOP': ('UAA', 'UAG', 'UGA')
}
def proteins(strand):
    """ translate a RNA to their proteins  """
    codons = []
    start, end = 0, 3
    for _ in range(len(strand)//3):
        codon = get_protein(strand[start:end])
        if codon == 'STOP':
            return codons
        codons.append(codon)
        start += 3
        end += 3
    return codons

def get_protein(codon):
    """ given a codon return their aminoacid """
    for item in aminoacids.items():
        if codon in item[1]:
            return item[0]
    return None
