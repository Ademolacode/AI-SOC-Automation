## Windows Brute Force Authentication Detection

This detection identifies repeated failed authentication attempts using
Windows Security EventCode 4625.

### Detection Logic
- Aggregates failed login attempts by source IP.
- Triggers when failures exceed a defined threshold.

### Required Fields
- ComputerName
- User
- Source IpAddress
- EventCode

### Common False Positives
- Misconfigured services.
- Vulnerability scanners.
- Password sync failures.
