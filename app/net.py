#! /usr/bin/env python

"""
This script is the main engine to make backend calls to network
devices and present the data back in a structured format to the
web front end.
"""

# Import modules
import os
from os import environ
from flask import jsonify, abort
from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import napalm_cli
from nornir_scrapli.tasks import send_command
from colorama import Fore, init

# Auto-reset colorama colours back after each print statement
init(autoreset=True)

# Gathering environmental variables and assigning to variables to use throughout code.
# Check whether NET_TESTFSM variable has been set, not mandatory, but recommeneded
if environ.get("NET_TEXTFSM") is None:
    # Print warning
    print(
        Fore.YELLOW
        + str("*" * 15)
        + " WARNING: Environmental variable `NET_TEXTFSM` not set. "
        + "*" * 15
    )
# Check whether NORNIR_DEFAULT_USERNAME variable has been set, not mandatory, but recommeneded
if environ.get("NORNIR_DEFAULT_USERNAME") is not None:
    # Set the env_uname to this variable so it can be used for the Nornir inventory
    env_uname = os.environ["NORNIR_DEFAULT_USERNAME"]
else:
    # Print warning
    print(
        Fore.YELLOW
        + "*" * 15
        + " WARNING: Environmental variable `NORNIR_DEFAULT_USERNAME` not set. "
        + "*" * 15
    )
    # Set the env_uname to an empty string, so that the code does not error out.
    # NOTE: It's valid form to use the groups.yaml and hosts.yaml file(s) to
    # store credentials so this will not raise an exception
    env_uname = ""
    # Print supplementary warning
    print(
        Fore.MAGENTA
        + "*" * 15
        + " NOTIFICATION: Environmental variable `NORNIR_DEFAULT_USERNAME` now set to ''."
        + "This may cause all authentication to fail. "
        + "*" * 15
    )
# Check whether NORNIR_DEFAULT_PASSWORD variable has been set, not mandatory, but recommeneded
if environ.get("NORNIR_DEFAULT_PASSWORD") is not None:
    # Set the env_pword to this variable so it can be used for the Nornir inventory
    env_pword = os.environ["NORNIR_DEFAULT_PASSWORD"]
else:
    print(
        Fore.YELLOW
        + "*" * 15
        + " WARNING: Environmental variable `NORNIR_DEFAULT_PASSWORD` not set. "
        + "*" * 15
    )
    # Set the env_pword to an empty string, so that the code does not error out.
    # NOTE: It's valid form to use the groups.yaml and hosts.yaml file(s) to
    # store credentials so this will not raise an exception
    env_pword = ""
    print(
        Fore.MAGENTA
        + "*" * 15
        + " NOTIFICATION: Environmental variable `NORNIR_DEFAULT_PASSWORD` now set to ''."
        + "This may cause all authentication to fail. "
        + "*" * 15
    )


# General functions, consumed by other functions
def get_nr():
    """
    Initialises a Nornir inventory from the various configuration
    files
    :return nr: An initialised Nornir inventory for use in other functions.
    """
    nr = InitNornir(
        inventory={
            "options": {
                "host_file": "inventory/hosts.yaml",
                "group_file": "inventory/groups.yaml",
                "defaults_file": "inventory/defaults.yaml",
            }
        }
    )
    # Set default username and password from environmental variables.
    nr.inventory.defaults.username = env_uname
    nr.inventory.defaults.password = env_pword
    return nr


def to_json(results):
    """
    Takes some Nornir results and runs them through jsonify to produce a structured result.
    :param results: The results to be processed
    :return j_results: Results after they have been run through jsonify
    """
    j_results = jsonify({host: result[0].result for host, result in results.items()})
    return j_results


# Inventory functions
def get_inv_all():
    """
    Retrieves the entire Nornir inventory into a dictionary and prepares
    it to preparation for consumption by the front end.

    NOTE: The default username and password are replaced with `**REDACTED**`
    so that these credentials are not exposed to the front-end.

    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Overwrite the default username and password,
    # so that users cannot exploit it
    nr.inventory.defaults.username = "**REDACTED**"
    nr.inventory.defaults.password = "**REDACTED**"
    # This calls all results of the get inventory dictionary call.
    r = nr.inventory.get_inventory_dict()
    return jsonify(r)


def get_inv_hosts():
    """
    Retrieves the Nornir hosts inventory into a dictionary and prepares
    it to preparation for consumption by the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # This calls all results of the get inventory dictionary call.
    # This is not ideal
    r_all = nr.inventory.get_inventory_dict()
    # Access the host directory results
    r = r_all["hosts"]
    return jsonify(r)


def get_inv_groups():
    """
    Retrieves the Nornir groups inventory into a dictionary and prepares
    it to preparation for consumption by the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # This calls all results of the get inventory dictionary call.
    # This is not ideal
    r_all = nr.inventory.get_inventory_dict()
    # Access the groups directory results
    r = r_all["groups"]
    return jsonify(r)


# NAPALM getter functions
def get_users():
    """
    Retrieves the results of `get_users` for all hosts in the Nornir
    inventory and prepares it to preparation for consumption by
    the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    r = nr.run(task=napalm_get, getters=["users"])
    return to_json(r)


