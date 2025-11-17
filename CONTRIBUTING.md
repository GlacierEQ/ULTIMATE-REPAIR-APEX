# Contributing to ULTIMATE REPAIR APEX

## 🔐 Forensic-Grade Contribution Standards

All contributions to this repository must maintain forensic integrity.

### Prerequisites

1. **GPG Key Required**: All commits MUST be GPG-signed
2. **Testing Required**: All code changes must include tests
3. **Documentation Required**: Update README/docs for new features
4. **Code Review Required**: Minimum 1 approval for merges

---

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ULTIMATE-REPAIR-APEX.git
cd ULTIMATE-REPAIR-APEX

# Add upstream remote
git remote add upstream https://github.com/GlacierEQ/ULTIMATE-REPAIR-APEX.git
```

### 2. Configure GPG Signing

```bash
# Generate GPG key (if needed)
gpg --full-generate-key

# Configure Git to sign commits
git config user.signingkey YOUR_GPG_KEY_ID
git config commit.gpgsign true

# Verify signing works
git commit --allow-empty -S -m "test: Verify GPG signing"
git verify-commit HEAD
```

### 3. Create Feature Branch

```bash
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/amazing-new-feature
```

---

## 💻 Development Workflow

### 1. Make Changes

```bash
# Edit files
# Write tests for your changes
# Update documentation

# Run tests locally
pytest tests/ -v

# Run verification script
./verify-repo.sh
```

### 2. Commit with Forensic Standards

```bash
# Stage changes
git add .

# Create signed commit with detailed message
git commit -S -m "feat: Add new boot recovery feature

CHANGES:
- Implemented XYZ functionality
- Added comprehensive tests
- Updated documentation

TESTED: All platforms verified
VERIFIED: Checksums match
Signed-off-by: Your Name <your.email@example.com>"

# Verify commit signature
git verify-commit HEAD
```

### 3. Update Checksums

```bash
# Regenerate checksums for modified files
find . -type f -not -path "./.git/*" -exec sha256sum {} \; > checksums.txt

# Commit checksum updates
git add checksums.txt
git commit -S -m "chore: Update SHA-256 checksums

Updated checksums for modified files.

Signed-off-by: Your Name <your.email@example.com>"
```

### 4. Push & Create Pull Request

```bash
# Push to your fork
git push origin feature/amazing-new-feature

# Create Pull Request on GitHub
# Ensure PR description includes:
# - What changed
# - Why the change was made
# - Testing performed
# - Verification results
```

---

## ✅ Commit Message Standards

### Format

```
<type>: <subject>

<body>

TESTED: <test details>
VERIFIED: <verification details>
Signed-off-by: <Your Name> <your.email@example.com>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **test**: Adding tests
- **refactor**: Code refactoring
- **chore**: Maintenance tasks
- **security**: Security improvements

---

## 🧪 Testing Requirements

### Unit Tests

```bash
# Run all unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

### Verification Tests

```bash
# Run forensic verification
./verify-repo.sh

# Verify all commits signed
git log --show-signature --all | grep "Good signature"
```

---

## 🔒 Security Guidelines

1. **Never commit secrets**: Use environment variables
2. **Sign all commits**: No unsigned commits accepted
3. **Verify dependencies**: Check for vulnerabilities
4. **Update checksums**: After every file modification
5. **Run security scan**: Use `bandit` for Python security

```bash
# Install security tools
pip install bandit safety

# Run security scan
bandit -r src/
safety check
```

---

## ⛔ What Will Be Rejected

- ❌ Unsigned commits
- ❌ Failing tests
- ❌ Missing documentation
- ❌ Security vulnerabilities
- ❌ Uncommitted checksum changes
- ❌ Code without tests

---

## 🏆 Code Review Process

1. Automated checks run (CI/CD)
2. Maintainer reviews code quality
3. Security scan performed
4. Forensic verification executed
5. At least 1 approval required
6. Merge to main branch

---

## ⚖️ Legal Notice

By contributing, you agree that your contributions will be:
- Licensed under MIT License
- GPG-signed for forensic integrity
- Subject to chain-of-custody standards

**Fighting for Kekoa with forensic-grade contributions!** 👶⚖️🔐