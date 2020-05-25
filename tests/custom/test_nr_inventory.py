# Import modules
import requests
import pprint
import pytest

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)

# Define base url
url = "http://localhost:5000/"


# Add pytest mark
@pytest.mark.frontend_custom
def nr_inventory_groups_api_custom(url):
    # Define the API path to be tested
    api_path = "api/nr/inventory/groups"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    req_body = req.json()
    # Assert that platform is correctly configured for each group
    assert req_body["ios"]["platform"] == "ios"
    assert req_body["eos"]["platform"] == "eos"
    assert req_body["junos"]["platform"] == "junos"
    assert req_body["nxos"]["platform"] == "nxos"
    # Assert that scrapli specific platform is correctly configured for each group
    assert req_body["ios"]["connection_options"]["scrapli"]["platform"] == "cisco_iosxe"
    assert req_body["eos"]["connection_options"]["scrapli"]["platform"] == "arista_eos"
    assert (
        req_body["junos"]["connection_options"]["scrapli"]["platform"]
        == "juniper_junos"
    )
    assert req_body["nxos"]["connection_options"]["scrapli"]["platform"] == "cisco_nxos"
    # Assert that scrapli specific port is correctly configured for each group
    assert req_body["ios"]["connection_options"]["scrapli"]["port"] == 22
    assert req_body["eos"]["connection_options"]["scrapli"]["port"] == 22
    assert req_body["junos"]["connection_options"]["scrapli"]["port"] == 22
    assert req_body["nxos"]["connection_options"]["scrapli"]["port"] == 22
    # Assert that scrapli specific authentication strict key is correctly configured for each group
    assert (
        req_body["ios"]["connection_options"]["scrapli"]["extras"]["auth_strict_key"]
        is False
    )
    assert (
        req_body["eos"]["connection_options"]["scrapli"]["extras"]["auth_strict_key"]
        is False
    )
    assert (
        req_body["junos"]["connection_options"]["scrapli"]["extras"]["auth_strict_key"]
        is False
    )
    assert (
        req_body["nxos"]["connection_options"]["scrapli"]["extras"]["auth_strict_key"]
        is False
    )


# Add pytest mark
@pytest.mark.frontend_custom
def nr_inventory_hosts_api_custom(url):
    # Define the API path to be tested
    api_path = "api/nr/inventory/hosts"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    req_body = req.json()
    # Assert that each host is configured correctly with the correct group and hostname
    assert req_body["dfjt-r001.lab.dfjt.local"]["hostname"] == "10.0.0.1"
    assert req_body["lab-arista-01.lab.dfjt.local"]["groups"] == ["eos"]
    assert req_body["lab-arista-01.lab.dfjt.local"]["hostname"] == "10.0.0.11"
    assert req_body["lab-arista-02.lab.dfjt.local"]["groups"] == ["eos"]
    assert req_body["lab-arista-02.lab.dfjt.local"]["hostname"] == "10.0.0.18"
    assert req_body["lab-csr-01.lab.dfjt.local"]["groups"] == ["ios"]
    assert req_body["lab-csr-01.lab.dfjt.local"]["hostname"] == "10.0.0.16"
    assert req_body["lab-junos-01.lab.dfjt.local"]["groups"] == ["junos"]
    assert req_body["lab-junos-01.lab.dfjt.local"]["hostname"] == "10.0.0.15"
    assert req_body["lab-nxos-01.lab.dfjt.local"]["groups"] == ["nxos"]
    assert req_body["lab-nxos-01.lab.dfjt.local"]["hostname"] == "10.0.0.14"
