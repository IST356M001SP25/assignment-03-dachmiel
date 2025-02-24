'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''


import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit
from io import StringIO
import json

st.title("Process Package Files")

# Initialize session state variables
if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'file_count' not in st.session_state:
    st.session_state.file_count = 0
if 'line_count' not in st.session_state:
    st.session_state.line_count = 0

# File uploader for packaging information
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file:
    # Read the file content
    binary_contents = uploaded_file.getvalue()
    file_content = StringIO(binary_contents.decode("utf-8")).read()
    
    packages = []
    line_count = 0
    # Split the file content into individual package data entries    
    for line in file_content.split('\n'):
        line = line.strip()
        # Parse the package data
        if line:
            # Parse the package data
            parsed_package = parse_packaging(line)
            total_units = calc_total_units(parsed_package)
            unit = get_unit(parsed_package)
            packages.append(parsed_package)
            line_count += 1

    count = len(packages)
    filename = uploaded_file.name
    json_filename = filename.replace(".txt",".json")

    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)

    summary = f"📝 {count} packages written to {json_filename}"
    # Update session state
    st.session_state.summaries.append(summary)
    st.session_state.file_count += 1
    st.session_state.line_count += line_count

    for s in st.session_state.summaries:
        st.info(s)
    st.success(f"Processed {st.session_state.file_count} files and {st.session_state.line_count} lines in total.")
else:
    st.info("Please upload a file containing packaging information.")

            