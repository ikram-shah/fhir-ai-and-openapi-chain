"""
Utility functions
"""

import re
import streamlit as st

from langchain.tools import OpenAPISpec, APIOperation

def clear_submit():
    """
    Clears the 'submit' value in the session state.
    """
    st.session_state["submit"] = False

def paths_and_methods():
    with st.spinner(text="Loading..."):
        spec = OpenAPISpec.from_url("https://hapi.fhir.org/baseR4/api-docs")
        OpenAPISpec.base_url = st.session_state.get("FHIR_API_BASE_URL")

        specifications = spec
        col1, col2 = st.columns(2)

        with col1:
            selected_path = st.selectbox("Select a path:", specifications.paths.keys())

        with col2:
            if selected_path:
                selected_method = st.selectbox("Select a method:", specifications.get_methods_for_path(selected_path))

        operation = APIOperation.from_openapi_spec(specifications, selected_path, selected_method)

        return operation

def validate_api_key(api_key_input):
    """
    Validates the provided API key.
    """
    api_key_regex = r"^sk-"
    api_key_valid = re.match(api_key_regex, api_key_input) is not None
    return api_key_valid

def set_logo_and_page_config():
    """
    Sets the HL7 FHIR logo image and page config.
    """
    im = "src/streamlit/src/assets/logo.png"
    st.set_page_config(page_title="FHIR AI and OpenAPI Chain", page_icon=im, layout="wide")
    st.image(im, width=50)
    st.header("FHIR AI and OpenAPI Chain")
    
def populate_markdown():
    """
    Populates markdown for sidebar.
    """
    st.markdown(
            "## How to use\n"
            "1. Add your [OpenAI API key](https://platform.openai.com/account/api-keys)\n"
            "2. Add your FHIR server endpoint (unauthenticated access needed)\n"
            "3. Ask question that can be answered from any chosen FHIR API\n")
    st.divider()
    api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
            help="You can get your API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)", 
            value=st.session_state.get("OPENAI_API_KEY", ""))
    fhir_api_base_url = st.text_input(
            "FHIR API Base URL",
            type="default",
            placeholder="http://",
            help="You may create sample FHIR server in [Intersystems IRIS](https://learning.intersystems.com/course/view.php?id=1492)",
            value=st.session_state.get("FHIR_API_BASE_URL", ""))
    return api_key_input,fhir_api_base_url

def check_all_config():
    if st.session_state.get("OPENAI_API_KEY") and st.session_state.get("FHIR_API_BASE_URL"):
        return True
    else:
        return False