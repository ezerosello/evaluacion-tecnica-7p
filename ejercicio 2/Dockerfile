FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "-m", "src.main"]
