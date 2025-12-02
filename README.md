This repository contains an example of using [fastapi] to create a web service.

[fastapi]: https://fastapi.tiangolo.com/

We're using [uv] for dependency management, so first install `uv`:

[uv]: https://github.com/astral-sh/uv

    pip install uv

And then run the example:

    uv run fastapi dev main.py

This will start the server on http://localhost:8000. All of the methods are no-op, but do take a look at the generated documentation available at http://localhost:8000/doc, which includes available paths and methods, information about data structures, etc.
