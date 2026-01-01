## Splunk Investigation Queries

### 1) Confirm repeated failed logons (EventCode 4625)
```spl
index=mydfir-project EventCode=4625
| stats count as failures by _time, ComputerName, user, src_ip
| sort - failures
