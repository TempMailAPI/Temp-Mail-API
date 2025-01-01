# Temporary Email CLI Tool

A command-line interface tool for managing temporary email addresses using the TempMail.so API. This tool allows you to create disposable email inboxes, receive emails, and manage your temporary email addresses all from the command line.

## Features

- Create temporary email inboxes with custom names and domains
- List available email domains
- Manage multiple inboxes
- View and read received emails
- Delete inboxes and individual emails
- Configurable inbox lifespan
- Secure API key storage

## Prerequisites

- Bash shell
- curl
- RapidAPI key for TempMail.so API
- Authentication token

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TempMailAPI/Temp-Mail-API.git
cd cli
```

2. Make the script executable:
```bash
chmod +x tempmail
```

3. Configure your API credentials:
```bash
./tempmail config <your-rapidapi-key> <your-auth-token>
```

## Usage

### Available Commands

```bash
./tempmail config <rapidapi-key> <auth-token>  # Configure API key
./tempmail domains                             # Show available domains
./tempmail create <name> <domain> [lifespan]   # Create new inbox
./tempmail list                                # List all inboxes
./tempmail delete-inbox <inbox-id>             # Delete inbox
./tempmail list-mails <inbox-id>               # List emails in inbox
./tempmail read-mail <inbox-id> <mail-id>      # Read email content
./tempmail delete-mail <inbox-id> <mail-id>    # Delete email
./tempmail help                                # Show help message
```

### Examples

1. List available domains:
```bash
./tempmail domains
```

2. Create a new inbox:
```bash
./tempmail create myinbox example.com
```

3. List all emails in an inbox:
```bash
./tempmail list-mails your-inbox-id
```

## Security

- API credentials are stored in `~/.tempmail_config`
- The configuration file permissions are set to 600 (readable only by the owner)
- API requests are made over HTTPS

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
