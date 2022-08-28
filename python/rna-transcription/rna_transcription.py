def to_rna(dna_strand):
    # nucleotidio correspondente do DNA para o RNA
    dna_transcription = {
        "A" : "U",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }

    return ''.join(dna_transcription[item] for item in dna_strand) # faz a transcrição do DNA para RNA usando o dict