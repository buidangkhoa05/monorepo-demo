from azure.cosmos import CosmosClient, PartitionKey
from .settings import get_settings

settings = get_settings()

class Database:
    def __init__(self):
        self.client = CosmosClient(
            url=settings.COSMOS_ENDPOINT,
            credential=settings.COSMOS_KEY
        )
        self.database = self.client.get_database_client(settings.COSMOS_DATABASE)
        
    def get_container(self, container_name: str):
        return self.database.get_container_client(container_name)
    
    async def create_container_if_not_exists(self, container_name: str, partition_key: str):
        try:
            return self.database.create_container_if_not_exists(
                id=container_name,
                partition_key=PartitionKey(path=f"/{partition_key}")
            )
        except Exception as e:
            print(f"Error creating container: {e}")
            raise

db = Database() 