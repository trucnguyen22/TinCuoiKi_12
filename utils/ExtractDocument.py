import streamlit as st
from modules import *
from pathlib import Path

def sidebarConfig(sidebar):
    with sidebar:
        pass

def customsGroup(current_dir):
    css__custom = f'{current_dir}/assets/styles/custom.css'
    Custom_CSS(st, css__custom)
    Custom_Code(st, """
            <div class="main__title"> 
                <h3> ExtractDocument <h3>
            <div/>        
        """)


def main(sidebar):
    pass
    # DocumentProcess().viewExtractDocument(DocumentProcess.Model(), sidebar)
    # DataReview().view(DataReview.Model(), sidebar)

def ExtractDocument(sidebar):
    current_dir = Path(".")
    sidebarConfig(sidebar)
    customsGroup(current_dir)
    main(sidebar)