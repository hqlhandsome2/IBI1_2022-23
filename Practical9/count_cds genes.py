
stop_codons = input("Input the stop codons: ") # Take input for stop codons from the user
terminator = ["TAA", "TAG", "TGA"] # Initialize a list to limit the choices of terminator codons
if stop_codons not in terminator: # Check if the input stop codon is in the list of terminator codons
    print("Error: Invalid stop codon") # If not, print an error message
else:
    gene_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa" # Set the gene file name
    output_file = f"{stop_codons}_stop_genes.fa" # Set the output file name with the input stop_condons

    with open(gene_file, "r") as input_handle, open(output_file, "w") as output_handle: # Open the gene file for reading and output file for writing
        seq = "" # Initialize an empty sequence
        gene_id = "" # Initialize an empty gene ID
        for line in input_handle: # Loop through each line in the gene file
            if line.startswith(">"): # If the line starts with ">"
                if seq.endswith(stop_codons): # Check if the sequence ends with the stop codon
                    count = seq.count(stop_codons) # count the number of coding sequences
                    output_handle.write(f'>{gene_id}'+"，"+f'{count}\n{seq}\n') # If it does, write the gene ID,the number of coding sequences and sequence to the output file
                gene_id = line.split(">")[1].rsplit(" ")[0] # Update the gene ID
                seq = "" # Reset the sequence
            else:
                seq += line.strip() # Add the line to the sequence and remove the whitespace
        if seq.endswith(stop_codons): # After looping through all lines, check if the last sequence ends with the stop codon
            output_handle.write(f">{gene_id}\n{seq}\n") # If it does, write the gene ID and sequence to the output file