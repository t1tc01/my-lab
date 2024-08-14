from qdrant_client import QdrantClient
from dotenv import load_dotenv
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.models import Filter, FieldCondition, MatchValue
import os


# Load the .env file
load_dotenv("../.env")

qdrant_url = os.getenv('QDRANT_URL')

client = QdrantClient(url=qdrant_url)
