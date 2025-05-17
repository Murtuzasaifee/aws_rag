from langchain_aws import BedrockEmbeddings


def get_embedding():
    embeddings = BedrockEmbeddings()
    return embeddings