def get_facts():
    """
    Retrieves the results of `get_facts` for all hosts in the Nornir
    inventory and prepares it to preparation for consumption by
    the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    r = nr.run(task=napalm_get, getters=["facts"])
    return to_json(r)


def get_interfaces():
    """
    Retrieves the results of `get_interfaces` for all hosts in the Nornir
    inventory and prepares it to preparation for consumption by
    the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    r = nr.run(task=napalm_get, getters=["interfaces"])
    return to_json(r)


def get_interfaces_ip():
    """
    Retrieves the results of `get_interfaces_ip` for all hosts in the Nornir
    inventory and prepares it to preparation for consumption by
    the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    r = nr.run(task=napalm_get, getters=["interfaces_ip"])
    return to_json(r)


def get_ntp_servers():
    """
    Retrieves the results of `get_ntp_servers` for all hosts in the Nornir
    inventory and prepares it to preparation for consumption by
    the front end.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    r = nr.run(task=napalm_get, getters=["ntp_servers"])
    return to_json(r)


def get_facts_host(host):
    """
    Retrieves the results of `get_facts` for an individual host
    of the Nornir inventory and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    r = device.run(name="Processing facts", task=napalm_get, getters=["facts"])
    return to_json(r)


def get_users_host(host):
    """
    Retrieves the results of `get_users` for an individual host
    of the Nornir inventory and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    r = device.run(name="Processing users", task=napalm_get, getters=["users"])
        # If/Else block to validate whether the task failed or not
    if r[host].failed is True:
        # Jsonify the host and the output, send the response and status code 500
        print("Hello I'm True and I've failed")
        return to_json(r), 500
    elif r[host].failed is False:
        # Jsonify the host and the output, send the response and status code 200
        print("Hello I'm False and I've succeeded")
        return to_json(r), 200
    # return to_json(r)


def get_interfaces_host(host):
    """
    Retrieves the results of `get_interfaces` for an individual host
    of the Nornir inventory and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    r = device.run(
        name="Processing interfaces", task=napalm_get, getters=["interfaces"]
    )
    return to_json(r)


def get_interfaces_ip_host(host):
    """
    Retrieves the results of `get_interfaces_ip` for an individual host
    of the Nornir inventory and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    r = device.run(
        name="Processing IP interfaces", task=napalm_get, getters=["interfaces_ip"]
    )
    return to_json(r)


def get_getter_host(host, getter):
    """
    Retrieves the results of a supplied getter for an individual host
    of the Nornir inventory and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :param getter: The getter to be retrieved.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    r = device.run(name="Processing IP interfaces", task=napalm_get, getters=[getter])
    return to_json(r)


def genie(host, command):
    """
    Retrieves the results of an individual command for an individual host
    of the Nornir inventory using the `use_genie=True` through the
    `netmiko_send_command` and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :param command: The command to be run on the host.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    # Execute netmiko send command, using Genie
    r = device.run(
        task=netmiko_send_command,
        name="Netmiko Command (Genie)",
        command_string=command,
        use_textfsm=False,
        use_genie=True,
    )
    return to_json(r)


def n_cli(host, command):
    """
    Retrieves the results of an individual command for an individual host
    of the Nornir inventory using the `napalm_cli` function
    and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :param command: The command to be run on the host.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    # Execute napalm_cli command
    r = device.run(name="NAPALM CLI", task=napalm_cli, commands=[command])
    return to_json(r)


def textfsm(host, command):
    """
    Retrieves the results of an individual command for an individual host
    of the Nornir inventory using the `use_textfsm=True` through the
    `netmiko_send_command` and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :param command: The command to be run on the host.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    # Execute netmiko send command, using Genie
    r = device.run(
        task=netmiko_send_command,
        name="Netmiko Command (TextFSM)",
        command_string=command,
        use_textfsm=True,
        use_genie=False,
    )
    return to_json(r)


def scrapli_cmd(host, command):
    """
    TODO: Rewrite to say it's using scrapli and nornir with parse genie output
    Retrieves the results of an individual command for an individual host
    of the Nornir inventory using the `use_textfsm=True` through the
    `netmiko_send_command` and prepares it to preparation for
    consumption by the front end.
    :param host: The host which is to be queried.
    :param command: The command to be run on the host.
    :return jsonify(r): Results after they have been run through jsonify
    """
    # Initialise Nornir
    nr = get_nr()
    # Filter by the host supplied into the function
    device = nr.filter(name=str(host))
    # Execute scrapli send command
    r = device.run(task=send_command, name="Scrapli Send Command", command=command)
    # If/Else block to validate whether the task failed or not
    if r[host].failed is True:
        # Jsonify the host and the output, send the response and status code 500
        return jsonify(host=host, command_output=""), 500
    elif r[host].failed is False:
        print("Hello I'm False and I've succeeded")
        # Use genie_parse_output to parse Nornir AggregatedResult via Genie
        output = r[host].scrapli_response.genie_parse_output()
        # Jsonify the host and the output, send the response and status code 200
        return jsonify(host=host, command_output=output), 200
