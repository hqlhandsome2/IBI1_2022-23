import re
import xml.dom.minidom
import openpyxl
from openpyxl.styles import Font

# Define a function to parse the GO OBO XML file
def parse_go_obo_xml(file_path):
    DOMTree = xml.dom.minidom.parse(file_path)
    term = DOMTree.documentElement
    terms = term.getElementsByTagName("term")
    parent_child_relations = {}

    rows = []

    # Loop through each <term> element to get the GO ID and get all the 'is_a' elements
    for term in terms:
        go_id = term.getElementsByTagName("id")[0].childNodes[0].data
        is_a_elements = term.getElementsByTagName("is_a")

        # Loop through each 'is_a' element to get the ID of the 'is_a' element
        for is_a_element in is_a_elements:
            is_a_id = is_a_element.childNodes[0].data

            # Check if the 'is_a' ID is already in the parent_child_relations dictionary, if not, create an empty list for that ID
            if is_a_id not in parent_child_relations:
                parent_child_relations[is_a_id] = []

            # Append the current GO ID as a child of the 'is_a' ID
            parent_child_relations[is_a_id].append(go_id)

    # Recursive function to count all child nodes, if the GO ID is not present in the parent_child_relations dictionary,there are no child nodes
    def count_child_nodes(go_id, parent_child_relations):
        if go_id not in parent_child_relations:
            return 0

        # Get the list of child nodes for the current GO ID
        child_nodes = parent_child_relations[go_id]
        count = len(child_nodes)

        # Loop through each child node and recursively count its child nodes
        for child_node in child_nodes:
            count += count_child_nodes(child_node, parent_child_relations)
        return count

    # Loop through each <term> element again and get the 'defstr' element and its data
    for term in terms:
        defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data

        # Search for the term 'autophagosome' in the 'defstr', if it is found, get the GO ID and the name of the term, then count the number of child nodes for the current GO ID
        match_autophagosome = re.search('autophagosome', defstr)
        if match_autophagosome:
            go_id = term.getElementsByTagName("id")[0].childNodes[0].data
            name = term.getElementsByTagName("name")[0].childNodes[0].data
            is_a_count = count_child_nodes(go_id, parent_child_relations)

            # Append the data to the rows list
            rows.append([go_id, name, defstr, is_a_count])

            # Print the information
            print("GO_id:", go_id)
            print("Term_Name:", name)
            print("Definition:", defstr)
            print("ChildNodes:", is_a_count)
            print()

    # Create and output a new Excel workbook called "autophagosome_task.xlsx"
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["id", "name", "definition", "childnodes"])

    # Define a bold font style
    bold_font = Font(bold=True)
    for cell in sheet[1]:
        cell.font = bold_font

    # Append the rows to the sheet
    for row in rows:
        sheet.append(row)

    # Save the workbook to a file
    workbook.save("autophagosome_task.xlsx")

# Usage example:
parse_go_obo_xml("go_obo.xml")
