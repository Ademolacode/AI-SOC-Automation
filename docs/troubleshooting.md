# Troubleshooting Guide

This document outlines common issues encountered during testing and validation.

## n8n Webhook Not Triggering

- Verify the webhook path matches the Splunk alert action.
- Confirm n8n is reachable from the Splunk environment.
- Check n8n execution logs for rejected requests.

## AI Output Formatting Issues

- Ensure the AI prompt enforces structured output.
- Validate responses before sending data to Slack or DFIR-IRIS.
- Review JSON validation logic if workflows fail unexpectedly.

## API Rate Limiting or Failures

- Confirm API keys are valid and active.
- Review rate limit headers from VirusTotal and AbuseIPDB.
- Implement delays or retries where required.

## DFIR-IRIS Case Creation Failures

- Validate API endpoint and authentication configuration.
- Confirm required fields are present in the request payload.
- Check DFIR-IRIS server logs for rejected requests.

## Slack Notifications Not Delivered

- Verify webhook URL configuration.
- Check message size and formatting.
- Review n8n execution logs for delivery errors.
