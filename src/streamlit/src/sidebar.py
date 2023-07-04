"""
Sidebar
"""

import streamlit as st
from utils import (
    validate_api_key,
    populate_markdown
)

def set_openai_api_key(api_key: str):
    """
    Sets the OpenAI API key in the session state.
    """
    st.session_state["OPENAI_API_KEY"] = api_key

def set_fhir_api_base_url(base_url: str):
    """
    Sets the FHIR API Base URL in the session state.
    """
    st.session_state["FHIR_API_BASE_URL"] = base_url

def setup():
    """
    Displays a sidebar with input and info contents.
    """
    with st.sidebar:
        
        api_key_input, fhir_api_base_url = populate_markdown()

        if st.button('Configure', use_container_width=True):
            if validate_api_key(api_key_input):
                st.session_state["is_key_configured"] = True
                st.success('Successfully Configured!', icon="✅")
            else:
                st.session_state["is_key_configured"] = False
                error_message = 'Configuration failed. Please check the following input(s):'
                if not validate_api_key(api_key_input):
                    error_message += '\n- OpenAI API Key format is invalid (should start with "sk-")'
                st.error(error_message, icon="🚨")

        if api_key_input:
            set_openai_api_key(api_key_input)
        if fhir_api_base_url:
            set_fhir_api_base_url(fhir_api_base_url)

        st.markdown("---")
        st.markdown(
            "This tool is a work in progress. You can contribute to the project on [GitHub](https://github.com/ikram-shah/fhir-ai-and-openapi-chain)"
        )
        st.write('\n')
        st.caption("⚠️ This is not official HL7 FHIR's implementation")