'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''

import streamlit as st
import packaging

st.title("Process One Package")

# Input field for package data
package_data = st.text_input("Enter package data:")

if st.button("Submit"):
    if package_data:
        # Parse the package data
        parsed_package = packaging.parse_packaging(package_data)
        
        # Display the package information
        st.subheader("Package Information")
        st.text(parsed_package)
        for item in parsed_package:
            name = list(item.keys())[0]
            size = list(item.values())[0]
            st.info(f"{name} 🟰 {size}")

        # Calculate and display the total package size
        total_size = packaging.calc_total_units(parsed_package)
        unit = packaging.get_unit(parsed_package)
        st.subheader("Total 📦 Size")
        st.write(f"{total_size} {unit}")
    else:
        st.error("Please enter package data.")