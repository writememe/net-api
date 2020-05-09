# TODO List

## app/net.py

- [x] pylama and black file
- [x] Comment up code correctly
- [ ] Add all other `getters`
  
## app/webapp.py

- [x] pylama and black file
- [ ] Comment up code correctly

## app/swagger.yml

- [x] yamllint file
- [x] Properly document API calls
- [ ] Add all other `getters`


## README.md

- [ ] Document up usage
- [ ] Add overview diagrams

# Set environmental variable
os.environ["NORNIR_DEFAULT_PASSWORD"] = "kev"
print("PASSWORD environment variable:", os.environ["NORNIR_DEFAULT_PASSWORD"])

# Examples for validation
# Import module
from os import environ
if environ.get('NORNIR_DEFAULT_PASSWORD') is not None:
    pass

## scrapli
- [ ] Document up usage
