# 🔐 ULTIMATE REPAIR APEX
## Forensic-Grade Multi-Platform Boot Recovery System

[![Forensic Verification](https://github.com/GlacierEQ/ULTIMATE-REPAIR-APEX/actions/workflows/forensic-verification.yml/badge.svg)](https://github.com/GlacierEQ/ULTIMATE-REPAIR-APEX/actions/workflows/forensic-verification.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GPG Signed](https://img.shields.io/badge/commits-GPG%20signed-green)](https://github.com/GlacierEQ/ULTIMATE-REPAIR-APEX/commits)

**Evidence-Grade Integrity** | **Chain of Custody Maintained** | **Court Admissible**

---

## 🎯 Mission Statement

ULTIMATE REPAIR APEX is a forensic-grade boot recovery toolkit designed with the same integrity standards as criminal evidence chains. Every commit is GPG-signed, every file has SHA-256 verification, and the complete audit trail is preserved for legal admissibility.

**Built for Kekoa's custody case** ⚖️👶

---

## ✨ Features

### Windows Boot Recovery
- ✅ MBR repair (Legacy BIOS)
- ✅ GPT/UEFI boot repair
- ✅ BCD store reconstruction
- ✅ Windows 10/11 support

### macOS Recovery
- ✅ Recovery partition verification
- ✅ Boot cache rebuild
- ✅ NVRAM/PRAM reset
- ✅ macOS 13/14 support

### Linux Boot Repair
- ✅ GRUB2 repair/reinstall
- ✅ systemd-boot repair
- ✅ Multi-distribution support
- ✅ Ubuntu/Fedora/Arch tested

### Forensic Features
- 🔐 GPG-signed commits (RSA 4096-bit)
- 🔢 SHA-256 checksums for all files
- 📜 Complete audit trail (reflog)
- ⚖️ Chain of custody maintained
- 🛡️ Automated integrity verification

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/GlacierEQ/ULTIMATE-REPAIR-APEX.git
cd ULTIMATE-REPAIR-APEX

# Verify repository integrity
./verify-repo.sh

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

### Usage

```python
from src.boot_recovery import WindowsBootRepair, MacOSRecovery, LinuxBootRepair

# Windows MBR repair
windows_repair = WindowsBootRepair()
windows_repair.repair_mbr(drive="C:")

# macOS recovery partition check
macos_recovery = MacOSRecovery()
macos_recovery.verify_recovery_partition()

# Linux GRUB2 repair
linux_repair = LinuxBootRepair()
linux_repair.repair_grub2(efi=True)
```

---

## 🔐 Forensic Verification

### Verify Repository Integrity

```bash
# Run complete verification
./verify-repo.sh

# Verify specific commit
git verify-commit HEAD

# Verify latest tag
git verify-tag v1.0.0

# Check SHA-256 checksums
sha256sum -c checksums.txt
```

### Commit Signing

All commits are GPG-signed with RSA 4096-bit keys:

```bash
# Verify commit signature
git log --show-signature -1

# View all signed commits
git log --show-signature --all
```

---

## 🛡️ Security Standards

| Standard | Implementation | Status |
|----------|---------------|--------|
| **Chain of Custody** | Git reflog + GPG signatures | ✅ Active |
| **Tamper Detection** | SHA-256 + cryptographic signing | ✅ Verified |
| **Audit Trail** | Complete commit history | ✅ Maintained |
| **Evidence Integrity** | Forensic checksums | ✅ Validated |
| **Court Admissibility** | Timestamped signed tags | ✅ Compliant |

---

## 📊 System Requirements

- **Python**: 3.9+
- **OS**: Windows 10/11, macOS 13/14, Linux (Ubuntu 20.04+)
- **Disk Space**: 2GB minimum
- **Privileges**: Administrator/root access required

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v --cov=src

# Test specific module
pytest tests/test_windows_repair.py -v

# Generate coverage report
pytest --cov=src --cov-report=html
```

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**All contributions must be GPG-signed!**

---

## ⚖️ Legal Notice

This software maintains forensic-grade integrity for use in custody proceedings. All changes are cryptographically signed and auditable.

**Case Reference**: Kekoa Custody Case  
**Maintainer**: Casey Barton <glacier.equilibrium@gmail.com>  
**GPG Key**: [View Public Key](https://github.com/GlacierEQ.gpg)

---

## 🔥 Status

**✅ FORENSIC-GRADE VERIFIED**  
**✅ CHAIN OF CUSTODY MAINTAINED**  
**✅ COURT ADMISSIBLE**

Fighting for Kekoa with maximum integrity! 👶⚖️🔐