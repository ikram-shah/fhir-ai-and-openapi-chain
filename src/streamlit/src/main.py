"""
FHIR - AI and OpenAPI Chain
"""

import streamlit as st
import requests

from sidebar import setup as set_sidebar
from utils import (
    clear_submit,
    paths_and_methods,
    set_logo_and_page_config
)
from langchain.requests import Requests
from langchain.llms import OpenAI
from langchain.chains import OpenAPIEndpointChain

set_logo_and_page_config()
set_sidebar()

operation = paths_and_methods()


llm = OpenAI(openai_api_key=st.session_state.get("OPENAI_API_KEY")) 

chain = OpenAPIEndpointChain.from_api_operation(
    operation,
    llm,
    requests=Requests(),
    verbose=True,
    return_intermediate_steps=False, 
)

query = st.text_area("Search Input", label_visibility="visible", placeholder="Ask anything...", on_change=clear_submit)

button = st.button("Search")

if button or st.session_state.get("submit"):
    if not st.session_state.get("is_key_configured"):
        st.error("Please configure your OpenAI and FHIR API base URL!", icon="🚨")
    elif not query:
        st.error("Please enter a question!", icon="🚨")
    else:
        st.session_state["submit"] = True
        with st.spinner(text="Searching..."):
            st.write("#### Answer")
            output = chain(query)
            st.write(output)

