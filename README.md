# AI-SOC-Automation
### End-to-End SOC Alert Triage Automation (Splunk · N8N · GPT-4)
[![Splunk](https://img.shields.io/badge/Splunk-000000?style=for-the-badge&logo=splunk&logoColor=white)](https://www.splunk.com/) [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/) [![N8N](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) [![VirusTotal](https://img.shields.io/badge/VirusTotal-394EFF?style=for-the-badge&logo=virustotal&logoColor=white)](https://www.virustotal.com/) [![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.com/)

This project demonstrates a production-quality SOC automation designed to accelerate alert triage while maintaining consistency and quality. The system simulates a complete SOC workflow from detection through AI-assisted analysis to case management using industry standard tools and realistic attack scenarios.

---

## 🎯 Project Objective

Modern Security Operations Centers are often overwhelmed by "alert fatigue." This project provides a blueprint for:

* **Accelerating Triage:** Reducing time-to-analysis from minutes to seconds.
* **Ensuring Consistency:** Standardizing investigation quality regardless of analyst experience.
* **AI Augmentation:** Using LLMs as a "force multiplier" for structured analysis and MITRE mapping.
* **Context Preservation:** Maintaining a complete audit trail from initial telemetry to final case creation.

---

## 🛠️ Technology Stack

| Component           | Technology            | Purpose                                          |
| ------------------- | --------------------- | ------------------------------------------------ |
| **SIEM**            | Splunk Enterprise     | Event correlation and alerting                   |
| **Telemetry**       | Sysmon                | Windows endpoint monitoring & process logging    |
| **Orchestration**   | N8N                   | Workflow automation engine (Self-hosted)         |
| **AI Analysis**     | OpenAI GPT-4 mini     | Structured triage generation & technique mapping |
| **Threat Intel**    | VirusTotal, AbuseIPDB | File Hash/IP reputation and risk scoring         |
| **Case Management** | DFIR-Iris             | Investigation lifecycle and evidence tracking    |
| **Notification**    | Slack Webhooks        | Real-time analyst alerting                       |
| **Testing**         | Atomic Red Team       | Adversary emulation (T1059.001, T1027, etc.)     |

---

## 🔄 End-to-End Workflow

1. **Detection:** Splunk generates security alerts from a Windows 10 lab environment based on Sysmon telemetry.
2. **Orchestration:** N8N receives the Splunk webhook and triggers a parallel-processed workflow.
3. **Enrichment:** Simultaneous API queries to **VirusTotal** (file hashes) and **AbuseIPDB** (IP reputation).
4. **AI Analysis:** OpenAI GPT-4 processes the alert + enrichment data to generate a structured report including MITRE ATT&CK mapping and severity assessment.
5. **Case Management:** **DFIR-Iris** automatically creates an investigation case with the full enrichment context.
6. **Notification:** **Slack** delivers a real-time summary to analysts with a direct link to the DFIR-Iris case.

---

## 📸 Visual Screenshots

**1. Splunk Detection**
![Splunk Detection](screenshots/splunk-detection.png)
*Splunk search querying the mydfir-project index for Windows EventCode 4625. The results are aggregated by time, computer name, user, and source IP, clearly highlighting repeated failed authentication attempts from the same source, which is indicative of brute force activity.*

**2. N8N AI Model**
![N8N Workflow](screenshots/n8n-workflow.png)
*N8N workflow node configured to send a system prompt to an OpenAI model. It shows how alert data is passed into the AI model as structured input, forming the basis for automated analysis and triage.*

**3. VirusTotal Enrichment**
![VirusTotal Enrichment](screenshots/Virustotal.png)
*N8N HTTP Request node configured to query the VirusTotal API using predefined credentials. It demonstrates automated threat intelligence enrichment by retrieving reputation data for hashes or indicators associated with the alert*

**4. AI-Generated Triage Output**
![GPT-mini-model](screenshots/GPT-mini-model.png)
*This screenshot captures the structured AI output containing severity assessment, MITRE ATT&CK technique mapping, and recommended response actions. It reflects automated decision support designed to reduce analyst triage time.*

**5. DFIR-Iris Case Management**
![DFIR-Iris Case](screenshots/dfir-iris-case.png)
*This screenshot shows an N8N HTTP Request node sending alert details and AI-generated context to DFIR-IRIS. It illustrates automated case creation with fields such as alert title and detailed description populated dynamically from upstream analysis.*

**6. Slack Notification**
![Slack Alert](screenshots/slack-notification.png)
*Slack channel receiving a detailed security alert message. The notification includes severity, MITRE ATT&CK techniques, and response guidance, enabling analysts to quickly understand and act on the incident.*

---

## 👤 Individual Contribution

I designed and implemented this system from the ground up, focusing on the following domains:

* **Detection Engineering:** Authored custom Splunk correlation searches targeting malicious PowerShell patterns and remote file downloads.
* **Workflow Orchestration:** Built N8N automation logic with parallel execution branches and custom error recovery mechanisms.
* **Threat Intelligence Integration:** Implemented API connections with logic for rate limiting and data normalization.
* **AI Engineering:** Designed system prompts for structured JSON output and built validation scripts to ensure model reliability.
* **DevOps & Testing:** Containerized the stack using Docker Compose and validated the pipeline using **Atomic Red Team** emulation.

---

## 💡 Lessons Learned & Challenges

#### **Challenge: AI Output Reliability**

**Problem:** Raw LLM outputs can be "chatty" or fail to follow JSON schemas, breaking downstream automation (Slack/Iris).
**Solution:** Implemented a multi-layer validation script (`json_validator.py`) that checks for required fields and cross-references suggested MITRE techniques against a known valid list.

#### **Challenge: Webhook & API Resilience**

**Problem:** High-volume alerts or API downtime can cause data loss or duplicate case creation.
**Solution:** Designed **idempotency controls** to prevent duplicate cases for the same alert and added a **webhook recovery workflow** to retry failed deliveries.

#### **Challenge: Operational Observability**

**Problem:** Identifying where a failure occurred in a multi-step pipeline is difficult without logging.
**Solution:** Implemented logging at every workflow stage, allowing for performance monitoring and quick debugging of failed API calls.

---

## ⚡ Technical Highlights

* **Production Reliability:** Features multi-layer AI output validation and retry logic.
* **Cost Optimization:** Implemented response caching and token-efficient prompting to reduce API costs.
* **Adversary Emulation:** Validated against real-world TTPs (Encoded PowerShell, Download Cradles).
* **No-Code/Low-Code Hybrid:** Demonstrates how to extend N8N with custom Python scripts for advanced logic.

---

## 📁 Repository Structure

```text
ai-soc-automation/
├── README.md
├── docker-compose.yml
├── .env.example
├── detections/
│   └── windows-authentication/
│       ├── brute-force-4625.spl
│       └── README.md
├── workflows/
│   ├── splunk-webhook.json
│   ├── ai-triage.json
│   ├── virustotal-enrichment.json
│   └── dfir-iris-case-create.json
├── scripts/
│   ├── json_validator.py
│   ├── rate_limiter.py
│   └── utils.py
├── investigations/
│   └── windows-bruteforce-authentication/
│       ├── README.md
│       ├── timeline.md
│       ├── iocs.md
│       └── splunk-queries.md
├── screenshots/
│   └── *.png
└── docs/
    ├── architecture.md
    ├── deployment.md
    └── troubleshooting.md
```

---

## 🚀 Quick Start

1. **Clone the Repo:**
   `git clone https://github.com/yourusername/ai-soc-automation.git`
2. **Configure Environment:**
   `cp .env.example .env` (Add your VirusTotal, AbuseIPDB, and OpenAI keys).
3. **Spin up Stack:**
   `docker-compose up -d`
4. **Initialize:** Import Splunk detections and N8N workflows found in the `/workflows` and `/detections` folders.
5. **Test:** Execute an Atomic Red Team test on a Windows host.

---


