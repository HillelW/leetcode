def get_repeated_dna_sequences(dna_sequence: str, sequence_length: int) -> set[str]:
    if not dna_sequence or len(dna_sequence) < sequence_length:
        return []
    
    dna_sequence_length = len(dna_sequence)
    result = set()
    seen_so_far = set()

    left = 0
    right = sequence_length - 1

    while right < dna_sequence_length:
        current_dna_sequence: str = dna_sequence[left: right+1]
        if not current_dna_sequence in seen_so_far:
            seen_so_far.add(current_dna_sequence)
        elif current_dna_sequence in seen_so_far:
            result.add(current_dna_sequence)
    
        left += 1
        right += 1
    return result

assert get_repeated_dna_sequences('AGCTGAAAGCTTAGCTG', 5) == {'AGCTG'}

