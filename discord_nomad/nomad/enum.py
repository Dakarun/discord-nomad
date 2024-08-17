from enum import auto, Enum, StrEnum


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class NomadPath(Enum):
    # Allocation
    LIST_ALLOCATIONS = "/v1/allocations"
    ALLOCATION = "/v1/allocation/{alloc_id}"
    CLIENT_ALLOCATION = "/v1/client/allocation"

    # Jobs
    JOBS = "/v1/jobs"
    JOB = "/v1/job"


class NomadAllocation(StrEnum):
    # Regular
    STOP = auto()
    SERVICES = auto()
    CHECKS = auto()

    # Client
    SIGNAL = auto()
    RESTART = auto()
    EXEC = auto()
    PAUSE = auto()


class NomadJob(StrEnum):
    SUBMISSION = auto()
    VERSIONS = auto()
    ALLOCATIONS = auto()
    EVALUATIONS = auto()
    DEPLOYMENTS = auto()
    DEPLOYMENT = auto()
    SUMMARY = auto()
    DISPATCH = auto()
    REVERT = auto()
    STABLE = auto()
    EVALUATE = auto()
    PLAN = auto()
    PERIODIC_FORCE = "periodic/force"
    SCALE = auto()
    SERVICES = auto()
    ACTIONS = auto()
    ACTION = auto()
