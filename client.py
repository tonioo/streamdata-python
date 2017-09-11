"""Streamdata.io demo."""

import collections
import json

import jsonpatch
import requests
import sseclient
from terminaltables import AsciiTable

SD_TOKEN = "[YOUR_STREAMDATAIO_APP_TOKEN]"
DEMO_API = "http://stockmarket.streamdata.io/v2/prices"
URL = (
    "https://streamdata.motwin.net/{}?X-Sd-Token={}".format(DEMO_API, SD_TOKEN)
)


def print_table(data):
    """Print data as a table."""
    table_data = []
    for item in data:
        item = collections.OrderedDict(
            sorted(item.items(), key=lambda t: t[0]))
        if len(table_data) == 0:
            table_data.append(item.keys())
        table_data.append(item.values())
    table = AsciiTable(table_data)
    print(table.table)


def run():
    """Launch client."""
    with requests.get(URL, stream=True) as response:
        client = sseclient.SSEClient(response)
        for event in client.events():
            if event.event == "data":
                print("Data event received")
                data = json.loads(event.data)
                print_table(data)
            elif event.event == "patch":
                print("Patch event received")
                patch = jsonpatch.JsonPatch.from_string(event.data)
                patch.apply(data, in_place=True)
                print_table(data)
            elif event.event == "error":
                print("Error: {}".format(event.data))
                response.close()
            else:
                print("Unhandled event received.")
                response.close()

if __name__ == "__main__":
    run()
