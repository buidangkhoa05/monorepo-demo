from typing import Dict, List, Optional
from azure.cosmos import ContainerProxy
from ..config.database import db

class BaseRepository:
    def __init__(self, container_name: str):
        self.container: ContainerProxy = db.get_container(container_name)
    
    async def create(self, item: Dict) -> Dict:
        return self.container.create_item(body=item)
    
    async def get_by_id(self, id: str, partition_key: str) -> Optional[Dict]:
        try:
            return self.container.read_item(item=id, partition_key=partition_key)
        except Exception:
            return None
    
    async def query(self, query: str, parameters: Optional[Dict] = None) -> List[Dict]:
        parameters = parameters or {}
        items = self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        )
        return [item for item in items]
    
    async def update(self, id: str, item: Dict, partition_key: str) -> Optional[Dict]:
        try:
            return self.container.replace_item(item=id, body=item, partition_key=partition_key)
        except Exception:
            return None
    
    async def delete(self, id: str, partition_key: str) -> bool:
        try:
            self.container.delete_item(item=id, partition_key=partition_key)
            return True
        except Exception:
            return False 