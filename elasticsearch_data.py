import asyncio

from es_test_data import CreateFakeData


def create_fake_data(path_to_config: str = "./config/es.config"):
    c = CreateFakeData(path_to_config=path_to_config)
    asyncio.get_event_loop().run_until_complete(c.generate_test_data())


create_fake_data()
