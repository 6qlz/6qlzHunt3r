# 6qlzHunt3r - Advanced Bug Bounty Scanner  

## Description  
6qlzHunt3r is an advanced AI automated security scanner designed to assist security researchers, penetration testers, and bug bounty hunters in identifying vulnerabilities in web applications.  
It automates reconnaissance, enumeration, and exploitation using cutting-edge scanning techniques, helping researchers find critical security flaws efficiently.  

This tool integrates with **ProjectDiscovery's Nuclei**, enabling precise vulnerability detection using structured templates. It also supports custom wordlists and payloads, allowing users to tailor scans based on specific testing needs.  

## Features  
- Automated scanning for various vulnerabilities, including:  
  - SQL Injection (SQLi)  
  - Cross-Site Scripting (XSS)  
  - Server-Side Request Forgery (SSRF)  
  - Local File Inclusion (LFI)  
  - Remote File Inclusion (RFI)  
  - Command Injection (RCE)  
  - Web Cache Poisoning  
  - Host Header Injection  
  - Security Misconfigurations  
  - Hardcoded Credentials  
  - Insecure Deserialization  
  - IDOR (Insecure Direct Object References)  
  - XXE (XML External Entity Injection)  
- Integration with **Nuclei** for structured vulnerability scanning  
- Supports **custom wordlists and payloads** for fuzzing  
- Generates **detailed reports** for discovered vulnerabilities  
- Fast and automated scanning workflow  
- Simple interactive CLI menu  

---

## Authentication Setup  
6qlzHunt3r requires authentication with **ProjectDiscovery Cloud API** to function properly.  

### How to Authenticate  
1. Visit [ProjectDiscovery Cloud](https://cloud.projectdiscovery.io) and create a free account.  
2. Generate a new API key from the **API Access** section.  
3. Run ``nuclei -auth`` command in your terminal:  

## Clone the Repository  

``git clone https://github.com/6qlz/6qlzHunt3r.git``
``cd 6qlzHunt3r``
``pip install -r requirements.txt``

## Disclaimer
 This tool is intended for educational and authorized security research purposes only. Unauthorized testing on systems without explicit permission is illegal and may result in legal consequences.
