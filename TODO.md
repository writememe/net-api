# TODO List

## app/net.py

- [ ] Add all other `getters`

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