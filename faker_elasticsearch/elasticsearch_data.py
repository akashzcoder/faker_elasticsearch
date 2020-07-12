import asyncio

from faker_elasticsearch.es_test_data import CreateFakeData


def create_fake_data(path_to_config: str):
    """
    Create fake data is used to connect to the elasticsearch server, generate and store documents asynchronously.
    The format of documents and the configuration of elasticsearch is read from the config file.

    :param path_to_config: path to the configuration file.
    :return: None
    """
    c = CreateFakeData(path_to_config=path_to_config)
    asyncio.get_event_loop().run_until_complete(c.generate_test_data())
