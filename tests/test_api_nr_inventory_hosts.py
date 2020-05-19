# Import modules
import requests
import pprint

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)


def api_nr_inventory_hosts_flask():
    # Define base url
    url = "http://localhost:5000/"
    # Define the API path to be tested
    api_path = "api/nr/inventory/hosts"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200
    req_body = req.json()
    # print full request and response
    pp.pprint(req)
    pp.pprint(req_body)


def api_nr_inventory_hosts_specific():
    # Define base url
    url = "http://localhost:5000/"
    # Define the API path to be tested
    api_path = "api/nr/inventory/groups"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    req_body = req.json()
    # Assert that each host is configured correctly with the correct group and hostname
    assert req_body["dfjt-r001.lab.dfjt.local"]["hostname"] == "10.0.0.1"
    assert req_body["lab-arista-01.lab.dfjt.local"]["groups"] == "eos"
    assert req_body["lab-arista-01.lab.dfjt.local"]["hostname"] == "10.0.0.11"
    assert req_body["lab-arista-02.lab.dfjt.local"]["groups"] == "eos"
    assert req_body["lab-arista-02.lab.dfjt.local"]["hostname"] == "10.0.0.18"
    assert req_body["lab-csr-01.lab.dfjt.local"]["groups"] == "ios"
    assert req_body["lab-csr-01.lab.dfjt.local"]["hostname"] == "10.0.0.16"
    assert req_body["lab-junos-01.lab.dfjt.local"]["groups"] == "junos"
    assert req_body["lab-junos-01.lab.dfjt.local"]["hostname"] == "10.0.0.15"
    assert req_body["lab-nxos-01.lab.dfjt.local"]["groups"] == "nxos"
    assert req_body["lab-nxos-01.lab.dfjt.local"]["hostname"] == "10.0.0.14"
    # print full request and response
    pp.pprint(req)
    pp.pprint(req_body)
