'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''

import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit
from io import StringIO
import json

st.title("Process Packaging File")

# File uploader for packaging information
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file:
    # Read the file content
    binary_contents = uploaded_file.getvalue()
    file_content = StringIO(binary_contents.decode("utf-8")).read()
    
    packages = []
    # Split the file content into individual package data entries    
    for line in file_content.split('\n'):
        line = line.strip()
        # Parse the package data
        parsed_package = parse_packaging(line)
        total_units = calc_total_units(parsed_package)
        unit = get_unit(parsed_package)
        packages.append(parsed_package)
        st.info(f"{line} 🟰 total units: {total_units} {unit}")

    count = len(packages)
    filename = uploaded_file.name
    json_filename = filename.replace(".txt",".json")

    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    st.success(f"📝 {count} packages written to {json_filename}")
else:
    st.info("Please upload a file containing packaging information.")

            