# Temp Mail API

A collection of implementations for interacting with the [TempMail.so](https://tempmail.so) temporary email service API. It allow developers to create and manage temporary email inboxes, retrieve emails, and handle other functionality with ease.  

## Supported Languages  

- Python
- PHP  
- Node.js
- C#
- Java
- Shell

## Docker 

    docker pull tempmailso/tempmail

## CLI

```bash
tempmail config <rapidapi-key> <auth-token>  # Configure API key
tempmail domains                             # Show available domains
tempmail create <name> <domain> [lifespan]   # Create new inbox
tempmail list                                # List all inboxes
tempmail delete-inbox <inbox-id>             # Delete inbox
tempmail list-mails <inbox-id>               # List emails in inbox
tempmail read-mail <inbox-id> <mail-id>      # Read email content
tempmail delete-mail <inbox-id> <mail-id>    # Delete email
tempmail help                                # Show help message
```

## Credentials

- Auth Token: Get from https://tempmail.so
- RapidAPI Key: Get from https://rapidapi.com/

## Features  
- **Inbox Management**: Create, list, and delete temporary email inboxes.  
- **Email Handling**: Retrieve, view, and delete emails.  
- **Flexible Lifespan**: Support for short-term and long-term inboxes.  
- **Authentication**: Secure access using RapidAPI keys and TempMail.so tokens.

## Documentation

Detailed API documentation can be found at the TempMail.so [API Documentation](https://tempmail.so/temp-mail-api).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this repo.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
