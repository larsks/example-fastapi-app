# pyright: reportIncompatibleVariableOverride=false
from pydantic import BaseModel
from pydantic import ConfigDict
from enum import StrEnum


def dash_to_underscore(name: str) -> str:
    """Converts underscores in names to dashes, since the existing
    config files seem to prefer dashes."""
    return name.replace("_", "-")


class StrictBase(BaseModel):
    model_config: ConfigDict = ConfigDict(
        extra="forbid", alias_generator=dash_to_underscore, populate_by_name=True
    )


class Response(StrictBase):
    """Base class for all HTTP responses. That means that every response will
    include the `success` and `error` fields."""

    success: bool
    error: str | None = None


class TaskStatus(StrictBase):
    job_id: int
    task_id: int
    label: str
    msg: str


class JobSummary(StrictBase):
    job_id: int
    status: str
    running_task_label: str
    pending_tasks: int = 0
    completed_tasks: int = 0
    pending_tasksailed_tasks: int = 0


class JobSummaryResponse(Response):
    data: list[JobSummary] = []


class JobStatus(StrictBase):
    job_status: str
    running_tasks: list[TaskStatus] = []
    pending_tasks: list[TaskStatus] = []
    completed_tasks: list[TaskStatus] = []
    failed_tasks: list[TaskStatus] = []
    job_error: str | None = None


class JobStatusResponse(Response):
    data: JobStatus


class TaskResult(StrictBase):
    description: str
    files: list[str] = []


class TaskResultsResponse(Response):
    data: list[TaskResult]


class JobResultsResponse(Response):
    data: dict[int, TaskResult]


class ConfigFile(StrictBase):
    pass


class TaskFileResponse(Response):
    data: str


class StringListResponse(Response):
    data: list[str] = []


class JobStart(StrictBase):
    job_id: int
    task_id: int


class JobStartResponse(Response):
    data: JobStart


class DiscoverCategory(StrEnum):
    """Using an enum lets us restrict a value to a specific list of choices. This class is used to restrict the 'category'
    parameter to the `/discover/{category}/{node}` method."""

    NETWORK = "network"
