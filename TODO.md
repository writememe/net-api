# TODO List

## app/net.py

- [x] pylama and black file
- [x] Comment up code correctly
- [ ] Add all other `getters`
- [x] Try all functions with fake password and ensure error code 500 is returned.
  
## app/webapp.py

- [x] pylama and black file
- [x] Comment up code correctly

## app/swagger.yml

- [x] yamllint file
- [x] Properly document API calls
- [ ] Add all other `getters`
- [x] Add error code 500 to the valid responses


## README.md

- [ ] Document up usage
- [x] Add overview diagrams

## .github/workflows/main.yaml
- [x] Fix the trigger on the job to exclude the README.md
- [x] Add docker run and build support
 
## scrapli
- [x] Document up usage


## tests

- [ ] Write offline tests
```
/nr/inventory/all
/nr/inventory/hosts
/nr/inventory/groups
/nr/napalm/users/all
/nr/napalm/facts/all
/nr/napalm/interfaces/all
/nr/napalm/interfaces_ip/all
/nr/napalm/ntp_servers/all
/nr/napalm/users/host
/nr/napalm/facts/host
/nr/napalm/interfaces/host
/nr/napalm/interfaces_ip/host
/nr/napalm/ntp_servers/host
/nr/napalm/napalm_cli/host
/nr/netmiko/textfsm/host
/nr/netmiko/genie/host
/nr/netmiko/host
/nr/scrapli/genie/host
/nr/scrapli/textfsm/host
/nr/scrapli/host
```
- [ ] Write online tests
```
/nr/napalm/napalm_cli/host
/nr/netmiko/textfsm/host
/nr/netmiko/genie/host
/nr/netmiko/host
/nr/scrapli/genie/host
/nr/scrapli/textfsm/host
/nr/scrapli/host
```
- [ ] pytest mark all functions
```
@pytest.mark.slow
def the_function():
```