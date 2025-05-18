# RAG Application on AWS

A Retrieval-Augmented Generation (RAG) application built with LangChain and AWS Bedrock, deployed using AWS CDK.

## Overview

This application implements a RAG system that:
- Processes PDF documents as knowledge sources
- Creates vector embeddings using AWS Bedrock
- Stores embeddings in a ChromaDB vector database
- Retrieves relevant context based on user queries
- Generates responses using LLMs via AWS Bedrock
- Provides a REST API for querying the system
- Stores query history in DynamoDB

## Architecture

The application consists of two main components:
1. **RAG Pipeline**: Core RAG functionality with API endpoints
2. **AWS Infrastructure**: CDK code for deploying the application

## Prerequisites

- Python 3.11+
- AWS account with Bedrock access
- AWS credentials configured locally
- Docker (for local testing and deployment)

## Installation

### RAG Pipeline

```bash
cd rag_pipeline
pip install -e .
```

### AWS Infrastructure

```bash
cd aws-rag-infra
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Adding Documents

1. Place PDF documents in the `rag_pipeline/src/data/source` directory
2. Create or update the vector database:
```bash
cd rag_pipeline
python create_db.py
```

To reset the database:
```bash
python create_db.py --reset
```

### Local Testing

Run the API server locally:
```bash
cd rag_pipeline
docker build --platform linux/amd64 -t aws_rag_app .
docker run --platform linux/amd64 --rm -it -p 8000:8000 -v ~/.aws:/root/.aws --entrypoint python aws_rag_app src/app_api_handler.py
```

### Deployment

Deploy the application to AWS:
```bash
cd aws-rag-infra
cdk synth
cdk deploy
```

### Querying the RAG System

#### Via API

Send a POST request to the deployed API endpoint:
```bash
curl -X POST https://<function-url>/submit_query -H "Content-Type: application/json" -d '{"query_text":"How can I contact support?"}'
```

#### Via Python

```python
from src.rag_app.query_rag import query_rag

response = query_rag("How can I contact support?")
print(response.response_text)
```

## Project Structure

- `rag_pipeline/` - Core application code
  - `src/rag_app/` - RAG implementation
    - `embeddings.py` - AWS Bedrock embedding functions
    - `chromaDB.py` - ChromaDB vector store interface
    - `query_rag.py` - RAG query processing logic
  - `src/data/` - Data directories
    - `source/` - Source PDF documents
    - `chroma/` - ChromaDB vector database
  - `src/app_api_handler.py` - FastAPI application
- `aws-rag-infra/` - AWS CDK infrastructure code

## Configuration

The application uses Meta Llama 3 70B by default. To change the model, modify the `BEDROCK_MODEL_ID` in `src/rag_app/query_rag.py`.

## Security Note

Ensure you're using environment variables or AWS IAM roles for credentials in production instead of hardcoded credentials.
