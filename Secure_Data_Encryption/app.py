import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate a key (same across the session; in real apps store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory storage
stored_data = {}
failed_attempts = 0

# Hashing function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_pass = hash_passkey(passkey)

    for val in stored_data.values():
        if val["encrypted_text"] == encrypted_text and val["passkey"] == hashed_pass:
            failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()

    failed_attempts += 1
    return None


st.title("🛡️ Secure Data Encryption System")
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.info("Use this app to **securely store and retrieve data** with a unique passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Your Data")
    text = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Enter a secret passkey:", type="password")

    if st.button("Encrypt & Save"):
        if text and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(text)
            stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data encrypted and stored securely!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Please fill all fields!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_input = st.text_area("Enter the encrypted data:")
    passkey_input = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            result = decrypt_data(encrypted_input, passkey_input)
            if result:
                st.success(f"✅ Decrypted Data:\n{result}")
            else:
                st.error(f"❌ Wrong passkey! Attempts left: {3 - failed_attempts}")
                if failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to login...")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Please fill all fields.")

elif choice == "Login":
    st.subheader("🔑 Reauthorize Access")
    login_pass = st.text_input("Enter admin password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":
            failed_attempts = 0
            st.success("✅ Login successful. Redirecting...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password.")
