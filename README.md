# 🔐 Cryptographic Methods for Sensitive Data Protection in a Simulated IoT Network

**Course:** CTEC 445.101 – Cybersecurity Foundations  
**Institution:** Bowie State University  
**Authors:** Aniyah Hall & Sanchez Salvador  
**Semester:** Fall 2024  
**Completion Date:** March 2024  
**Status:** ✅ Completed

---

## 🧠 Project Overview

This project explores advanced **cryptographic methods** to protect sensitive data in a **simulated Internet of Things (IoT) network**. Given the rise in cyberattacks on healthcare and smart systems, our objective was to test and implement **privacy-preserving techniques** tailored to the unique demands of IoT devices.

Through real-world case studies, simulated environments, and security tool testing, we identified the **most effective encryption and access control methods** for safeguarding data in interconnected systems.

---

## 🔍 Problem Statement

Traditional cryptographic protocols struggle to protect IoT networks due to limited device processing power and the complexity of large-scale encryption. As IoT adoption expands—especially in healthcare and industrial systems—ensuring **data confidentiality, integrity, and availability** is critical.

This project evaluates which cryptographic strategies provide the most robust protection for IoT-based environments, using both academic research and implementation-based testing.

---

## 🌐 Case Study

We examined the **Target data breach (2013)** and healthcare IoT vulnerabilities to demonstrate the importance of multi-layered encryption, endpoint authentication, and secure communication protocols. Case applications include:
- **AES-256** for data encryption
- **SSL/TLS** for secure data transmission
- **Blockchain + PKI** for tamper-proof logging
- **MFA & network segmentation** to harden access controls

---

## 🧪 Methodologies

### 🔹 1. Formal Verification
- Used **PRISM model checker** to mathematically validate cryptographic security
- Simulated packet capture and attack modeling
- Found a **0.05% breach probability**, confirming high system resilience

### 🔹 2. Data Masking with Steganography
- Embedded encrypted messages in images using **2D-DWT-1L and 2L**
- SSIM, SC, and Correlation values ~1 showed **high imperceptibility and integrity**

### 🔹 3. Blockchain-Based Access Control
- Used decentralized control with **chaotic encryption**
- Prevented file tampering, unauthorized access, and validated users via hash checks

### 🔹 4. Elliptic Curve Cryptography (ECC)
- Combined **Caesar cipher + IECC** for multi-layered encryption
- Offered **faster encryption**, low computational load, and stronger key security

### 🔹 5. Encryption Algorithms Comparison
- Tested **AES, DES, and RSA** in a simulated network
- AES used for real-time protection; RSA for secure key exchange
- DES shown to be outdated and only useful for legacy systems

### 🔹 6. Blockchain Simulation
- Built a basic blockchain prototype with **proof-of-work and secure transactions**
- Demonstrated potential for future IoT data logging applications

### 🔹 7. Intrusion Detection System (IDS)
- Deployed **Snort** to monitor network traffic and detect SQL injection, brute-force, and data exfiltration
- Showed value of pairing IDS with encryption to form a complete defense

### 🔹 8. Multi-Factor Authentication (MFA)
- Implemented **Google Authenticator (TOTP)** to simulate device-level MFA
- Prevented unauthorized access even after device or password compromise

---

## ✅ Results Summary

- **ECC + AES + Blockchain** proved to be the strongest cryptographic trio for lightweight, scalable, and secure IoT networks.
- Simulated tests validated strong encryption without overloading limited IoT resources.
- IDS and MFA boosted real-time defense and access control.
- Recommended a **multi-layered security approach** with real-time monitoring, blockchain authentication, and lightweight encryption.

---

## 🛠 Tools & Technologies

- Python (for simulation and encryption tests)  
- PRISM Model Checker  
- Snort IDS  
- Google Authenticator  
- AES, DES, RSA, ECC Algorithms  
- Custom Blockchain Simulation

---

## 📁 Project Files

```bash
iot-crypto-security/
│
├── README.md
├── /docs
│   └── Cryptographic Methods for Sensitive Data Protection in a Simulated IoT Network.docx
├── /src
│   ├── encryption_tests.py
│   ├── blockchain_simulation.py
│   └── ids_snort_config.rules
├── /images
│   └── diagrams, stego-images, flowcharts
└── /references
    └── IEEE and MDPI papers
