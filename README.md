# Inventory

Inventory is a basic asset management system (Windows).

## Installation

I prefer to run it in a docker container where possible: (both methods expect a file called env_file with a VAR=VAL format

```bash
docker build -t inventory:latest .
docker run --env-file=env_file -d -p 5000:5000 inventory
```

Or

```bash
docker build -t inventory:latest .
docker-compose up
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
