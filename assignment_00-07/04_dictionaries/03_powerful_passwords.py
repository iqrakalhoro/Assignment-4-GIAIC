from hashlib import sha256
import datetime
import re


stored_logins = {
    "admin@example.com": sha256("admin123!".encode()).hexdigest()
}
login_attempts = {}
activity_log = []


def hash_password(password):
    return sha256(password.encode()).hexdigest()


def is_strong_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

def register_user():
    print("\n🔐 Register New Account")
    email = input("📧 Enter your email: ")
    if email in stored_logins:
        print("⚠️ Email already registered.")
        return
    password = input("🔑 Enter a strong password: ")
    if not is_strong_password(password):
        print("❌ Weak password! Must be 8+ characters with upper, lower, number, and special char.")
        return
    stored_logins[email] = hash_password(password)
    log_activity(f"✅ Registered: {email}")
    print("✅ User registered successfully!")

def login(email, password_to_check):
    if email not in stored_logins:
        print("❌ Email not registered.")
        return False

    if login_attempts.get(email, 0) >= 3:
        print("🚫 Too many failed attempts. Try again later.")
        return False

    hashed = hash_password(password_to_check)
    if stored_logins[email] == hashed:
        login_attempts[email] = 0  # reset counter
        log_activity(f"🔓 Login successful: {email}")
        print("✅ Login successful!")
        return True
    else:
        login_attempts[email] = login_attempts.get(email, 0) + 1
        print(f"❌ Incorrect password. Attempt {login_attempts[email]}/3")
        log_activity(f"❌ Failed login for {email}")
        return False

def log_activity(event):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    activity_log.append(f"[{time}] {event}")

def print_activity_log():
    print("\n📋 Activity Log:")
    for entry in activity_log:
        print(entry)

def main():
    while True:
        print("\n📘 MENU:")
        print("1. 🔑 Login")
        print("2. ✅ Register")
        print("3. 📊 View Activity Log")
        print("4. ❌ Exit")

        choice = input("➡️ Enter choice (1-4): ")
        if choice == "1":
            email = input("📧 Email: ")
            password = input("🔑 Password: ")
            login(email, password)
        elif choice == "2":
            register_user()
        elif choice == "3":
            print_activity_log()
        elif choice == "4":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid option. Please choose 1–4.")

if __name__ == '__main__':
    main()
