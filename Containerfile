FROM ghcr.io/astral-sh/uv:python3.14-alpine

WORKDIR /app/
COPY pyproject.toml uv.lock ./
RUN uv sync
COPY ./ ./

ENV UV_NO_CACHE=1
CMD ["uv", "run", "--no-sync", "uvicorn", "--host", "0.0.0.0", "coldpress.app:app"]
