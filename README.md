 [![Gitter](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://openexchange.intersystems.com/package/iris-fhir-template)
 [![Quality Gate Status](https://community.objectscriptquality.com/api/project_badges/measure?project=intersystems_iris_community%2Firis-fhir-template&metric=alert_status)](https://community.objectscriptquality.com/dashboard?id=intersystems_iris_community%2Firis-fhir-template)
 [![Reliability Rating](https://community.objectscriptquality.com/api/project_badges/measure?project=intersystems_iris_community%2Firis-fhir-template&metric=reliability_rating)](https://community.objectscriptquality.com/dashboard?id=intersystems_iris_community%2Firis-fhir-template)
# fhir-ai-and-openapi-chain
🤖 Ask questions to your FHIR API's in natural language 🤖

💪 Built with [OpenAI](https://openai.com/), [LangChain](https://github.com/hwchase17/langchain) & [Streamlit](https://streamlit.io/)

## Prerequisites
- Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
- [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

## Installation 

### Docker (e.g. for dev purposes)

Clone/git pull the repo into any local directory

```
$ git clone https://github.com/intersystems-community/iris-fhir-template.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d
```

## Streamlit

### 🌲 Environment Setup

```shell
pip install -r src/streamlit/requirements.txt
```

```shell
streamlit run src/streamlit/src/main.py
```

### 🔑 Requirements to try

1. [OpenAI API Key](https://platform.openai.com/account/api-keys)
2. FHIR Server connection details

## Patient data
The template goes with 5 preloaded patents in [/data/fhir](https://github.com/intersystems-community/iris-fhir-server-template/tree/master/data/fhir) folder which are being loaded during [docker build](https://github.com/intersystems-community/iris-fhir-server-template/blob/8bd2932b34468f14530a53d3ab5125f9077696bb/iris.script#L26)
You can generate more patients doing the following. Open shel terminal in repository folder and call:
```
#./synthea-loader.sh 10
```
this will create 10 more patients in data/fhir folder.
Then open IRIS terminal in FHIRSERVER namespace with the following command:
```
docker-compose exec iris iris session iris -U FHIRServer
```
and call the loader method:
```
FHIRSERVER>d ##class(fhirtemplate.Setup).LoadPatientData("/irisdev/app/output/fhir","FHIRSERVER","/fhir/r4")
```

 with using the [following project](https://github.com/intersystems-community/irisdemo-base-synthea)

## Testing FHIR R4 API

Open URL http://localhost:32783/fhir/r4/metadata
you should see the output of fhir resources on this server

## Development Resources
[InterSystems IRIS FHIR Documentation](https://docs.intersystems.com/irisforhealth20203/csp/docbook/Doc.View.cls?KEY=HXFHIR)
[FHIR API](http://hl7.org/fhir/resourcelist.html)
[Developer Community FHIR section](https://community.intersystems.com/tags/fhir)