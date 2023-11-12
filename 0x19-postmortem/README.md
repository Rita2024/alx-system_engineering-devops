## postmortem : Web Servuce Outage Incident
By: Rita Ejezie

## Issue Summary:

# Duration:
* Start Time: October 10, 2023, 14:00 UTC
* End Time: October 11, 2023, 02:00 UTC

# Impact:
* Web service outage affecting 30% of users
* Users experienced slow page loading and intermittent errors

# Root Cause:
* Database connection pool exhaustion due to a misconfiguration

## Timeline:

# Detection:
* October 10, 2023, 14:30 UTC
* Automated monitoring alerted the team to increased error rates and latency.

# Actions:
* Investigated frontend and backend components for anomalies.
* Assumed high traffic as the cause initially and scaled resources.

# Misleading Paths:
* Explored potential DDoS attack scenarios.
* Investigated CDN and DNS configurations.

# Escalation:
* Escalated to the database team when initial efforts didn't resolve the issue.

# Resolution:
* Identified misconfigured database connection pool settings.
* Adjusted connection pool parameters to prevent exhaustion.
* Stabilized services by restarting affected components.

## Root Cause and Resolution:

# Root Cause:
* Misconfigured database connection pool settings led to connections not being released properly, causing exhaustion over time.

# Resolution:
* Modified database connection pool parameters to ensure proper recycling of connections.
* Implemented additional monitoring to detect abnormal connection pool behavior.

## Corrective and Preventative Measures:

# Improvements/Fixes:
* Conduct a comprehensive review of system configurations to identify and rectify potential misconfigurations.
* Enhance monitoring to proactively detect and alert on database connection pool issues.

# Tasks:
* Implement regular configuration audits to catch potential issues before they impact services.
* Conduct a thorough review of the incident with the team to share learnings and prevent similar misconfigurations.
* Develop and document a protocol for handling misconfigurations promptly.
* Enhance documentation related to database connection pool settings for better visibility and understanding.


This incident highlighted the importance of continuous monitoring and the need for a systematic approach to troubleshooting. By implementing the outlined corrective and preventative measures, we aim to strengthen our system's resilience and minimize the risk of similar issues in the future. Our commitment to learning from incidents is crucial in maintaining a robust and reliable web infrastructure.
