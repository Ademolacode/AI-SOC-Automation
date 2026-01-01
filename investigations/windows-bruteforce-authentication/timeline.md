## Investigation Timeline (UTC)

| Time (UTC) | Stage | What Happened |
|---|---|---|
| 26/12/2025 16:40:01 | Detection / Case Intake | DFIR-IRIS triage record created for brute force alert involving host "mydfir" and user "mydfir" |
| 26/12/2025 16:40–16:41 | SIEM Evidence | Splunk detection shows repeated EventCode 4625 failures from the same source IP |
| 26/12/2025 16:41–16:42 | Enrichment | AbuseIPDB enrichment confirms high confidence malicious reputation for the source IP |
| 26/12/2025 16:41–16:42 | Enrichment | VirusTotal enrichment flags the file hash as malicious and associated with trojan/RAT behavior |
| 26/12/2025 16:42–16:43 | Assessment | MITRE techniques mapped and severity rated as Critical based on brute force plus confirmed malware |
| 26/12/2025 16:43–16:45 | Response Guidance | Containment and investigation actions documented (block IP, isolate host, scan, hunt for persistence) |
