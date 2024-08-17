from dataclasses import dataclass
from discord_nomad.nomad.clients.base import NomadBaseClient
from discord_nomad.nomad.enum import NomadPath, NomadJob, HTTPMethod


@dataclass
class NomadJobClient(NomadBaseClient):
    host: str

    def list_jobs(self):
        endpoint = NomadPath.JOBS.value
        response = self._get(endpoint)
        return response

    def get_job(self, job_id: str):
        endpoint = "/".join([NomadPath.JOB.value, job_id])
        response = self._get(endpoint)
        return response

    def submit_job(self):
        pass

    def job_versions(self):
        pass

    def job_allocations(self, job_id: str):
        endpoint = "/".join([NomadPath.JOB.value, job_id, NomadJob.ALLOCATIONS.value])
        response = self._get(endpoint)
        return response
