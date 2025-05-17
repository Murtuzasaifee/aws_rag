# RAG Application Deployment on AWS

A Retrieval-Augmented Generation (RAG) application built with LangChain and AWS Bedrock.

## Overview

This application implements a RAG system that:
- Processes PDF documents as knowledge sources
- Creates vector embeddings using AWS Bedrock
- Stores embeddings in a ChromaDB vector database
- Retrieves relevant context based on user queries
- Generates responses using LLMs via AWS Bedrock

## Prerequisites

- Python 3.11+
- AWS account with Bedrock access
- AWS credentials configured locally

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -e .
```

## Usage

### Adding Documents

1. Place PDF documents in the `src/data/source` directory
2. Create or update the vector database:
```bash
python create_db.py
```

To reset the database:
```bash
python create_db.py --reset
```

### Querying the RAG System

```python
from src.rag_app.query_rag import query_rag

response = query_rag("How can I contact support?")
print(response.response_text)
```

## Project Structure

- `src/rag_app/` - Core application code
  - `embeddings.py` - AWS Bedrock embedding functions
  - `chromaDB.py` - ChromaDB vector store interface
  - `query_rag.py` - RAG query processing logic
- `src/data/` - Data directories
  - `source/` - Source PDF documents
  - `chroma/` - ChromaDB vector database

## Configuration

The application uses Meta Llama 3 70B by default. To change the model, modify the `BEDROCK_MODEL_ID` in `src/rag_app/query_rag.py`.
