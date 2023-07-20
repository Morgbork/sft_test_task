## Description

Test task for "СФТ" company.

To get all unique producers ids from contract id use the following uri:

```
/shop/producers-ids/{contract_id}/
```

## System requirements

- Python 3.10+

## Installation

To reproduce the environment on testing or deployment stage, do

```shell
$ pip install -r requirements.txt
```

## Code style

The following tools are used to maintain code style:  

**black** – code formatter  
**flake8** – code style enforcer  
**isort** – to keep imports sorted  
**pre-commit** – to manage pre-commit hooks  

To install pre-commit hooks to your local repository, run:

```shell
$ pre-commit install
$ pre-commit run --all-files
```

## Testing

```shell
$ pytest
```
