import re

print("\n========== IOC EXTRACTOR TOOL ==========\n")

# Read suspicious file
with open("sample.txt", "r", encoding="utf-8") as file:
    data = file.read()

# -----------------------------
# IOC PATTERNS
# -----------------------------

# IP addresses
ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}'

# Emails
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# URLs
url_pattern = r'https?://[^\s]+'

# Domains
domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'

# Hashes
hash_pattern = r'\b[a-fA-F0-9]{32,64}\b'

# -----------------------------
# FIND IOCs
# -----------------------------

ips = re.findall(ip_pattern, data)

emails = re.findall(email_pattern, data)

urls = re.findall(url_pattern, data)

domains = re.findall(domain_pattern, data)

hashes = re.findall(hash_pattern, data)

# Remove duplicates
ips = list(set(ips))
emails = list(set(emails))
urls = list(set(urls))
domains = list(set(domains))
hashes = list(set(hashes))

# -----------------------------
# PRINT RESULTS
# -----------------------------

print("[IP ADDRESSES]")
if ips:
    for ip in ips:
        print(f" - {ip}")
else:
    print(" No IP addresses found")

print("\n[EMAIL ADDRESSES]")
if emails:
    for email in emails:
        print(f" - {email}")
else:
    print(" No emails found")

print("\n[URLS]")
if urls:
    for url in urls:
        print(f" - {url}")
else:
    print(" No URLs found")

print("\n[DOMAINS]")
if domains:
    for domain in domains:
        print(f" - {domain}")
else:
    print(" No domains found")

print("\n[HASHES]")
if hashes:
    for h in hashes:
        print(f" - {h}")
else:
    print(" No hashes found")

print("\n========================================")