FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/engine/.venv/bin:$PATH"

WORKDIR /engine

RUN groupadd -r appuser && useradd -r -g appuser -s /usr/sbin/nologin appuser

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY --chown=appuser:appuser . .

USER appuser

CMD ["python", "main.py"]