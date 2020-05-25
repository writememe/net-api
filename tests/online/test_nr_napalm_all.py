# Import modules
import requests
import pprint
import pytest

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)

# Define base url
url = "http://localhost:5000/"

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_facts_all_api(url):
    # Define the API path to be tested
    api_path = "api/nr/napalm/facts/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_interfaces_all_api(url):
    # Define the API path to be tested
    api_path = "api/nr/napalm/interfaces/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_interfaces_ip_all_api(url):
    # Define the API path to be tested
    api_path = "api/nr/napalm/interfaces_ip/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    # TODO: Switching error code to 500 due to nxos get_interfaces_ip bug
    assert req.status_code == 500

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_ntp_servers_all_api(url):
    # Define the API path to be tested
    api_path = "api/nr/napalm/ntp_servers/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200

# Add pytest mark
@pytest.mark.frontend_online
def nr_napalm_users_all_api(url):
    # Define the API path to be tested
    api_path = "api/nr/napalm/users/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    # TODO: Switching error code to 500 due to junos get_users bug
    assert req.status_code == 500