
FROM mcr.microsoft.com/playwright/python:v1.46.0-focal

WORKDIR /app
COPY . .
RUN python -m pip install -U pip &&         if [ -f requirements.txt ]; then pip install -r requirements.txt; fi &&         python -m pip install pytest httpx pyyaml

CMD ["pytest", "-q", "--ai-triage"]
