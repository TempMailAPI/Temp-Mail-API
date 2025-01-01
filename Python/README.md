# TempMail.so Python SDK

A Python SDK for interacting with the TempMail.so temporary email service API.

## Features

- Create and manage temporary email inboxes
- List available email domains
- Retrieve and manage emails
- Full API coverage with simple interface
- Type hints support
- MIT licensed

## Installation

```bash
pip install temp-mail-so
```

## Quick Start

```python
from temp_mail_so import TempMailSo

# Initialize client
client = TempMailSo(
    rapid_api_key="your_rapid_api_key_here",
    auth_token="your_auth_token_here"
)

# Create a temporary inbox
inbox = client.create_inbox(
    address="test123",  # Email prefix
    domain="mailnuo.com",  # Domain
    lifespan=300  # Inbox lifespan in seconds (0 for permanent)
)

# List all emails in an inbox
emails = client.list_emails(inbox_id="your_inbox_id")
```

## API Reference

### TempMailSo Class

#### `__init__(rapid_api_key: str, auth_token: str)`
Initialize the TempMail client with your API credentials.

#### `list_domains() -> Dict`
Get a list of available email domains.

#### `create_inbox(address: str, domain: str, lifespan: int = 0) -> Dict`
Create a new temporary email inbox.
- `address`: Custom email prefix
- `domain`: Email domain
- `lifespan`: Inbox lifespan in seconds (0, 300, 600, 900, 1200, 1800). 0 means permanent.

#### `list_inboxes() -> Dict`
Get a list of all inboxes associated with the account.

#### `delete_inbox(inbox_id: str) -> Dict`
Delete a specific inbox.

#### `list_emails(inbox_id: str) -> Dict`
Get all emails in a specific inbox.

#### `get_email(inbox_id: str, email_id: str) -> Dict`
Get details of a specific email.

#### `delete_email(inbox_id: str, email_id: str) -> Dict`
Delete a specific email.

## Requirements

- Python 3.6+
- `requests` library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

TempMail.so

## Version

1.0.0

_Last updated: 2025-01-01_
