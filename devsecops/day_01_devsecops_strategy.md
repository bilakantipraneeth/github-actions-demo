# Day 1: DevSecOps Strategy & Governance (Module 1 Review)

This document summarizes the key concepts covered in the first module of our DevSecOps course.

---

### **1. The Business Case for DevSecOps**

This section answers the question: "Why should a company care about DevSecOps?"

*   **The Problem:** Traditional security happens at the end of development, which is slow and expensive.
*   **The Solution (Business Value):** DevSecOps integrates security into every step, providing clear benefits:
    *   **Reduced Cost:** It's cheaper to fix bugs found early.
    *   **Increased Speed:** Eliminates long, manual security reviews that delay releases.
    *   **Reduced Risk:** Continuously finding and fixing flaws makes a successful cyberattack less likely.

**Key Takeaway:** DevSecOps helps a business deliver safer software, faster and cheaper.

---

### **2. Key Security Frameworks**

This section answers: "Where do we start? What's our plan?"

*   **The Problem:** Doing security without a plan leads to gaps.
*   **The Solution (Frameworks):** We use expert-created frameworks to provide a blueprint.
    *   **NIST SSDF:** A **checklist** from a government authority that tells you *what* to do.
    *   **OWASP SAMM:** A **step-by-step To-Do list generator** that assesses your current security level and gives you a concrete plan to improve.

**Key Takeaway:** Frameworks give you a structured, proven plan for your security program.

---

### **3. Threat Modeling with STRIDE**

This was our first hands-on lab, answering: "How can we find security flaws before we even write any code?"

*   **The Problem:** Many security flaws are in the application's *design*, not just the code.
*   **The Solution (Threat Modeling):** We analyze the design to predict how an attacker might break it.
    *   **STRIDE** is a brainstorming tool to think of different threat types:
        *   **S**poofing (impersonation)
        *   **T**ampering (unauthorized modification)
        *   **R**epudiation (denying an action)
        *   **I**nformation Disclosure (data leaks)
        *   **D**enial of Service (making the app unavailable)
        *   **E**levation of Privilege (gaining extra powers)

**Key Takeaway:** Threat modeling helps us build a more secure design from the very beginning.
