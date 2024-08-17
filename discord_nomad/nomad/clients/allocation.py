from dataclasses import dataclass
from discord_nomad.nomad.clients.base import NomadBaseClient
from discord_nomad.nomad.enum import NomadPath, NomadAllocation, HTTPMethod


@dataclass
class NomadAllocationClient(NomadBaseClient):
    host: str

    def list_allocations(self):
        endpoint = NomadPath.LIST_ALLOCATIONS.value
        response = self._get(endpoint)
        return response

    def stop_allocation(self, alloc_id: str):
        pass

    def allocation_services(self, alloc_id: str):
        pass

    def allocation_checks(self, alloc_id: str):
        pass

    def signal_allocation(self, alloc_id: str):
        pass

    def restart_allocation(self, alloc_id: str, task_name: str = ""):
        base_endpoint = NomadPath.CLIENT_ALLOCATION.value
        op = NomadAllocation.RESTART.value
        endpoint = "/".join([base_endpoint, alloc_id, op])
        payload = None
        if task_name:
            payload = {"TaskName": task_name}
        response = self._post(endpoint, payload)
        return response

    def exec_allocation(self, alloc_id: str):
        pass

    def pause_allocation(self, alloc_id: str):
        pass
