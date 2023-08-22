from pdfc.pdf_compressor import compress
import streamlit as st
import tempfile
import os
import warnings

def main():
    st.title("Aplikasi Pengompress PDF")
    st.subheader("Upload the PDF File")

    #create temporary directory
    uploaded_file = st.file_uploader("Choose a PDF File", type=["pdf"])

    if uploaded_file is not None:
        temp_dir = tempfile.TemporaryDirectory()
        input_path = os.path.join(temp_dir.name, uploaded_file.name)
        output_path = os.path.join(temp_dir.name, "compressed.pdf")

        #save uploaded file to temporary directory
        with open(input_path, "wb") as file:
            file.write(uploaded_file.getvalue())

        st.subheader("Compression Level")
        comp_level = st.radio(
            "Select the compression level",
            ('0 : Default',
             '1 : Prepress (high quality, color preserving, 300 dpi images)',
             '2 : printer (high quality, 300 dpi images)',
             '3 : ebook (low quality, 150 dpi images)',
             '4 : screen (screen view only quality, 72 dpi images)')
        )

        if comp_level =='0 : Default':
            fullpower = 0
        elif comp_level == '1 : Prepress (high quality, color preserving, 300 dpi images)':
            fullpower = 1
        elif comp_level == '2 : printer (high quality, 300 dpi images)':
            fullpower = 2
        elif comp_level == '3 : ebook (low quality, 150 dpi images)':
            fullpower = 3
        elif comp_level == '4 : screen (screen view only quality, 72 dpi images)':
            fullpower = 4

        if st.button("Compress"):
            compress(input_path, output_path, power=fullpower)

            compressed_file = open(output_path, "rb").read()
            st.download_button("Download Compressed PDF", compressed_file, file_name="compressed.pdf")

# compress('test.pdf', 'test_comp.pdf', power=4)

if __name__ == "__main__":
    main()
