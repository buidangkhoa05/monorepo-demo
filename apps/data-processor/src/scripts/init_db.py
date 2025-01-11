from ..config.database import db
from ..config.settings import get_settings

settings = get_settings()

async def init_database():
    # Create containers if they don't exist
    await db.create_container_if_not_exists(
        settings.PREDICTIONS_CONTAINER,
        partition_key="type"
    )
    await db.create_container_if_not_exists(
        settings.MODELS_CONTAINER,
        partition_key="type"
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_database()) 