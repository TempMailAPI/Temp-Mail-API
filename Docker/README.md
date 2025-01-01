# TempMail CLI Docker Image

A command-line interface Docker image for managing temporary email addresses using the TempMail.so API. This tool allows you to create disposable email inboxes, receive emails, and manage your temporary email addresses all from the command line.

## Quick Start

```bash
# Pull the Docker image
docker pull tempmailso/tempmail

# Create configuration file with your API credentials
mkdir -p ~/.tempmail_config
echo "RAPID_API_KEY=your-rapidapi-key" > ~/.tempmail_config
echo "AUTH_TOKEN=your-auth-token" >> ~/.tempmail_config
chmod 600 ~/.tempmail_config

# Run the container
docker run -v ~/.tempmail_config:/root/.tempmail_config tempmailso/tempmail
```

For convenience, add this alias to your shell configuration file (~/.bashrc, ~/.zshrc, etc.):
```bash
alias tempmail='docker run -v ~/.tempmail_config:/root/.tempmail_config tempmailso/tempmail'
```

## Required Credentials

Before using this tool, you need to obtain two credentials:
- **Auth Token**: Get from [TempMail.so](https://tempmail.so)
- **RapidAPI Key**: Get from [RapidAPI](https://rapidapi.com/)

## Features

- Create temporary email inboxes with custom names and domains
- List available email domains
- Manage multiple inboxes
- View and read received emails
- Delete inboxes and individual emails
- Configurable inbox lifespan
- Secure API key storage

## Usage Examples

After setting up the alias, you can use these commands:

```bash
# Show help message
tempmail help

# List available domains
tempmail domains

# Create new inbox
tempmail create myinbox example.com

# List all inboxes
tempmail list

# Check emails in an inbox
tempmail list-mails <inbox-id>

# Read specific email
tempmail read-mail <inbox-id> <mail-id>
```

## Available Commands

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

## Security

- API credentials are stored in a local configuration file
- Configuration file permissions are set to 600 (readable only by owner)
- All API requests are made over HTTPS
- Credentials are never logged or exposed

## Docker Image Details

- Base Image: Alpine Linux 3.21.0
- Installed Dependencies: bash, curl
- Size: Minimal (~10MB)
- Global Command: The `tempmail` command is available system-wide in the container

## Source Code

The source code for this Docker image is available on GitHub: [TempMailAPI/Temp-Mail-API](https://github.com/TempMailAPI/Temp-Mail-API)

## License

This project is licensed under the MIT License.
