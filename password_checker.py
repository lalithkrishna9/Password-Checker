import re
import math

def check_password(password):
    
    rules = {
        "At least 8 characters":len(password) >= 8,
        "Uppercase letter":bool(re.search(r"[A-Z]", password)),
        "Lowercase letter":bool(re.search(r"[a-z]", password)),
        "Number (0-9)":bool(re.search(r"[0-9]", password)),
        "Special character":bool(re.search(r"[!@#$%^&*()<>?}|]\;':]", password)),
        "12+ characters (recommended)":  len(password) >= 12,
    }
    score = sum(rules.values())

    
    labels = ["Very Weak", "Weak", "Fair", "Moderate", "Strong", "Very Strong"]
    label = labels[max(0, score - 1)]

    
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[^a-zA-Z0-9]", password): pool += 32

    entropy = round(math.log2(pool) * len(password), 2) if pool else 0

    
    seconds = (2 ** entropy / 2) / 10_000_000_000 if entropy else 0
    if   seconds < 1:         crack = "instant"
    elif seconds < 60:        crack = f"{int(seconds)} seconds"
    elif seconds < 3600:      crack = f"{int(seconds / 60)} minutes"
    elif seconds < 86400:     crack = f"{int(seconds / 3600)} hours"
    elif seconds < 31_536_000:crack = f"{int(seconds / 86400)} days"
    elif seconds < 3.15e9:    crack = f"{int(seconds / 31_536_000)} years"
    elif seconds < 3.15e12:   crack = f"{int(seconds / 3.15e9):,}K years"
    else:                     crack = "billions of years"

    
    print(f"\n  Password  : {'*' * len(password)}  ({len(password)} digits)")
    for rule, passed in rules.items():
        print(f"  {'✓' if passed else '✗'}  {rule}")
    print(f"\n  Strength  : {label}  ({score}/6)")
    print(f"  Entropy   : {entropy} bits  |  Pool: {pool} chars")
    print(f"  Crack time: {crack}  (offline, 10B guesses/sec)\n")


print("Password Strength Checker — Ctrl+C to quit\n")
while True:
    try:
        pw = input("  Enter password: ")
        if pw:
            check_password(pw)
    except KeyboardInterrupt:
        print("\n  Bye!")
        break