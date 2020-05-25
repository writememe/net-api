# Import modules
import requests
import pprint

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)

# Define base url
url = "http://localhost:5000/"

# Provide the dictionary of parameters for the request
param_dict = {"host": "lab-csr-01.lab.dfjt.local"}

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_facts_host_api(url, param_dict):
    # Define the API path to be tested
    api_path = "api/nr/napalm/facts/host"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path, params=param_dict)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_interfaces_host_api(url, param_dict):
    # Define the API path to be tested
    api_path = "api/nr/napalm/interfaces/host"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path, params=param_dict)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_interfaces_ip_host_api(url, param_dict):
    # Define the API path to be tested
    api_path = "api/nr/napalm/interfaces_ip/host"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path, params=param_dict)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_ntp_servers_host_api(url, param_dict):
    # Define the API path to be tested
    api_path = "api/nr/napalm/ntp_servers/host"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path, params=param_dict)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_users_host_api(url, param_dict):
    # Define the API path to be tested
    api_path = "api/nr/napalm/users/host"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path, params=param_dict)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200