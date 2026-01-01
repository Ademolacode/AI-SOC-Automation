# Deployment Guide

This project is designed to run in a local lab or test environment.

## Prerequisites

- Docker and Docker Compose
- Splunk Enterprise or Splunk Free
- n8n (self-hosted)
- API keys for:
  - OpenAI
  - VirusTotal
  - AbuseIPDB
  - Slack Webhook
  - DFIR-IRIS

## Deployment Steps

1. Clone the repository:
   git clone https://github.com/yourusername/ai-soc-automation.git

2. Configure environment variables:
   cp .env.example .env

3. Start the orchestration services:
   docker-compose up -d

4. Import automation components:
   - Import Splunk detections from the `detections/` directory
   - Import n8n workflows from the `workflows/` directory

5. Configure webhooks and credentials inside n8n.

6. Validate deployment:
   - Generate test authentication failures
   - Confirm alert ingestion in n8n
   - Verify case creation and Slack notification

## Version Notes

Some versions of n8n may introduce breaking changes.
A pinned version is defined in `docker-compose.yml` for stability.
