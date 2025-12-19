from fastapi import FastAPI
import pyotp

app = FastAPI()

totp = pyotp.TOTP(pyotp.random_base32())

@app.post("/decrypt-seed")
def decrypt_seed():
    return {"status": "ok"}

@app.get("/generate-2fa")
def generate_2fa():
    return {"otp": totp.now()}

@app.post("/verify-2fa")
def verify_2fa(code: str):
    return {"valid": totp.verify(code)}
