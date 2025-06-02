# Preparing Data with Data Prep Kit

## Overview

In this section, we will process PDF documents and save them into a vector database

Here is the workflow:

![](Images/data-prep-1.png)


## Step-1: Setup Python Dev Environment

```bash
conda create -n rag-1 -y python=3.11
conda activate rag-1
pip install -r requirements.txt
```

## Step-2: Process Data

Run notebook: [process_data.ipynb](process_data.ipynb)