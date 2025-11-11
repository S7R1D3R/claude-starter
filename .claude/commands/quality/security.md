---
description: Run security vulnerability scan on code and dependencies
---

# Security Scan

Perform comprehensive security vulnerability scanning.

## Dependency Scanning

Check for known vulnerabilities in dependencies:

### JavaScript/Node.js
- **npm audit**: `npm audit`
- **yarn audit**: `yarn audit`
- **Snyk**: `snyk test` (if installed)

### Python
- **safety**: `safety check`
- **pip-audit**: `pip-audit`
- **Bandit** (code scan): `bandit -r .`

### Rust
- **cargo-audit**: `cargo audit`

### Go
- **govulncheck**: `govulncheck ./...`

### Ruby
- **bundler-audit**: `bundle audit`

### Java
- **OWASP Dependency Check**: If configured
- **Snyk**: `snyk test`

### PHP
- **composer audit**: `composer audit`

## Static Code Analysis

Scan code for security issues:

### All Languages
- **Semgrep**: `semgrep --config=auto .`
- **Trivy**: `trivy fs .`

### Python
- **Bandit**: `bandit -r src/`
  - Checks for SQL injection, XSS, hardcoded secrets, etc.

### JavaScript
- **ESLint security plugin**: If configured
- **npm audit signatures**: `npm audit signatures`

### Go
- **gosec**: `gosec ./...`

## Security Checklist

Scan for common vulnerabilities:

### 1. Secrets Detection
- [ ] No API keys in code
- [ ] No passwords in code
- [ ] No private keys committed
- [ ] Check .env files in .gitignore

### 2. Injection Vulnerabilities
- [ ] SQL injection protection
- [ ] Command injection protection
- [ ] XSS protection
- [ ] Path traversal protection

### 3. Authentication & Authorization
- [ ] Proper session management
- [ ] Secure password storage
- [ ] JWT properly validated
- [ ] Authorization checks present

### 4. Data Protection
- [ ] Sensitive data encrypted
- [ ] HTTPS enforced
- [ ] No sensitive data in logs
- [ ] Secure cookie settings

### 5. Dependencies
- [ ] No known vulnerabilities
- [ ] Dependencies up to date
- [ ] Minimal dependency footprint

## Execution Process

1. **Run** dependency audit
2. **Run** static code analysis
3. **Scan** for secrets
4. **Check** configuration files
5. **Aggregate** findings
6. **Prioritize** by severity
7. **Report** results with remediation

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔒 SECURITY SCAN RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Dependency Vulnerabilities
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 Critical: 1
   • lodash@4.17.20 - Prototype Pollution
     Fix: npm install lodash@4.17.21

🟡 High: 2
   • axios@0.21.0 - SSRF vulnerability
     Fix: npm install axios@0.21.4
   • express@4.17.0 - Open redirect
     Fix: npm install express@4.18.0

🟢 Medium: 5
   [Details...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 Code Security Issues
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ src/api/db.js:45
   SQL Injection risk - Using string concatenation
   Use parameterized queries instead

⚠ src/utils/auth.js:23
   Weak password hashing - Using MD5
   Use bcrypt or argon2 instead

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary:
  Dependencies: 8 vulnerabilities (1 critical, 2 high, 5 medium)
  Code Issues: 2 warnings

Action Required:
  1. Update vulnerable dependencies immediately
  2. Fix SQL injection in db.js
  3. Upgrade password hashing algorithm

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Remediation Guidance

For each issue:
- Explain the vulnerability
- Show vulnerable code
- Provide secure alternative
- Link to resources (OWASP, CVE)

## Severity Levels

- 🔴 **Critical**: Immediate action required
- 🟡 **High**: Fix before release
- 🟠 **Medium**: Should fix soon
- 🟢 **Low**: Consider fixing

## Arguments

- `/quality:security` - Full security scan
- `/quality:security --deps-only` - Only check dependencies
- `/quality:security --code-only` - Only static code analysis
- `/quality:security --fix` - Auto-update fixable vulnerabilities

**IMPORTANT**: Critical vulnerabilities should block deployment. Always provide clear remediation steps.
