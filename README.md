# 🔐 Password Strength Checker

A terminal-based password analysis tool written in Python. It evaluates passwords against common security rules, calculates Shannon entropy, and estimates offline brute-force crack time — all with no external dependencies.

---

## Features

- ✅ Checks 6 password rules (length, character variety, etc.)
- 📊 Calculates **entropy in bits** based on character pool size
- ⏱️ Estimates **crack time** assuming a 10B guesses/sec offline attack
- 🏷️ Assigns a human-readable **strength label** (Very Weak → Very Strong)
- 🔒 Never prints the password in plaintext — masked with `*`

---

## Requirements

- Python 3.6+
- No third-party packages — uses only `math` and `re` from the standard library

---

## Usage

```bash
python password_checker.py
```

You'll see an interactive prompt:

```
  Password Strength Checker
  Type a password to analyse it. Press Ctrl+C to quit.

  Enter password: ••••••••••••

─────────────────────────────────────────────
  Password : ************  (12 chars)
─────────────────────────────────────────────

  Rules:
    ✓  At least 8 characters
    ✓  Uppercase letter
    ✓  Lowercase letter
    ✓  Number (0-9)
    ✓  Special character
    ✓  12+ characters (recommended)

  Strength     : Very Strong  (6/6 rules passed)
  Entropy      : 78.6 bits
  Char pool    : 94 possible characters
  Crack time   : billions of years  (offline, 10B guesses/sec)
─────────────────────────────────────────────
```

Press `Ctrl+C` to exit.

---

## How It Works

### Rule Checking

Six rules are evaluated using regex pattern matching:

| Rule | Criteria |
|---|---|
| Minimum length | ≥ 8 characters |
| Uppercase | Contains `[A-Z]` |
| Lowercase | Contains `[a-z]` |
| Digit | Contains `[0-9]` |
| Special character | Contains anything not alphanumeric |
| Recommended length | ≥ 12 characters |

### Entropy Calculation

Entropy is calculated using the formula:

```
Entropy (bits) = log₂(pool_size) × password_length
```

The character pool is built by detecting which character classes are present:

| Class | Pool size |
|---|---|
| Lowercase letters | +26 |
| Uppercase letters | +26 |
| Digits | +10 |
| Special characters | +32 |

A password using all four classes has a pool of 94, giving ~6.55 bits per character.

### Crack Time Estimation

Assumes an offline brute-force attack at **10 billion guesses per second** (realistic for a modern GPU targeting hashed passwords). The attacker is expected to find the password after trying half of all possible combinations on average:

```
seconds = (2^entropy / 2) / 10,000,000,000
```

Results are shown in a human-readable format from "instant" up to "billions of years".

### Strength Label

The number of passed rules (0–6) maps to a label:

| Score | Label |
|---|---|
| 0 | Very Weak |
| 1 | Weak |
| 2 | Fair |
| 3 | Moderate |
| 4 | Strong |
| 5–6 | Very Strong |

---

## File Structure

```
password-strength-checker/
└── password_checker.py       # Single-file implementation
└── README.md    # This file
```
---

## License

MIT License. Feel free to use, modify, and distribute.
