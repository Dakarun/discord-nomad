from dataclasses import dataclass
from discord_nomad.nomad.clients import NomadAllocationClient, NomadJobClient

@dataclass
class NomadClient(NomadAllocationClient, NomadJobClient):
    host: str
