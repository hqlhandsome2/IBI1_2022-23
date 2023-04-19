

def dna_sequence_analysis(seq: str):  # Define a function called "dna_sequence_analysis" that takes a single argument called "seq".
    seq = seq.upper()  # Convert the input sequence to uppercase to handle mixed case input.
    start_codon = "ATG"  # Defines the start codon for the DNA sequence.
    stop_codon = "TGA"  # Defines the stop codon for the DNA sequence.
    for i in range(len(seq) - 2):  # Loops through the sequence to find the start and stop codons using nested for loops.
        if seq[i:i + 3] == start_codon:  # If a start codon is found
            final_stop_codon_index = None
            for j in range(i + 3, len(seq) - 2, 3):  # loops through the sequence again to find the final stop codon...
                if seq[j:j + 3] == stop_codon:
                    final_stop_codon_index = j
            if final_stop_codon_index is not None:  # and if a final stop codon is found
                code_len = final_stop_codon_index + 3 - i
                coding_percentage = (code_len / len(seq)) * 100
                print(f"Final stop codon found at position {final_stop_codon_index}")  # ...prints the position of the final stop codon.
            else:
                print("Error: Cannot find stop_codon")  # If no final stop codon is found, prints an error message and returns.
                return 0, 'non-coding'
            break
    else:
        print("Error: Cannot find start_codon")  # If no start codon is found, prints an error message and returns.
        return 0, 'non-coding'
    if coding_percentage > 50:  # Determines if the sequence is protein-coding, non-coding or unclear based on the specified criteria.
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 10:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'

seq = input("input your DNA sequence:")  # Prompts the user to input their DNA sequence.
result = dna_sequence_analysis(seq)  # Calls the "dna_sequence_analysis" function with the input sequence as an argument.
print(f"Coding percentage: {result[0]}%")  # Prints the percentage of coding DNA in the input sequence.
print(f"Sequence type: {result[1]}")  # Prints whether the input sequence is protein-coding, non-coding or unclear.

# sample
seq='atatgctgaacatgctgttagtcgtttttaggctgaggcctatgactgtgagggactacttttgaaag'
#input your DNA sequence:atatgctgaacatgctgttagtcgtttttaggctgaggcctatgactgtgagggactacttttgaaag
#Final stop codon found at position 62
#Coding percentage: 92.64705882352942%
#Sequence type: protein-coding