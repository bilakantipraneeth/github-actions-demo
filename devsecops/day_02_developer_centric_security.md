# Day 2 (Module 2): Developer-Centric Security (Detailed Theory)

---

### **Part 1: A Deep Dive into the OWASP Top 10 (2021 Edition)**

The OWASP (Open Web Application Security Project) Top 10 is the most respected and widely-used awareness document for web application security. It represents a broad consensus about the most critical security risks facing web applications.

---

#### **A01:2021 - Broken Access Control**

**1. What It Is:** This occurs when an application fails to properly enforce restrictions on what authenticated users are allowed to do, allowing them to access data or perform actions outside of their intended permissions.

**2. Real-World Breach Example: The Capital One Breach (2019):** A misconfigured Web Application Firewall (a form of broken access control on infrastructure) allowed an attacker to send a specially crafted request that granted them elevated privileges. This allowed them to access and exfiltrate the personal and financial data of over 100 million customers.

**3. Mitigation:** Enforce access control checks on the server side for every single request. Deny by default. Never rely on the client-side to enforce security.

---

#### **A02:2021 - Cryptographic Failures**

**1. What It Is:** Failures in protecting data, both "at rest" (stored) and "in transit" (over the network). This often leads to the exposure of sensitive data like passwords and personal information.

**2. Real-World Breach Example: The LinkedIn Breach (2012):** Attackers stole 6.5 million user password hashes. The passwords were not "salted" (a unique random string added to each password before hashing), which made them much easier to crack with pre-computed "rainbow tables."

**3. Mitigation:** Use strong, modern encryption (AES-256). For passwords, use a strong, slow, and salted hashing algorithm like **Argon2**, scrypt, or bcrypt. Enforce TLS for all data in transit.

---

#### **A03:2021 - Injection**

**1. What It Is:** Occurs when an application allows untrusted user data to be interpreted and executed as part of a command or query (e.g., SQL Injection).

**2. Real-World Breach Example: The TalkTalk Breach (2015):** A UK telecommunications company was the victim of a basic SQL Injection attack. The attacker stole the personal and financial details of nearly 157,000 customers, leading to a record £400,000 fine.

**3. Mitigation:** Use safe, **parameterized queries** (prepared statements). This separates data from commands, preventing the database from interpreting user input as part of the command.

---

#### **A04:2021 - Insecure Design**

**1. What It Is:** Flaws in the logic and architecture of an application that cannot be fixed by patching a single line of code. It represents a fundamental weakness in how the system was planned.

**2. Real-World Use Case (Business Logic Flaw):** An airline website allows a user to book a flight at full price and then, in a separate step, apply a discount coupon to the already-booked ticket, receiving a cash refund. The design of the interaction between the two features is insecure.

**3. Mitigation:** Use **Threat Modeling** during the design phase to brainstorm what could go wrong. Use secure design patterns and write explicit security requirements.

---

#### **A05:2021 - Security Misconfiguration**

**1. What It Is:** Security settings being configured incorrectly or left in an insecure default state. This can happen at any level of the application stack.

**2. Real-World Breach Example: Magellan Health Breach (2020):** A misconfigured cloud server allowed attackers to gain access, leading to a ransomware attack and the theft of data from 365,000 patients.

**3. Mitigation:** Use Infrastructure as Code (IaC) scanners (like **Checkov**) to automatically detect misconfigurations. Follow industry-standard hardening guides and do not use default credentials.

---

#### **A06:2021 - Vulnerable and Outdated Components**

**1. What It Is:** Using third-party software components (libraries, frameworks) that have known security vulnerabilities. Also known as "software supply chain" risk.

**2. Real-World Breach Example: The Equifax Breach (2017):** Caused entirely by Equifax failing to update a vulnerable version of the Apache Struts web framework. Attackers exploited the known vulnerability to steal the data of 147 million people.

**3. Mitigation:** Use **Software Composition Analysis (SCA)** tools (like **Trivy**) to automatically scan all project dependencies for known vulnerabilities. Maintain a patch management process.

---

#### **A07:2021 - Identification and Authentication Failures**

