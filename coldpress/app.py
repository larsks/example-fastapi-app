# pyright: reportUnusedCallResult=false

import os
import fastapi
from pathlib import Path

from . import models


class ColdpressApi:
    root_dir: Path

    def __init__(self, root_dir: str | Path | None = None):
        if not root_dir:
            root_dir = os.getcwd()

        self.root_dir = Path(root_dir)

    def list_examples(self) -> list[str]:
        search_path = self.root_dir / "examples"
        examples = [path.name for path in search_path.iterdir() if path.is_dir()]
        return examples


class ColdpressApp:
    api: ColdpressApi

    def __init__(self, api: ColdpressApi):
        self.api = api

    def add_routes(self, app: fastapi.FastAPI):
        app.get("/job")(self.list_jobs)
        app.get("/job/{job}")(self.job_status)
        app.get("/job/{job}/config")(self.job_config)
        app.get("/job/{job}/results")(self.job_results)
        app.get("/job/{job}/results/{task}")(self.task_results)
        app.get("/job/{job}/results/{task}/file/{filename}")(self.task_file)
        app.get("/example")(self.list_examples)
        app.get("/node")(self.list_nodes)

        app.post("/discover/{category}/{node}")(self.discover)
        app.post("/example/{example}/launch")(self.launch_example)

    def list_nodes(self) -> models.StringListResponse:
        pass

    def list_jobs(self) -> models.JobSummaryResponse:
        pass

    def job_status(self, job: int) -> models.JobStatusResponse:
        pass

    def job_config(self, job: int) -> models.ConfigFile:
        pass

    def job_results(self, job: int) -> models.JobResultsResponse:
        pass

    def task_results(self, job: int, task: int) -> models.TaskResultsResponse:
        pass

    def task_file(self, job: int, task: int, filename: str) -> models.TaskFileResponse:
        pass

    def discover(
        self, category: models.DiscoverCategory, node: int
    ) -> models.JobStartResponse:
        pass

    def list_examples(self) -> models.StringListResponse:
        try:
            return models.StringListResponse(
                success=True, data=self.api.list_examples()
            )
        except Exception as err:
            return models.StringListResponse(success=False, error=str(err))

    def launch_example(self, example: str) -> models.JobStartResponse:
        pass


app = fastapi.FastAPI()
cp = ColdpressApp(ColdpressApi())
cp.add_routes(app)
