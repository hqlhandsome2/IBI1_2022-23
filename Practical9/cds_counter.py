# Define the DNA sequence, promoter and terminator codons
seq = "ATGCAATCGACTACGATCTGAGAGGCCTAA"
promoter = "ATG"
terminator = ["TAA", "TAG", "TGA"]

# Initialize an empty list to store the positions of stop codons
stop = []

# Iterate through the sequence in steps of 1
for i in range(len(seq)-2):
    codon = seq[i:i+3]
    # Check if the current codon is equal to the promoter
    if codon == promoter:
        # If it is, iterate through the rest of the sequence in steps of 3
        for j in range(i+3, len(seq)-2, 3):
            stop_codon = seq[j:j+3]
            # Check if the current codon is a stop codon
            if stop_codon in terminator:
                # If it is, add its position to the list of stop codons
                stop.append(j)
# Count the number of stop codons found
count = len(stop)
# Print the count
print(count)
