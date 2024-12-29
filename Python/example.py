"""
TempMail.so API SDK Usage Examples
This file demonstrates how to use the TempMail SDK for various operations.
"""

from tempmail_sdk import TempMailSo
import time

# Initialize the client with your API credentials
client = TempMailSo(
    rapid_api_key="YOUR_RAPIDAPI_KEY",
    auth_token="YOUR_AUTH_TOKEN"
)

def main():
    # 1. List available domains
    print("Getting available domains...")
    domains = client.list_domains()
    print(f"Available domains: {domains}\n")

    # 2. Create a new inbox
    print("Creating new inbox...")
    inbox = client.create_inbox(
        address="testuser123",
        domain="mailnuo.com",
        lifespan=600  # 10 minutes
    )
    inbox_id = inbox['data']['id']
    print(f"Created inbox with ID: {inbox_id}\n")

    # 3. List all inboxes
    print("Listing all inboxes...")
    inboxes = client.list_inboxes()
    print(f"All inboxes: {inboxes}\n")

    # 4. Wait for and check emails (simulated)
    print("Checking for emails...")
    time.sleep(5)  # Wait a bit for potential emails
    emails = client.list_emails(inbox_id)
    print(f"Emails in inbox: {emails}\n")

    # 5. If there are emails, get details of the first one
    if emails.get('data') and len(emails['data']) > 0:
        email_id = emails['data'][0]['id']
        print("Getting email details...")
        email_details = client.get_email(inbox_id, email_id)
        print(f"Email details: {email_details}\n")

        # 6. Delete the email
        print("Deleting email...")
        delete_result = client.delete_email(inbox_id, email_id)
        print(f"Delete email result: {delete_result}\n")

    # 7. Finally, delete the inbox
    print("Deleting inbox...")
    delete_result = client.delete_inbox(inbox_id)
    print(f"Delete inbox result: {delete_result}")

if __name__ == "__main__":
    main() 
