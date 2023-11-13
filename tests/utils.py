import json
import shutil
import sqlite3
import pandas as pd


path_db = "tests/oc-lettings-site-tests.sqlite3"
path_json = "tests/datas_json/"


def data_transfer_to_json(src):
    """
    Transfer datas from source tables in sqlite3 and save to json.
    """
    # Extract from table source :
    con = sqlite3.connect(path_db)
    data = pd.read_sql_query(f"SELECT * FROM {src}", con)
    con.close()

    # JSON naming
    name = src
    new = name.split('_')
    new_name = new[-1]
    json_file = path_json + f'{new_name}.json'

    # Transform and save to JSON
    data.to_json(json_file, indent=4, orient='records')

def load_address(requested_address):
    # Parse the JSON data into a Python dictionary  
    addresses = json.loads(requested_address)  
    for address in addresses:
        if address['street'] == input:
            return address
    return None


data_transfer_to_json('lettings_address')
data_transfer_to_json('profiles_profile')
data_transfer_to_json('lettings_letting')