from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import subprocess

# Load student's private key
with open("keygen/private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Get current commit hash
commit_hash = subprocess.check_output(
    ["git", "rev-parse", "HEAD"]
).strip()

# Sign the commit hash
signature = private_key.sign(
    commit_hash,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Save signature
with open("sig.bin", "wb") as f:
    f.write(signature)

print("Commit signed successfully")
