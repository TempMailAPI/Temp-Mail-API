"""
TempMail.so API SDK
A Python wrapper for the TempMail.so temporary email service API.

This SDK provides methods to:
- Create and manage temporary email inboxes
- List available domains
- Retrieve and manage emails
- Handle authentication

Author: TempMail.so
License: MIT
Version: 1.0.0
"""

import requests
from typing import Dict, List, Optional, Union


class TempMailSo:
    """TempMail API client for managing temporary email services."""
    
    BASE_URL = "https://tempmail-so.p.rapidapi.com"
    
    def __init__(self, rapid_api_key: str, auth_token: str):
        """
        Initialize the TempMail client.
        
        Args:
            rapid_api_key (str): Your RapidAPI key
            auth_token (str): Your TempMail.so authorization token
        """
        self.headers = {
            'x-rapidapi-key': rapid_api_key,
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
    def list_domains(self) -> Dict:
        """Get a list of available email domains."""
        response = requests.get(
            f"{self.BASE_URL}/domains",
            headers=self.headers
        )
        return response.json()
    
    def create_inbox(self, address: str, domain: str, lifespan: int = 0) -> Dict:
        """
        Create a new temporary email inbox.
        
        Args:
            address (str): Custom email prefix
            domain (str): Email domain
            lifespan (int): Inbox lifespan in seconds (0, 300, 600, 900, 1200, 1800)
                          0 means long-term use
        """
        data = {
            'name': address,
            'domain': domain,
            'lifespan': lifespan
        }
        response = requests.post(
            f"{self.BASE_URL}/inboxes",
            headers=self.headers,
            data=data
        )

        return response.json()
    
    def list_inboxes(self) -> Dict:
        """Get a list of all inboxes associated with the account."""
        response = requests.get(
            f"{self.BASE_URL}/inboxes",
            headers=self.headers
        )
        return response.json()
    
    def delete_inbox(self, inbox_id: str) -> Dict:
        """
        Delete a specific inbox.
        
        Args:
            inbox_id (str): ID of the inbox to delete
        """
        response = requests.delete(
            f"{self.BASE_URL}/inboxes/{inbox_id}",
            headers=self.headers
        )
        return response.json()
    
    def list_emails(self, inbox_id: str) -> Dict:
        """
        Get all emails in a specific inbox.
        
        Args:
            inbox_id (str): ID of the inbox
        """
        response = requests.get(
            f"{self.BASE_URL}/inboxes/{inbox_id}/mails",
            headers=self.headers
        )
        return response.json()
    
    def get_email(self, inbox_id: str, email_id: str) -> Dict:
        """
        Get details of a specific email.
        
        Args:
            inbox_id (str): ID of the inbox
            email_id (str): ID of the email
        """
        response = requests.get(
            f"{self.BASE_URL}/inboxes/{inbox_id}/mails/{email_id}",
            headers=self.headers
        )
        return response.json()
    
    def delete_email(self, inbox_id: str, email_id: str) -> Dict:
        """
        Delete a specific email.
        
        Args:
            inbox_id (str): ID of the inbox
            email_id (str): ID of the email to delete
        """
        response = requests.delete(
            f"{self.BASE_URL}/inboxes/{inbox_id}/mails/{email_id}",
            headers=self.headers
        )
        return response.json() 
