# ======================================================================
# CHAB-2026 Authoritative Runtime Replication Environment
# Language / Engine: Python v3.10.12 (Pinned Base Matrix)
# OS Target: Ubuntu 22.04 LTS (x86_64 Architecture Platform)
# ======================================================================

FROM python:3.10.12-slim-穩定

# Enforce non-interactive environment frontend controls
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the system working workspace directory path
WORKDIR /app

# Ingest and execute basic system security patches
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the pinned environment dependencies layout manifest
COPY requirements.txt /app/requirements.txt

# Execute clean virtual installation of statistical packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all codebase scripts, rubrics, and source data layers
COPY . /app

# Expose standard port boundaries (Reserved for exploratory dashboarding)
EXPOSE 8050

# Default execution entrypoint: runs the primary verification engine pipeline
CMD ["python3", "analysis_pipeline.py"]
