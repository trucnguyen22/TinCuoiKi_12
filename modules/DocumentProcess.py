import numpy as np
from streamlit_elements import *
import streamlit as st
from PIL import Image
from io import BytesIO
import cv2
# =========================
from modules.GoogleForm import GoogleFormGenerator
from modules.modules import Custom_Code
from streamlit_image_comparison import image_comparison
IMAGE_TO_URL = {
    "sample_image_1": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",
    "sample_image_2": "https://user-images.githubusercontent.com/34196005/143309867-42841f5a-9181-4d22-b570-65f90f2da231.jpg",
}


class DocumentProcess:
    class Model:
        subheader_1 = "Select"
        subheader_2 = "Tải lên"

        upload_help = "Tải file .docx"
        upload_button_text = "Tải lên"
        upload_button_text_desc = "Choose a file"

        def set_file_path(self, file_path):
            st.session_state['file_path'] = file_path

        def get_file_path(self):
            if 'file_path' not in st.session_state:
                return None
            return st.session_state['file_path']

    def __init__(self) -> None:
        pass

    def viewDocumentation(self, model, sidebar):
        placeholder_show = st.empty()

        with sidebar:
            st.subheader(model.subheader_1)
            warning_name_group = st.empty()
        with st.form("upload-form", clear_on_submit=True):
            # Image input
            col1, col2 = st.columns([3, 2])
            with col1:
                img2_url = st.text_input(
                    "Image Noisy URL:", value=IMAGE_TO_URL["sample_image_1"])
            with col2:
                uploaded_file = st.file_uploader(model.upload_button_text_desc,
                                                 #  accept_multiple_files=True,
                                                 type=['jpg', 'jpeg', 'png'],
                                                 help=model.upload_help,
                                                 key="uploaded_file"
                                                 )
            col1, col2, col3 = st.columns([6, 4, 6])
            with col2:
                submitted = st.form_submit_button(
                    model.upload_button_text, use_container_width=True)
            col1, col2, col3 = st.columns([6, 4, 6])
            with col2:
                reset = st.form_submit_button(
                    "Reset", use_container_width=True)

            if reset:
                st.session_state.pop('file_path', None)
                pass

            if submitted and uploaded_file is not None:
                self.upload_file(model, uploaded_file)

        if model.get_file_path() is not None:
            data = model.get_file_path()
            image = data["image"]
            imageArray = data["imageArray"]
            imagegray = cv2.cvtColor(imageArray, cv2.COLOR_BGR2RGB)
            image_comparison(
                img1=image,
                img2=imagegray,
                label1="Image Noisy",
                label2="Image DeNoised",
                starting_position=50,
                show_labels=True,
                make_responsive=True,
                in_memory=True,
            )

            pass
        else:
            st.info("Video hướng dẫn")
            st.video(open('assets/video/video.mp4', 'rb').read())

    def upload_file(self, model, uploaded_file):
        if uploaded_file is not None:
            pil_image = Image.open(BytesIO(uploaded_file.read()))
            cv_image = np.array(pil_image)
            model.set_file_path({"image": pil_image, "imageArray": cv_image})
            print("input")