**1. What It Is:** Failures related to confirming a user's identity and managing their sessions, including weak password policies and insecure session management.

**2. Real-World Breach Example: Credential Stuffing Attacks:** Attackers take username/password lists from one breach (e.g., LinkedIn) and try them on other websites. Because people reuse passwords, these attacks are highly successful.

**3. Mitigation:** Implement **Multi-Factor Authentication (MFA)**. Enforce strong password policies. Invalidate sessions on logout and after inactivity.

---

#### **A08:2021 - Software and Data Integrity Failures**

**1. What It Is:** Failures related to verifying the integrity of software and data, particularly in CI/CD pipelines and auto-update mechanisms.

**2. Real-World Breach Example: The SolarWinds Attack (2020):** Attackers breached SolarWinds' build server and injected malicious code into an update. SolarWinds then digitally signed this malicious update and shipped it to customers. Because it was legitimately signed, it was trusted and installed, giving attackers a backdoor into thousands of organizations.

**3. Mitigation:** Use digital signatures to verify the integrity of all software. Secure your CI/CD pipeline with strong access controls and auditing.

---

#### **A09:2021 - Security Logging and Monitoring Failures**

**1. What It Is:** The lack of adequate logging, monitoring, and response capabilities to detect and react to an attack.

**2. Real-World Breach Example: The Equifax Breach (2017) - The Aftermath:** Forensic analysis revealed attackers were active inside Equifax's network for **76 days** before being discovered. Critical alerts from security tools were not properly investigated, giving attackers months of unfettered access.

**3. Mitigation:** Log all critical security events (logins, access control failures, etc.). Centralize logs and configure automated alerts for suspicious patterns. Have an incident response plan.

---

#### **A10:2021 - Server-Side Request Forgery (SSRF)**

**1. What It Is:** A vulnerability that allows an attacker to force a server to make network requests on their behalf, often to internal, non-public services.

**2. Real-World Breach Example: The Capital One Breach (2019) - The Entry Point:** The attacker used an SSRF vulnerability to force a public-facing server to make requests to the internal AWS metadata service. This allowed them to retrieve temporary cloud credentials, which they used to access the customer data.

**3. Mitigation:** Sanitize and validate all user-supplied URLs. Use an allow-list of permitted domains for the server to connect to. Use firewall rules to block requests to internal metadata services.

---

### **Part 2: Secure Design Principles (Detailed)**

These are proactive, fundamental concepts that prevent entire classes of vulnerabilities from being created.

*   **Principle of Least Privilege (PoLP):** Grant any entity only the absolute minimum permissions necessary to perform its function. This contains damage if the entity is compromised.
*   **Defense in Depth:** Implement multiple, overlapping, and diverse security controls. Assume any single control can fail.
*   **Fail-Secure:** When a system encounters an error, it should default to a secure state (i.e., deny access).
*   **Separation of Duties:** A critical task cannot be completed by a single person; it requires two or more individuals to prevent fraud and error.
*   **Keep It Simple (KISS):** Complexity is the enemy of security. Simpler systems have a smaller attack surface and are easier to audit and secure.
*   **Zero Trust Architecture:** A modern model based on the philosophy: "Never trust, always verify." Every request must be authenticated and authorized, regardless of its origin.

---

### **Part 3: A Deep Dive into Automated Security Tooling**

Automation is the engine of DevSecOps. These tools help us scale security and provide rapid feedback.

*   **Pre-Commit Hooks:** Scripts that run on a developer's machine to block commits containing obvious mistakes, like API keys. This is the "far-left" of shifting left.
*   **Static Application Security Testing (SAST):** "White-box" testing that analyzes source code from the inside-out without running it. It finds vulnerable patterns in the code itself. (e.g., SonarQube, Checkmarx).
*   **Software Composition Analysis (SCA):** Identifies all third-party components in an application and checks them against a database of known vulnerabilities. (e.g., Trivy, Snyk).
*   **Dynamic Application Security Testing (DAST):** "Black-box" testing that attacks a *running* application from the outside-in, simulating real-world attacks. (e.g., OWASP ZAP, Burp Suite).

A mature DevSecOps program uses a combination of all these tools at different stages of the lifecycle.
