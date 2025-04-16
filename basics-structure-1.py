import yaml

my_file = "basics-structure-1.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f"key: {key}")
            print(f"value: {value}")
            datatype = type(key)
            print(f'the datatype of {key} is {datatype}')

    except yaml.YAMLERROR as err:
        print(err)