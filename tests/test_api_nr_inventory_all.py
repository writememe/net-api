# Import modules
import requests
import pprint

# Set indentation on pretty print
pp = pprint.PrettyPrinter(indent=2)


def api_nr_inventory_all_flask():
    # Define base url
    url = "http://localhost:5000/"
    # Define the API path to be tested
    api_path = "api/nr/inventory/all"
    # Convert dict to json by json.dumps() for body data.
    req = requests.get(url + api_path)
    # Validate response headers and body contents, e.g. status code.
    assert req.status_code == 200
    req_body = req.json()
    # Assert that the default username and password are showing "**REACTED**"
    # rather than the exact value
    assert req_body["defaults"]["username"] == "**REDACTED**"
    assert req_body["defaults"]["password"] == "**REDACTED**"
    # print full request and response
    pp.pprint(req)
    pp.pprint(req_body)
