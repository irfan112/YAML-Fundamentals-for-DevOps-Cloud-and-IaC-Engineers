import yaml

my_file = "basics-structure-2-newline-char.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print("--------")
            print(f'{value}')

    except yaml.YAMLERROR as err:
        print(err)