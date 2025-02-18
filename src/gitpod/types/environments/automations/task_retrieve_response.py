# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel
from ...shared.task import Task

__all__ = ["TaskRetrieveResponse"]


class TaskRetrieveResponse(BaseModel):
    task: Task
