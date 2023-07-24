# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker/54763270#54763270

# :tyranno: FROM python:${project.requires-python~.semver_max(@).semver_minor(@)~}
FROM python:3.11

# --------------------------------------
# ------------- Set labels -------------

# See https://github.com/opencontainers/image-spec/blob/master/annotations.md
# :tyranno: LABEL org.opencontainers.image.version="${project.version}"
LABEL org.opencontainers.image.version="1.0.0-0"
# :tyranno: LABEL org.opencontainers.image.vendor="${tool.tyranno.data.vendor}"
LABEL org.opencontainers.image.vendor="dmyersturnbull"
# :tyranno: LABEL org.opencontainers.image.title="${project.name}"
LABEL org.opencontainers.image.title="tyranno"
# :tyranno: tool.poetry.version= 0.11.0
LABEL org.opencontainers.image.version="1.0.0-0"
# :tyranno: LABEL org.opencontainers.image.url="${project.urls.homepage}"
LABEL org.opencontainers.image.url="https://github.com/dmyersturnbull/tyranno"
# :tyranno: LABEL org.opencontainers.image.documentation="${project.urls.docs}"
LABEL org.opencontainers.image.documentation="https://github.com/dmyersturnbull/tyranno"


# --------------------------------------
# ---------- Copy and install ----------

# ENV no longer adds a layer in new Docker versions,
# so we don't need to chain these in a single line
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=120

# Install system deps
# :tyranno: RUN pip install '${build-system.requires~[?contains('poetry-core')]~}'
RUN pip install 'hatchling~=1.7'

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY pyproject.toml /app/

RUN pip install .

# Copy to workdir
COPY . /app

CMD tyranno --help
