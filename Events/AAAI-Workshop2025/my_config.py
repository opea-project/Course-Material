import os 


## Configuration
class MyConfig:
    pass 

MY_CONFIG = MyConfig ()

## Input Data - configure this to the folder we want to process
MY_CONFIG.INPUT_DATA_DIR = "input"
MY_CONFIG.OUTPUT_FOLDER = "output"
MY_CONFIG.OUTPUT_FOLDER_FINAL = os.path.join(MY_CONFIG.OUTPUT_FOLDER , "output_final")
### -------------------------------

### Milvus config
#MY_CONFIG.DB_URI = './rag_2.db'  # For embedded instance
MY_CONFIG.DB_URI = 'http://localhost:19530'  # For docker
MY_CONFIG.COLLECTION_NAME = 'rag_milvus'


## Embedding model
MY_CONFIG.EMBEDDING_MODEL = 'BAAI/bge-base-en-v1.5'
MY_CONFIG.EMBEDDING_LENGTH = 768
