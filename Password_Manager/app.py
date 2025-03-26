import streamlit as st
import re
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase the password length to at least 8 characters.")

    # Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Assign Strength Level
    if score == 1 or score == 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback
def main():
    st.title("🔐 Password Strength Meter")

    # User Input
    password = st.text_input("Enter your password:", type="password")

    if st.button("Check Strength"):
        if password:
            strength, feedback = check_password_strength(password)

            # Display Strength
            st.subheader(f"Password Strength: {strength}")

            # Feedback
            if feedback:
                st.warning("🔹 Suggestions to Improve:")
                for tip in feedback:
                    st.write(f"• {tip}")
            else:
                st.success("✅ Your password is strong!")
        else:
            st.error("Please enter a password.")

if __name__ == "__main__":
    main()
