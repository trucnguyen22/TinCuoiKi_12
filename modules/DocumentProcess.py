import os
import re
from streamlit_elements import elements, mui, html
from streamlit_elements import *
import streamlit as st
import pandas as pd
import numpy as np
import json
import shutil
import docx
# =========================
from modules.GoogleForm import GoogleFormGenerator
from modules.modules import Custom_Code

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
        self.convert_to_label = None
        self.check = False         
        self.save_folder = "./assets/output"
        self.pattern = re.compile(r'^(câu|bài|cau|bai|\d+:)', re.IGNORECASE)                    
    def viewDocumentation(self, model, sidebar):        
        placeholder_show = st.empty()
        
        with sidebar:
            createform = st.empty()
            st.subheader(model.subheader_1)
            name_group = st.text_input("Tên môn học")
            warning_name_group = st.empty()
            with st.form("upload-form", clear_on_submit=True):
                uploaded_file = st.file_uploader(model.upload_button_text_desc, 
                                                #  accept_multiple_files=True,
                                                 type=['docx'],
                                                 help=model.upload_help,
                                                 key="uploaded_file" 
                                                )
                submitted = st.form_submit_button(model.upload_button_text)
                reset = st.form_submit_button("Reset")
                
                if reset:
                    st.session_state.pop('file_path', None)
                    pass
                
                if submitted and uploaded_file is not None:
                    if name_group == "":
                        with warning_name_group:
                            st.warning("Vui lòng nhập tên môn học")
                        return
                    with st.spinner('Wait for it...'):
                        self.upload_file(model, uploaded_file, name_group)
        
        if model.get_file_path() is not None:
            dataJSON = self.read_json_file(model.get_file_path())
            
            st.metric("Số lượng câu hỏi", len(dataJSON))
            with st.expander("Tạo Form"):
                st.title("Setting")
                st.checkbox('Activate quiz', True, key="quiz_toggle")
                st.checkbox('Activate required', True, key="required_toggle")
                st.checkbox('Activate shuffle', True, key="shuffle_toggle")
                with st.form("Create-Form", clear_on_submit=True):
                    title_form = st.text_input('Tiêu đề form', placeholder='Nhập thông tin ...')
                    form_description = st.text_input('Thông tin mô tả', placeholder='Nhập thông tin ...')
                    form_documentTitle = st.text_input('Tên file', placeholder='Nhập thông tin ...')
                    submitted = st.form_submit_button(model.upload_button_text)    
                    
                    if submitted and title_form is not None and form_description is not None and form_documentTitle is not None:
                        form_generator = GoogleFormGenerator()
                        form_generator.authenticate()
                        form_generator.create_google_form(title_form, form_description, form_documentTitle)
                        form_generator.setting_configure(
                            is_quiz=st.session_state.quiz_toggle,
                            is_required=st.session_state.required_toggle,
                            is_shuffle=st.session_state.shuffle_toggle,
                        )     
                        with st.spinner("Wait for it..."):
                            form_generator.read_data_from_json(dataJSON)     
                        st.link_button("Link form 😘", form_generator.get_link_form())
                        pass
                    else:
                        st.warning("Vui lòng điền đầy đủ thông tin")
            st.title("Nội dung")
            for j, data in enumerate(dataJSON):
                question = data["question"]
                answer = data["answer"]
                right_answer = data["right_answer"]
                with st.expander(question, False):
                    st.subheader("Câu trả lời:")
                    for i,text in enumerate(answer):
                        st.text_area(text["value"], text["value"], key=f"{j}{i}", disabled=True, label_visibility="hidden")
                    st.subheader("Câu trả lời đúng:")
                    for text in right_answer:
                        st.success(text["value"])
            pass
        else:
            st.info("Video hướng dẫn")
            # st.video(open('assets/video/video.mp4', 'rb').read())
        
            
    def set_save_folder_group(self, group):
        self.save_folder_group = str(group)
        self.pathfile_result = os.path.join(self.save_folder, self.save_folder_group)
            
    def save_file_json(self, model, name, data):
        output_directory = os.path.join(self.pathfile_result)
        os.makedirs(output_directory, exist_ok=True)
        file_path = os.path.join(output_directory, f"{name}.json")
        model.set_file_path(file_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None
        
    def upload_file(self, model, uploaded_file, name_group = None):           
        if name_group is None:
            name_group = "demo"  
            
        if uploaded_file is not None:
            self.set_save_folder_group(name_group)
            data_json = []
            doc = docx.Document(uploaded_file)
            paragraphs = [p for p in doc.paragraphs if p.text.strip()]
            print("\n"*5)
            for i in range(0, len(paragraphs)):
                if self.pattern.search(paragraphs[i].text):
                    data_json.append({
                        "question": paragraphs[i].text,
                        "answer": [],
                        "right_answer": []
                    })
                    indexOfJson = len(data_json) - 1
                else:
                    text = paragraphs[i].text
                    runs = paragraphs[i].runs
                    data_json[indexOfJson]["answer"].append({"value":text})
                    if runs[0].font.color.rgb is not None or runs[0].bold or runs[0].underline:
                        data_json[indexOfJson]["right_answer"].append({"value":text})
                
            json_data = json.dumps(data_json, ensure_ascii=False, indent=4)
            self.save_file_json(model, name_group, data_json)