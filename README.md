s2i build -e S2I_SOURCE_NOTEBOOK_LIST=01_chatbot_data_preparation.ipynb,02_chatbot_model.ipynb quay.io/willbenton/nachlass-s2i:latest https://github.com/hanvitha/chatbot_notebooks

pipelines in project chatbot_pipelines