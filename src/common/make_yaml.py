import yaml

with open('console_access_settings.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)