"""
Utility functions
"""

import re
import yaml
import os
import streamlit as st

from langchain.tools import OpenAPISpec, APIOperation

models = ['gpt-3.5-turbo','gpt-4','text-davinci-003','text-curie-001']

def clear_submit():
    """
    Clears the 'submit' value in the session state.
    """
    st.session_state["submit"] = False

def paths_and_methods():
    spec = OpenAPISpec.from_url("https://hapi.fhir.org/baseR4/api-docs")
    OpenAPISpec.base_url = st.session_state.get("FHIR_API_BASE_URL")

    col1, col2 = st.columns(2)

    with col1:
        selected_path = st.selectbox("Select a path:", spec.paths.keys())

    with col2:
        if selected_path:
            selected_method = st.selectbox("Select a method:", spec.get_methods_for_path(selected_path))

    operation = APIOperation.from_openapi_spec(spec, selected_path, selected_method)

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
    im = "src/streamlit/src/assets/fhir-logo.png"
    st.set_page_config(page_title="FHIR AI and OpenAPI Chain", page_icon=im, layout="wide")
    st.image(im, width=100)
    st.header("FHIR AI and OpenAPI Chain")
    st.caption("⚠️ This is not official HL7 FHIR's implementation")
    
def populate_markdown():
    """
    Populates markdown for sidebar.
    """
    st.markdown(
            "## How to use\n"
            "1. Choose preferred OpenAI Model, your [OpenAI API key](https://platform.openai.com/account/api-keys) 🔑\n"
            "2. Ask any question that can be answered from FHIR API 💬\n")
    st.session_state["OPENAI_MODEL_CHOSEN"] = st.selectbox('OpenAI Model', models, key='model', help="Learn more at [OpenAI Documentation](https://platform.openai.com/docs/models/)")
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
            value=st.session_state.get("FHIR_API_BASE_URL", ""))
    return api_key_input,fhir_api_base_url