
# Define the input and output file names
gene_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "TGA_genes.fa"

# Open the input and output files
with open(gene_file, "r") as input_handle, open(output_file, "w") as output_handle:
    # Initialize variables to store the current gene name and sequence
    seq = ""
    gene_name = ""

    # Iterate through each line in the input file
    for line in input_handle:
        # If the line starts with ">", it is a header line
        if line.startswith(">"):
            # Check if the current sequence ends with "TGA"
            if seq.endswith("TGA"):
                # If it does, write the gene name and sequence to the output file
                output_handle.write(f">{gene_name}\n{seq}\n")
            # Update the gene name variable with the new gene name from the header line
            gene_name = line.split()[0][1:]
            # Reset the sequence variable to an empty string
            seq = ""
        else:
            #  If the line does not start with ">", it is a sequence line，add the sequence to the current sequence variable
            seq += line.strip()
    # After iterating through all lines, check if the last sequence ends with "TGA"
    if seq.endswith("TGA"):
        # If it does, write the gene name and sequence to the output file,close the input and output files (automatically done by the "with" statement)
        output_handle.write(f">{gene_name}\n{seq}\n")
