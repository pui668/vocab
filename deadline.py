import streamlit as st

def load_html_file(file_path):
    with open("C:\Users\puipu\Downloads\MyFlow\deadlist.html", 'r', encoding='utf-8') as file:
        return file.read()

st.title('死期到了')

html_content = load_html_file('deadlist.html')

st.components.v1.html(html_content, height=600, scrolling=True)
