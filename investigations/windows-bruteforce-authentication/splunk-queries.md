# Splunk Investigation Queries

This document contains the Splunk searches used during the investigation to
validate the brute force authentication alert and scope potential impact.

---

## 1. Confirm Repeated Failed Logons (EventCode 4625)

    index=mydfir-project EventCode=4625
    | stats count AS failures by _time, ComputerName, user, src_ip
    | sort - failures

---

## 2. Pivot on Source IP Observed in Alert

    index=mydfir-project IpAddress="69.74.29.21" (EventCode=4625 OR EventCode=4624)
    | stats count by EventCode, ComputerName,  user

---

## 3. Check for Successful Logons from Same Source IP

    index=mydfir-project EventCode=4624 IpAddress="69.74.29.21"
    | table _time, ComputerName,  user, LogonType, src_ip
    | sort - _time

---

## 4. Identify Targeted Accounts and Hosts

    index=mydfir-project EventCode=4625
    | stats count AS failures by ComputerName, user, src_ip
    | sort - failures
