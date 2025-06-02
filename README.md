# Microsoft Build 2025 Workshop: Streamlining Enterprise AI RAG Pipelines with OPEA ChatQnA

## Abstract

Retrieval-augmented generation (RAG) systems are transforming enterprise AI by delivering accurate and contextually aware responses. However, RAG's success hinges on high-quality data preparation and robust deployment pipelines. This workshop focuses on OPEA ChatQnA to showcase an end-to-end workflow for building scalable RAG systems. Participants will gain hands-on experience in preparing data, configuring RAG pipelines, and integrating these tools to address real-world enterprise challenges.

This workshop demonstrates an end-to-end solution using OPEA ChatQnA, providing participants with hands-on experience in: 
- Ensuring data quality for retrievers.
- Deploying models at scale on Microsoft* Azure VMs.
- Integrating pipelines to streamline workflows.

This workshop focuses on leveraging OPEA for deploying scalable RAG solutions, demonstrating how these tools address critical pain points in enterprise AI.

## Workshop Objectives

Provide a foundational understanding of RAG systems and their enterprise applications.
Guide participants in preparing high-quality datasets for RAG systems.
Showcase the deployment of scalable RAG pipelines using OPEA on Azure VMs.

## What you will learn
By the end of the workshop, participants will:
- Understand the architecture and applications of RAG systems.
- Learn best practices for preparing data for retrievers.
- Gain hands-on experience building and deploying RAG pipelines using OPEA.
- Master integration techniques for dynamic and scalable workflows on Azure.

## Structure and Duration
Duration: 1 hour.
Format: Lecture (20%), Hands-on (70%), Q&A (10%).

## Intended Audience
AI engineers and data scientists exploring advanced NLP systems.
Solution architects focused on deploying enterprise-scale AI.
Professionals interested in RAG and its applications in knowledge-intensive domains.

## Prerequisites
- Proficiency in the Python programming language.
- Basic understanding of microservices architecture.
- Familiarity with cloud infrastructure concepts.
## Agenda:
- Introduction to RAG and Challenges (10 minutes)
- Data Preparation for RAG Systems (20 minutes)
- Building RAG Pipelines with OPEA (20 minutes)
- Closing Discussion and Q&A (10 minutes)
## Setup Instructions for JupyterLab on Azure VM

### Step 1: Update and Install Required Packages

#### Setting up JupyterLab with Password Authentication
1. Make the setup script executable:
   ```bash
   chmod +x setup_jupyter.sh

2. Run the setup script
   
   ```bash
   ./setup_jupyter.sh

3.  During the setup process, you will be prompted to create a password for accessing JupyterLab.


### Step 2: SSH Tunneling to Access JupyterLab
#### Securely Access JupyterLab via SSH Port Forwarding

Reverse tunneling (SSH port forwarding) is used to securely access the Jupyter notebook server running on the Azure VM from your local machine.

1. Open a terminal on your local machine and run the following command:

   ```bash
   ssh -L 9999:localhost:9999 <azureuser>@<AZURE_VM_PUBLIC_IP>

- Replace `<AZURE_VM_PUBLIC_IP>` with your VM's public IP address.
- Replace `<azureuser>` with your VM's username.
   
2. Once connected, open your browser and navigate to: http://localhost:9999
3. Enter the password you created during the setup process to access JupyterLab.

Note: To exit the virtual environment when finished, simply type deactivate

### Final Notes

Congratulations! You have successfully set up JupyterLab on your Azure VM and accessed it securely via SSH tunneling. You are now ready to proceed with the workshop activities.
If you encounter any issues during the setup or while running the notebook, please reach out to the workshop facilitators for assistance.
We hope you enjoy the workshop and gain valuable insights into building scalable RAG pipelines with OPEA ChatQnA. 

## Detailed Outline
1. Introduction to RAG Concepts (10 minutes)
Overview of RAG architecture: retrievers, generators, and rerankers.
Use cases: enterprise search, knowledge management, and personalized recommendations.
Challenges in RAG system deployment.

2. Data Preparation for RAG (20 minutes)
Hands-on activity: Preparing datasets.
We will showcase processing and cleaning various PDF documents so they can be used for RAG.
Exporting cleaned data into a vector database for querying.

3. RAG Pipeline Deployment with OPEA (20 minutes)
Building RAG pipelines with OPEA:
Configuring retrievers with the cleaned dataset.
Deploying open LLMs (LLama / Qwen) for generative capabilities.
Incorporating rerankers for improved relevance.


5. Q&A and next steps (10 mins)

## Conclusion
This workshop provides a hands-on introduction to building scalable RAG systems, emphasizing data preparation and deployment optimization. Using OPEA Chat QnA, participants will learn to create robust, real-world AI pipelines that seamlessly bridge data quality and model performance on Azure cloud infrastructure.

