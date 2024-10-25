import streamlit as st

# Function to load the HTML file
def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Streamlit app title
st.title('Sentence Rewriting')

# Load the HTML content from the relative file path
html_content = load_html_file('Model Essay.html')

# Display the HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
