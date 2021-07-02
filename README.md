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

## Failed Test
A failed test will generate a screenshot of the failed stage on the browser and save
in the `screenshots` folder.

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
pytest -m login -v
```

### Run Signup test
```
pytest -m sigup -v
```

### Run Test & Generate HTML Report
```
pytest -m login -v --html=login_test.hmtl
```

```
pytest -m signup -v --html=signup_test.hmtl
```


## TODO
* Complete test automation for signup