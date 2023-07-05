# FHIR - AI and OpenAPI Chain

[![Gitter](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://openexchange.intersystems.com/package/FHIR---AI-and-OpenAPI-Chain)
[![Quality Gate Status](https://community.objectscriptquality.com/api/project_badges/measure?project=intersystems_iris_community%2Firis-fhir-template&metric=alert_status)](https://community.objectscriptquality.com/dashboard?id=intersystems_iris_community/fhir-ai-and-openapi-chain)

💻  Contributors - [Ikram Shah](https://community.intersystems.com/user/ikram-shah) and [Sowmiya Nagarajan](https://community.intersystems.com/user/sowmiya-nagarajan).

💪  Built with [OpenAI](https://openai.com/), [LangChain](https://github.com/hwchase17/langchain) & [Streamlit](https://streamlit.io/)

## Demo

https://github.com/ikram-shah/fhir-ai-and-openapi-chain/assets/17762967/99512028-8190-4581-9f0a-fd7b699c7d2c

## Overview

🤖  Ask question to any of your chosen FHIR API in natural language 🤖

<img width="1512" alt="Screenshot 2023-07-04 at 12 31 35 AM" src="https://github.com/ikram-shah/fhir-ai-and-openapi-chain/assets/17762967/30f0a468-276a-41fe-9695-9c2be85ba86d">

## Try online on [Streamlit](https://fhir-ai-and-openapi-chain.streamlit.app/)
1. Get OpenAI Key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Get FHIR Server API endpoint
   - You may either enter your own sample FHIR server (unauthenticated access needed)
   - You may create a temporary sample server in [Intersystems IRIS FHIR platform](https://learning.intersystems.com/course/view.php?id=1492)

## Try locally using local FHIR server

### OpenAI API Key
Get OpenAI Key from [OpenAI Platform](https://platform.openai.com/account/api-keys)

### Setup Local FHIR Server
1. Prerequisites: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) & [Docker desktop](https://www.docker.com/products/docker-desktop)
2. Installation:
     ```
     $ git clone https://github.com/ikram-shah/fhir-ai-and-openapi-chain.git
     ```
     ```
     $ docker-compose up -d
     ```
3. Generate sample patient data [ref](https://github.com/intersystems-community/irisdemo-base-synthea)
     ```
     ./synthea-loader.sh 10
     ```
     ```
     docker-compose exec iris iris session iris -U FHIRServer
     ```
     ```
     FHIRSERVER>d ##class(fhirtemplate.Setup).LoadPatientData("/irisdev/app/output/fhir","FHIRSERVER","/fhir/r4")
     ```
4. Test FHIR R4 API by visitng [http://localhost:32783/fhir/r4/metadata](url)

### Streamlit

 ```
 pip install -r src/streamlit/requirements.txt
 ```
 
 ```
 streamlit run src/streamlit/src/main.py
 ```
     
### Folder Structure

```
fhir-ai-and-openapi-chain/
├──src
│   ├── streamlit/              //streamlit code             
│   │   ├── src/
│   │   │   ├── main.py                 
│   │   │   └── ...
│   └── fhirtemplate/
│       ├── setup.cls
│       └── ...
.
.
.
├── requirements.txt            //requirements for streamlit to run
├── docker-compose.yml
├── Dockerfile
├── README.md
└── LICENSE
```

### Known Limitations

Due to the limitations imposed by OpenAI's token usage, if the reference data + prompt being sent to the OpenAI API exceeds the specified limit, an error may be encountered.

<img width="1069" alt="Screenshot 2023-07-04 at 12 46 09 AM" src="https://github.com/ikram-shah/fhir-ai-and-openapi-chain/assets/17762967/81d6cba7-8f74-4807-9197-5a3eca62427d">


### Useful Resouces

[HL7 OpenAPI Specifications](https://hapi.fhir.org/baseR4/api-docs)

[FHIR Postman collection by apievangelist](https://apievangelist.com/) 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/api-evangelist/workspace/fast-healthcare-interoperability-resources-fhir/collection/35240-c30a5371-445c-4046-af66-649b43842f3e?action=share&creator=4063768)

[InterSystems IRIS FHIR Documentation](https://docs.intersystems.com/irisforhealth20203/csp/docbook/Doc.View.cls?KEY=HXFHIR)

[FHIR API](http://hl7.org/fhir/resourcelist.html)

[Intersystems Community](https://community.intersystems.com/tags/fhir)

## License

This project is licensed under the [MIT License](LICENSE).

You can find the full text of the license in the [LICENSE](LICENSE) file.
