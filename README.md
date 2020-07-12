# Faker_elasticsearch

Faker_elasticsearch is a conda package that you can use to generate and store fake data in your elastic search server.

## Installation

Use the package manager [conda](url) to install faker_elasticsearch.

```bash
conda install faker_elasticsearch
```

## Usage

Step 1: Create a config file stating the configurations of the elasticsearch server.

Notice the schema of fake data documents is also a part of this config file. An example
document schema is given in the config file below.

Sample config file:
```text
es_url = "http://localhost:9200/"
index_name = "test_data"
index_type = "test_type"
batch_size = 1000
num_of_shards = 2
http_upload_timeout = 3
count = 100000
format = "name:str,address:words,country_code:country_code,acc_id:account_number,ip_address:ipv4,timestamp:ts"
num_of_replicas = 0
force_init_index = False
set_refresh = False
out_file = "test.csv"
id_type = None
dict_file = None
username = None
password = None
validate_cert = True
```

```python
from faker_elasticsearch import elasticsearch_data
path_to_config = "es.config"  # path to the config file.
elasticsearch_data.create_fake_data(path_to_config=path_to_config)
```

That's all, enjoy!!!

Note: Currently supported field types are:

- `bool` returns a random true or false
- `ts` a timestamp (in milliseconds), randomly picked between now +/- 30 days
- `ipv4` returns a random ipv4
- `tstxt` a timestamp in the "%Y-%m-%dT%H:%M:%S.000-0000" format, randomly
  picked between now +/- 30 days
- `int:min:max` a random integer between `min` and `max`. If `min` and `max`
  are not provided they default to 0 and 100000
- `str:min:max` a word ( as in, a string), made up of `min` to `max` random
  upper/lowercase and digit characters. If `min` and `max` are optional,
  defaulting to `3` and `10`
- `words:min:max` a random number of `strs`, separated by space, `min` and
  `max` are optional, defaulting to '2' and `10`
- `dict:min:max` a random number of entries from the dictionary file,
  separated by space, `min` and `max` are optional, defaulting to '2' and `10`
- `text:words:min:max` a random number of words seperated by space from a
  given list of `-` seperated words, the words are optional defaulting to
  `text1` `text2` and `text3`, min and max are optional, defaulting to `1`
  and `1`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please start contributing to unit tests. I will gradually update when I get the time.

## License
[MIT](https://choosealicense.com/licenses/mit/)