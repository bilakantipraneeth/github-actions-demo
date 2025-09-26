# Day 7 (Module 7): Security Observability & Response (Detailed Theory)

---

### **Part 1: From Logging & Monitoring to Observability**

This represents an evolution in understanding system state.

*   **1. Logging:** The foundation. The act of recording discrete, timestamped events (e.g., "User 'alice' logged in"). Logs are the raw evidence.

*   **2. Monitoring:** The action of analyzing logs to watch for pre-defined patterns. It answers *known questions* (e.g., "Is CPU usage above 90%?").

*   **3. Observability:** The ability to ask *new questions* of your system without needing to ship new code. It's about having such rich data (logs, metrics, traces) that you can explore and understand unpredictable failure modes. It allows you to debug "unknown-unknowns."

--- 

### **Part 2: Designing a Logging Strategy (What to Log)**

The goal is to collect enough data to reconstruct the timeline of a security incident.

*   **Key Data Sources to Log:**
    *   **Cloud Provider Logs (CRITICAL):** In GCP, this is **Cloud Audit Logs**, which records every authenticated API call made in your project.
    *   **Application Logs:** Your application's own structured (e.g., JSON) output.
    *   **Web Server & Load Balancer Logs:** Access and error logs.
    *   **Operating System Logs:** Linux `syslog` or Windows Event Logs.
    *   **Network Logs:** GCP VPC Flow Logs and Firewall logs.

*   **A Good Security Log Event Answers the "5 W's":**
    *   **Who:** The user or service principal.
    *   **What:** The action performed.
    *   **When:** A precise timestamp.
    *   **Where:** The source IP and the resource acted upon.
    *   **Outcome:** Success or failure.

---

### **Part 3: Centralized Logging & SIEM Architecture**

Logs must be collected into a central platform for analysis.

*   **Centralized Logging Architecture (e.g., ELK Stack):**
    *   **Analogy:** A city's water system, collecting logs (wastewater) from individual servers (houses) and sending them to a central plant (logging platform) for analysis.
    *   **Components:** Log Shippers (e.g., Filebeat) -> Log Processor (e.g., Logstash) -> Storage & Search (e.g., Elasticsearch) -> Visualization (e.g., Kibana).
    *   **GCP Equivalent:** Google Cloud's operations suite (Cloud Logging, Monitoring, Trace).

*   **What is a SIEM?**
    *   **Definition:** A Security Information and Event Management system. It's a centralized logging platform with a security intelligence layer on top.
    *   **Key Feature (Correlation):** A SIEM's primary job is to automatically **correlate** seemingly unrelated events from different log sources to find attack patterns.
    *   **Use Case:** A SIEM correlates a firewall alert from a malicious IP, a series of failed web logins, and a successful user login from an unusual country into a single, high-priority incident: "Suspected brute-force attack followed by impossible travel login."

---

### **Part 4: Introduction to Incident Response (IR)**

*   **Definition:** An organization's process for responding to and managing the aftermath of a security breach.

*   **The IR Lifecycle (based on the NIST standard):**
    1.  **Preparation:** The work done *before* an incident: creating the plan, training the team, preparing tools.
    2.  **Detection & Analysis:** Identifying that an incident is happening and analyzing its scope and severity.
    3.  **Containment:** Stopping the attack from spreading. Isolating affected systems, blocking IPs, disabling user accounts.
    4.  **Eradication:** Removing the threat from the environment (e.g., removing malware, patching the vulnerability).
    5.  **Recovery:** Restoring affected systems to normal operation, often from clean backups or IaC templates.
    6.  **Post-Incident Activity (Lessons Learned):** The most important step. Conducting a blameless post-mortem to understand the root cause and improve defenses to prevent the same attack from happening again.
