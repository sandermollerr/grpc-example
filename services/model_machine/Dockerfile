###############################################
# Base Image
###############################################
FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1  \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/app" \
    VENV_PATH="/opt/app/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV PYTHONPATH="$PYSETUP_PATH"


###############################################
# Builder Image
###############################################
FROM base as build

#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt-get update && apt-get -y install musl-dev curl build-essential python-dev3.12
RUN apt-get update && apt-get -y install musl-dev curl build-essential
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY libraries/grpc /libraries/grpc
COPY services/model_machine/poetry.lock ./
COPY services/model_machine/pyproject.toml  ./

RUN poetry install


###############################################
# Runtime Image
###############################################
FROM base as runtime

COPY --from=build $PYSETUP_PATH $PYSETUP_PATH
COPY services/model_machine/src ./src
COPY services/model_machine/resources ./resources

ENTRYPOINT ["python"]
CMD ["src/main.py"]


