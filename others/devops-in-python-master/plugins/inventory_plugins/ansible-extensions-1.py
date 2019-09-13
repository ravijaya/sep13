"""a sample python plugin"""

import json
from ansible.plugins.inventory import BaseInventoryPlugin

server = dict()
server['name'] = ['localhost']

class InventoryModule(BaseInventoryPlugin):
    """an inventory module"""
    NAME = 'myplugin'

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        try:
            with open(path) as fpin:
                data = json.loads(fpin.read())
        except ValueError as exc:
            raise Exception(exc)

        for host in data:
            self.inventory.add_host(server['name'])
