# Hotjar Simple Website Test
This is a simple simulation to test the Signup and Login processes
on [Hotjar](https://hotjar.com) website, using python selenium and pytest
frameworks.

## Platforms
* Linux

## Key Modules
* Selenium (Python)
* Selenium Chrome driver
* Pytest

## Run Test

### Clone Repository
```
git clone https://gitlab.com/eruckemmanuel/hotjar-simple-website-test
```

### Install Python Dependencies
```
pip install -r requirements.txt
```

### Define Account Data
In the .env file, add details for Hotjar account


### Run Login test
```
pytest -m login
```

### Run Signup test
```
pytest -m sigup
```


## TODO
* Complete test automation for signup