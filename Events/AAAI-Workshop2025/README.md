# AAAI 2025 : Streamlining Enterprise AI RAG Pipelines with OPEA and IBM DataPrepKit

## Abstract

Retrieval-augmented generation (RAG) systems are transforming enterprise AI by delivering accurate and contextually aware responses. However, RAG’s success hinges on high-quality data preparation and robust deployment pipelines. This workshop combines IBM DataPrepKit and OPEA to showcase an end-to-end workflow for building scalable RAG systems. Participants will gain hands-on experience in preparing data, configuring RAG pipelines, and integrating these tools to address real-world enterprise challenges.

This workshop demonstrates an end-to-end solution by combining IBM DataPrepKit and OPEA, providing participants with hands-on experience in: 
- Ensuring data quality for retrievers.
- Deploying models at scale with optimized hardware.
- Integrating pipelines to streamline workflows.

This workshop focuses on leveraging IBM DataPrepKit for robust data preparation and OPEA for deploying scalable RAG solutions, demonstrating how these tools address critical pain points in enterprise AI.

## Workshop Objectives

Provide a foundational understanding of RAG systems and their enterprise applications.
Guide participants in preparing high-quality datasets using IBM DataPrepKit.
Showcase the deployment of scalable RAG pipelines using OPEA on Intel Gaudi accelerators.

## What you will learn
By the end of the workshop, participants will:
- Understand the architecture and applications of RAG systems.
- Learn best practices for preparing data with IBM DataPrepKit for retrievers.
- Gain hands-on experience building and deploying RAG pipelines using OPEA.
- Master integration techniques for dynamic and scalable workflows.

## Structure and Duration
Duration: 1 hour.
Format: Lecture (20%), Hands-on (70%), Q&A (10%).

## Intended Audience
AI engineers and data scientists exploring advanced NLP systems.
Solution architects focused on deploying enterprise-scale AI.
Professionals interested in RAG and its applications in knowledge-intensive domains.

## Prerequisites
Comfortable python programming language
Basic understanding of microservices, cloud architecture
Attendees would be given cloud access to run the workshop

## Agenda:
- Introduction to RAG and Challenges (10 minutes)
- Data Preparation with IBM DataPrepKit (20 minutes)
- Building RAG Pipelines with OPEA (20 minutes)
- Closing Discussion and Q&A (10 minutes)

## Detailed Outline
1. Introduction to RAG Concepts (10 minutes)
Overview of RAG architecture: retrievers, generators, and rerankers.
Use cases: enterprise search, knowledge management, and personalized recommendations.
Challenges in RAG system deployment.

2. Data Preparation with IBM DataPrepKit (20 minutes)
Hands-on activity: Preparing datasets.
We will showcase processing and cleaning various PDF documents so they can be used for RAG.
Exporting cleaned data into a vector database for querying

3. RAG Pipeline Deployment with OPEA (20 minutes)
Building RAG pipelines with OPEA:
Configuring retrievers with the cleaned dataset.
Deploying open LLMs (LLama / Mistral-7B / Granite) for generative capabilities.
Incorporating rerankers for improved relevance.
Hands-on: Participants deploy a travel Q&A system based on the pipeline.

    [Follow this guide](data-prep.md)

4. Bonus Topics (Time Permitting)
Utilizing Intel Gaudi accelerators for optimization and scalability.
Experiment with various vector databases

5. Q&A  and next steps (10 mins)

## Conclusion
This workshop provides a hands-on introduction to building scalable RAG systems, emphasizing data preparation and deployment optimization. By combining IBM DataPrepKit and OPEA, participants will learn to create robust, real-world AI pipelines that seamlessly bridge data quality and model performance.


## Authors and Contributors

### Ezequiel Lanza

**Open Source AI Evangelist at Intel (TAC Chair for [LF AI and Data](https://lfaidata.foundation))**


👋 Hi, I'm Ezequiel Lanza (Eze), and I'm passionate about helping people explore the thrilling realm of artificial intelligence. As a regular AI conference presenter, I take pride in creating impactful use cases, tutorials, and guides to assist developers in adopting open source AI tools.With a solid foundation in engineering and a decade of experience assisting customers and developers in the software realm, I bring a wealth of practical knowledge to the table. Currently, I'm writing my thesis as I pursue a Master's in Data Science from Universidad Austral in Argentina (Yeah, it was AI before ChatGPT:).
[Linkedin](https://www.linkedin.com/in/ezelanza/)  &nbsp;  • &nbsp;[Dev.to](https://dev.to/eze_lanza)

### Sujee Maniyam

**AI Engineer, Developer Advocate @ Node51 (Consulting for [IBM / The AI Alliance](https://thealliance.ai/))**  <br>

Sujee Maniyam is an expert in Generative AI, Machine Learning, Deep Learning, Big Data, Distributed Systems, and Cloud technologies. He is passionate about developer education, fostering community engagement. Sujee has led numerous training sessions, hackathons, and workshops. He is also an author, open source contributor and frequent speaker at conferences and meetups.

[Linkedin](https://www.linkedin.com/in/sujeemaniyam/) &nbsp;  • &nbsp;[portfolio](https://sujee.dev/portfolio)

### Murilo Gustineli

**Senior AI Software Solutions Engineer @ Intel**

I’m a Senior AI Software Solutions Engineer at Intel, currently pursuing a master’s in Computer Science at Georgia Tech focusing on Machine Learning. My work involves creating synthetic datasets, fine-tuning large language models, and training multi-modal models using Intel’s Gaudi accelerators as part of the Development Enablement team. I’m particularly interested in Deep Learning, information retrieval, and biodiversity research, aiming to improve species identification and support conservation efforts.

[Linkedin](https://www.linkedin.com/in/murilo-gustineli/) 