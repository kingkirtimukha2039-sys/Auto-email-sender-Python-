# ============================================
# AUTO EMAIL SENDER - Python Project
# By: [Your Name] | Portfolio Project
# ============================================
# SETUP: pip install secure-smtplib
# Gmail: Enable "App Password" in Google Account
# Go to: myaccount.google.com > Security > App Passwords
# ============================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── CONFIG ──────────────────────────────────
SENDER_EMAIL    = "your_email@gmail.com"   # Your Gmail
SENDER_PASSWORD = "your_app_password"      # Gmail App Password (NOT your real password)
# ────────────────────────────────────────────


def send_email(to_email, subject, body):
    """Send a single email."""
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"]    = SENDER_EMAIL
        msg["To"]      = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail and send
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

        print(f"✅ Email sent to {to_email}")
        return True

    except Exception as e:
        print(f"❌ Failed to send to {to_email} → {e}")
        return False


def send_bulk_emails(recipients, subject, body):
    """Send same email to multiple people."""
    print(f"\n📧 Sending emails to {len(recipients)} recipients...\n")
    success = 0
    for email in recipients:
        if send_email(email, subject, body):
            success += 1
    print(f"\n📊 Result: {success}/{len(recipients)} emails sent successfully!")


def send_personalized_emails(recipient_list):
    """
    Send personalized emails using a list of dicts.
    Each dict: {"email": "...", "name": "...", "subject": "...", "body": "..."}
    """
    print(f"\n📧 Sending {len(recipient_list)} personalized emails...\n")
    success = 0
    for person in recipient_list:
        if send_email(person["email"], person["subject"], person["body"]):
            success += 1
    print(f"\n📊 Result: {success}/{len(recipient_list)} emails sent successfully!")


# ── MAIN MENU ────────────────────────────────
def main():
    print("=" * 45)
    print("       AUTO EMAIL SENDER - Python")
    print("=" * 45)
    print("1. Send email to ONE person")
    print("2. Send SAME email to MULTIPLE people")
    print("3. Send PERSONALIZED emails")
    print("4. Exit")
    print("=" * 45)

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        to      = input("Recipient email: ").strip()
        subject = input("Subject: ").strip()
        body    = input("Message body: ").strip()
        send_email(to, subject, body)

    elif choice == "2":
        emails_input = input("Enter emails separated by comma: ").strip()
        recipients   = [e.strip() for e in emails_input.split(",")]
        subject      = input("Subject: ").strip()
        body         = input("Message body: ").strip()
        send_bulk_emails(recipients, subject, body)

    elif choice == "3":
        # Example personalized list — edit as needed
        recipient_list = [
            {
                "email":   "friend1@gmail.com",
                "subject": "Hello Rahul!",
                "body":    "Hi Rahul,\n\nThis is a personalized message just for you!\n\nBest,\nYour Name"
            },
            {
                "email":   "friend2@gmail.com",
                "subject": "Hello Priya!",
                "body":    "Hi Priya,\n\nThis is a personalized message just for you!\n\nBest,\nYour Name"
            },
        ]
        print("\n⚠️  Edit the recipient_list in the code with real emails before running!")
        confirm = input("Have you edited the list? (yes/no): ").strip().lower()
        if confirm == "yes":
            send_personalized_emails(recipient_list)
        else:
            print("Please edit recipient_list in the code first.")

    elif choice == "4":
        print("👋 Goodbye!")

    else:
        print("❌ Invalid choice. Please enter 1–4.")


if __name__ == "__main__":
    main()


# ============================================
# HOW TO USE:
# 1. Replace SENDER_EMAIL with your Gmail
# 2. Replace SENDER_PASSWORD with Gmail App Password
# 3. Run: python auto_email_sender.py
# 4. Choose option 1, 2, or 3
# ============================================
