"""
TempMail.so API SDK Usage Examples
This file demonstrates how to use the TempMail SDK for various operations.
"""

from temp_mail_so import TempMailSo

def main():
    # Initialize client
    # Replace with your actual API key
    client = TempMailSo(
        rapid_api_key="your_rapid_api_key_here",
        auth_token="your_auth_token_here"
    )
    
    try:
        # 1. Get available domain list
        print("Getting available domains...")
        domains = client.list_domains()
        print(f"Available domains: {domains}\n")

        # 2. Create a temporary inbox
        print("Creating temporary inbox...")
        inbox = client.create_inbox(
            address="test123",  # Email prefix
            domain="mailnuo.com",  # Domain
            lifespan=300  # Inbox lifespan (seconds), 0 means permanent
        )
        print(f"Created inbox info: {inbox}\n")
        
        # 3. Get all inboxes
        print("Getting inbox list...")
        inboxes = client.list_inboxes()
        print(f"All inboxes: {inboxes}\n")
        
        # Assuming we have received an email, inbox_id and email_id are known
        inbox_id = "your_inbox_id"
        
        # 4. Get all emails from specified inbox
        print(f"Getting all emails from inbox {inbox_id}...")
        emails = client.list_emails(inbox_id)
        print(f"Email list: {emails}\n")
        
        # 5. If there are emails, get details of the first email
        if emails.get('mails'):
            email_id = emails['mails'][0]['id']
            print(f"Getting details for email {email_id}...")
            email_detail = client.get_email(inbox_id, email_id)
            print(f"Email details: {email_detail}\n")
            
            # 6. Delete this email
            print(f"Deleting email {email_id}...")
            delete_result = client.delete_email(inbox_id, email_id)
            print(f"Delete result: {delete_result}\n")
        
        # 7. Finally delete the inbox
        print(f"Deleting inbox {inbox_id}...")
        delete_inbox_result = client.delete_inbox(inbox_id)
        print(f"Delete inbox result: {delete_inbox_result}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 
