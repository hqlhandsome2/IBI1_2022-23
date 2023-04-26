
# Open the three files
human = open("ACE2_human.fa", "r")
mouse = open("ACE2_mouse.fa", "r")
cat = open("ACE2_cat.fa", "r")

# Initialize sequence lists
human_seq=[]
mouse_seq=[]
cat_seq=[]

# Initialize sequence strings
human_sequence = ''
mouse_sequence = ''
cat_sequence = ''

# Read the human sequence
for line in human:
    if not line.startswith(">"):
        human_sequence += line.strip()
# Read the mouse sequence
for line in mouse:
    if not line.startswith(">"):
        mouse_sequence += line.strip()
# Read the cat sequence
for line in cat:
    if not line.startswith(">"):
        cat_sequence += line.strip()

# Initialize edit distances
edit_distance12=0 # 12 means human and mouse
edit_distance13=0 # 13 means human and cats
edit_distance23=0 # 23 means mouse and cats

# Calculate edit distances
for i in range(len(human_sequence)):
    if human_sequence[i]==mouse_sequence[i]: # Compare each amino acid between human and mouse
        edit_distance12 += 1                 # Add a score 1 if amino acid are the same
    if human_sequence[i]==cat_sequence[i]:
        edit_distance13 += 1
    if mouse_sequence[i]==cat_sequence[i]:
        edit_distance23 += 1

# Calculate percentages of similarity
human_mouse_percentage=edit_distance12*100/len(human_sequence)
human_random_percentage=edit_distance13*100/len(human_sequence)
mouse_random_percentage=edit_distance23*100/len(human_sequence)


# Initialize alignment scores
score12=0
score13=0
score23=0

# Open the BLOSUM62 matrix file
with open('blosum62.txt', 'r') as file: # get from https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
    data = file.read()
    lines = data.strip().split('\n') # Split the data into lines
    header = lines[0].split() # Get the header row
    matrix = {} # Initialize the matrix dictionary
    for row in lines[1:]:  # Iterate over each row
        items = row.split() # Split the row into items
        key = items[0] # Get the key
        values = [int(x) for x in items[1:]] # Get the values and convert them to integers
        matrix[key] = dict(zip(header, values))  # Store the key and values in the matrix dictionary

# Iterate over each position in the sequences
for i in range(len(human_sequence)):
    # Get the characters at the current position
    x=human_sequence[i]
    y=mouse_sequence[i]
    z=cat_sequence[i]
    # Look up the substitution scores in the BLOSUM62 matrix
    score12 += int(matrix[x][y])
    score13 += int(matrix[x][z])
    score23 += int(matrix[y][z])


# Print results
print("Human amino acid sequence:",human_sequence)
print("Mouse amino acid sequence:",mouse_sequence)
print("Random amino acid sequence:",cat_sequence)
print("The blosum score between human and mouse is",score12)  # 3579
print("The blosum score between human and cat is",score13)    # 3717
print("The blosum score between mouse and cat is",score23)    # 3592
print("The percentage of identical amino acids between human and mouse:",human_mouse_percentage,"%") # 82.11180124223603 %
print("The percentage of identical amino acids between human and cat:",human_random_percentage,"%")  # 85.21739130434783 %
print("The percentage of identical amino acids between mouse and cat:",mouse_random_percentage,"%") # 81.73913043478261 %

