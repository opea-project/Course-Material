# GenAI Workshops - Deploying OPEA ChatQnA RAG on Kubernetes

## Abstract

Retrieval-augmented generation (RAG) systems are transforming enterprise AI by delivering accurate and contextually aware responses. However, RAG’s success hinges on robust, scalable deployment pipelines.  
This workshop showcases how to deploy [**OPEA ChatQnA**](https://github.com/opea-project/GenAIExamples/tree/main/ChatQnA), an open, modular RAG system, on Kubernetes. Participants will gain hands-on experience deploying in Kubernetes environments, deploying RAG microservices, and integrating them into a working system.

This workshop demonstrates an end-to-end solution by deploying OPEA ChatQnA RAG pipelines in Kubernetes, providing participants with hands-on experience in:
- Deploying models, retrievers, and vector databases as microservices.
- Configuring scalable RAG systems.
- Accessing and interacting with deployed RAG APIs.
- Replacing the LLM model and observing behavior differences.

## What you will learn

By the end of the workshop, participants will:
- Understand the architecture of OPEA ChatQnA RAG systems.
- Deploy embedding models, vector stores, and RAG APIs in Kubernetes.
- Configure services and endpoints for accessing the deployed system.
- Replace the LLM model and evaluate system performance and output quality.
- Gain practical skills for scaling and troubleshooting RAG systems in production.

## Structure and Duration

- **Duration**: 2 hours 
- **Format**: Lecture (20%), Hands-on (70%), Q&A (10%)

## Intended Audience

- AI engineers and data scientists building NLP and RAG applications.
- DevOps engineers and solution architects deploying AI services.
- Professionals interested in scalable GenAI system deployment.

## Prerequisites

- Comfortable with basic Kubernetes concepts (pods, services, deployments).
- Familiarity with Python (optional for deeper API interaction).
- Basic knowledge of microservices and cloud-native architecture.
- `kubectl` and `helm` installed locally.
- A running Kubernetes cluster (local or cloud).
- Attendees will be provided cloud access with setup instructions.

## Agenda

- Set up Kubernetes environments for participants (15 minutes)
- Introduction to OPEA ChatQnA RAG architecture (15 minutes)
- Deploying RAG pipelines with Helm on Kubernetes (60 minutes)
- Replacing the LLM model and checking behavior (15 minutes)
- Practical example: Querying the deployed ChatQnA system (15 minutes)
- Closing Discussion and Q&A (10 minutes)

## Detailed Outline

### 1. Introduction to OPEA ChatQnA RAG Concepts (10 minutes)

- Overview of OPEA ChatQnA RAG architecture: retrievers, generators, APIs.
- Use cases: enterprise search, knowledge management, domain-specific assistants.
- Challenges in RAG system deployment at scale.

### 2. Building RAG Pipelines on Kubernetes with OPEA (60 minutes)

- Setting up namespace and dependencies.
- Deploying embedding models and vector databases.
- Configuring ChatQnA API microservice.
- Exposing the API via ingress or load balancer.

### 3. Replacing the LLM Model (15 minutes)

- How to swap the generator model (e.g., moving from Intel Mistral to Qwen).
- Updating the Kubernetes deployments and config.
- Observing differences in behaviour.

### 4. Practical Example (15 minutes)

- Sending queries to the deployed ChatQnA endpoint.
- Analyzing retrieved context and generated answers.
- Troubleshooting and scaling tips.

### 5. Q&A and Next Steps (10 minutes)

- Discussion on real-world deployment patterns.
- Sharing further resources and community channels.

## Conclusion

This workshop provides a hands-on introduction to deploying scalable RAG systems in Kubernetes. By deploying and modifying OPEA ChatQnA, participants will learn to create robust, real-world AI pipelines that seamlessly integrate retrieval and generation components using open, modular architectures.

## Authors and Contributors

### Ezequiel Lanza

**Open Source AI Evangelist at Intel (TAC Chair/Board Member for [LF AI and Data](https://lfaidata.foundation))**


👋 Hi, I'm Ezequiel Lanza (Eze), and I'm passionate about helping people explore the thrilling realm of artificial intelligence. As a regular AI conference presenter, I take pride in creating impactful use cases, tutorials, and guides to assist developers in adopting open source AI tools.With a solid foundation in engineering and a decade of experience assisting customers and developers in the software realm, I bring a wealth of practical knowledge to the table. Currently, I'm writing my thesis as I pursue a Master's in Data Science from Universidad Austral in Argentina (Yeah, it was AI before ChatGPT:).
[Linkedin](https://www.linkedin.com/in/ezelanza/)  &nbsp;  • &nbsp;[Dev.to](https://dev.to/eze_lanza)

### Murilo Gustineli

**Senior AI Software Solutions Engineer @ Intel**

I’m a Senior AI Software Solutions Engineer at Intel, currently pursuing a master’s in Computer Science at Georgia Tech focusing on Machine Learning. My work involves creating synthetic datasets, fine-tuning large language models, and training multi-modal models using Intel’s Gaudi accelerators as part of the Development Enablement team. I’m particularly interested in Deep Learning, information retrieval, and biodiversity research, aiming to improve species identification and support conservation efforts.

[Linkedin](https://www.linkedin.com/in/murilo-gustineli/) 

### Kelli Belcher

**AI Software Solutions Engineer @ Intel**

I'm an AI Software Solutions Engineer at Intel with a background in risk analytics and decision science across the financial services, healthcare, and tech industries. In my current role, I help to build machine learning and GenAI solutions using Intel's portfolio of open AI software tools. I hold a Master of Science degree in Data Analytics from the University of Texas.

[Linkedin](https://www.linkedin.com/in/kelli-belcher/) 
