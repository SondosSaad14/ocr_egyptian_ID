import os
import tempfile
from PIL import Image
import streamlit as st
from main import detect_and_process_id_card

# Streamlit page configuration (global colors and layout)
st.set_page_config(
    page_title="ID Egyptian Card",
    page_icon="💳",
    layout="wide",  # Set to "centered" or "wide" layout
    initial_sidebar_state="expanded",  # "collapsed", "expanded"
)

# Customize the app's UI colors
st.markdown("""
    <style>
        .stApp {
            background-color:rgb(0, 0, 0);
        }

        .stSidebar {
            background-color:rgb(6, 7, 7);
            color:rgb(247, 250, 252);
        }

        .stButton>button {
            background-color:rgb(137, 10, 10);
            color: white;
        }

        .stButton>button:hover {
            background-color: rgb(137, 10, 10);
        }

        h1, h2, h3 {
            color: rgb(246, 237, 237);
        }

        .stTextInput>div>div>input {
            color:rgb(6, 6, 6);
            background-color: rgb(255, 255, 255);
        }

        .stMarkdown {
            color: rgb(255, 255, 255);
        }

        .stFileUploader {
            color: rgb(137, 10, 10);
        }
    </style>
""", unsafe_allow_html=True)


# Initialize session state for navigation
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "Home"

# Sidebar navigation menu with a different color scheme
tabs = ["Home", "Help"]
selected_tab = st.sidebar.selectbox("Choose a Section", tabs)

# Update the session state with the selected tab
st.session_state.current_tab = selected_tab

# Home Tab
if st.session_state.current_tab == "Home":
    uploaded_file = st.sidebar.file_uploader("Upload an ID card image",
                                             type=['webp', 'jpg', 'tif', 'tiff', 'png', 'mpo', 'bmp', 'jpeg', 'dng', 'pfm'])

    # If no file is uploaded, display the HOME image
    if not uploaded_file:
        image = Image.open("TXT.jpg")
        resized_image = image.resize((5760, 3240))
        st.image(image, use_container_width=True)

    else:
        # Process the uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        image = Image.open(temp_file_path)

        st.subheader('Egyptian ID Card EXTRACTING, OCR 💳')
        st.sidebar.image(image)
        
        # Layout using columns for a cleaner structure
        col1, col2 = st.columns([1, 2])
        try:
            first_name, second_name, Full_name, national_id, address, birth, gov, gender = detect_and_process_id_card(temp_file_path)

            with col1:
                st.subheader('Egyptian ID Card Extractor 💳')
                st.image(Image.open("d2.jpg"), use_container_width=True)

            with col2:
                st.markdown("### Results from the Egyptian ID Card 💳")

                st.markdown(" ## WORDS EXTRACTED : ")
                st.write(f"**First Name**: {first_name}")
                st.write(f"**Second Name**: {second_name}")
                st.write(f"**Full Name**: {Full_name}")
                st.write(f"**National ID**: {national_id}")
                st.write(f"**Address**: {address}")
                st.write(f"**Birth Date**: {birth}")
                st.write(f"**Governorate**: {gov}")
                st.write(f"**Gender**: {gender}")
        except Exception as e:
                st.error(f"An error occurred: {e}")
        finally:
                os.remove(temp_file_path)

# Guide Tab
elif st.session_state.current_tab == "Help":
    st.title("How to Use the Egyptian ID Card OCR Application 📖")

    st.markdown("""
    ## Project Overview:
    This application processes Egyptian ID cards to extract key information, including names, addresses, and national IDs. It also decodes the national ID to provide additional details like birth date, governorate, and gender.
    
    ## Features:
    - **ID Card Detection**: Automatically detects and crops the ID card from the image.
    - **Field Detection**: Identifies key fields such as first name, last name, address, and serial number.
    - **Text Extraction**: Extracts Arabic and English text using EasyOCR.
    - **National ID Decoding**: Decodes the ID to extract birth date, governorate, gender, and nationality.
    
    ## How It Works:
    1. **Upload an Image**: Upload an image of the ID card using the sidebar.
    2. **Detection and Extraction**: YOLO models detect the ID card and its fields. EasyOCR extracts text from the identified fields.
    3. **Result Presentation**: Outputs extracted information such as full name, address, and national ID details.
    4. **ID Decoding**: Decodes the national ID to reveal demographic details.
    
    ## Steps to Use:
    - Get your image ready.
    - Click on Home.
    - Upload an Egyptian ID card image.
    - View the extracted information and analysis.
    """ )

    st.markdown("""
    ## Acknowledgments

    - [YOLO]      (https://github.com/ultralytics/yolov5) for object detection.
    - [EasyOCR]   (https://github.com/JaidedAI/EasyOCR) for optical character recognition.
    - [Streamlit] (https://streamlit.io/) for the web interface.
                
""")

with st.spinner('Processing the ID card...'):
    first_name, second_name, Full_name, national_id, address, birth, gov, gender = detect_and_process_id_card(temp_file_path)
st.success('Processing complete!')

st.download_button(
    label="Download Extracted Data",
    data="extracted_data.csv",
    file_name="extracted_data.csv",
    mime="text/csv"
)
