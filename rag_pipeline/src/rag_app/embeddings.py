from langchain_aws import BedrockEmbeddings
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def get_embedding():
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1").strip()

    session = boto3.Session(region_name=region, aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
                            aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY"))


    embeddings = BedrockEmbeddings(client=session.client('bedrock-runtime'), model_id="amazon.titan-embed-text-v1")
    return embeddings