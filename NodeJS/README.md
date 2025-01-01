# TempMail.so API SDK

[![NPM Version](https://img.shields.io/npm/v/temp-mail-so.svg)](https://www.npmjs.com/package/temp-mail-so)
[![License](https://img.shields.io/npm/l/temp-mail-so.svg)](https://github.com/TempMailAPI/Temp-Mail-API/blob/main/LICENSE)

Node.js SDK for [TempMail.so](https://tempmail.so) API - A simple and easy-to-use temporary email API service.

## Features

- Create temporary email inboxes
- Manage inbox lifecycle
- Receive and manage emails
- Full TypeScript support
- Simple and intuitive API

## Installation

```bash
npm install temp-mail-so
```

## Quick Start

```javascript
const TempMailSo = require('temp-mail-so');

// Initialize client
const client = new TempMailSo('YOUR_RAPIDAPI_KEY', 'YOUR_AUTH_TOKEN');

// Create temporary inbox
async function createTemporaryInbox() {
    try {
        // Get available domains
        const domains = await client.getDomains();
        
        // Create inbox (prefix, domain, lifetime in seconds)
        const inbox = await client.createInbox('test', domains[0], 1800);
        console.log('New inbox:', inbox);
        
        // Get received emails
        const emails = await client.listMails(inbox.id);
        console.log('Received emails:', emails);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## API Documentation

### Initialization

```javascript
const client = new TempMailSo(rapidApiKey, authToken);
```

### Available Methods

#### getDomains()
Get list of available domains
```javascript
const domains = await client.getDomains();
```

#### createInbox(address, domain, lifespan)
Create a new temporary inbox
- `address`: Email prefix
- `domain`: Domain name
- `lifespan`: Lifetime in seconds, available values: 0, 300, 600, 900, 1200, 1800

```javascript
const inbox = await client.createInbox('test', 'example.com', 1800);
```

#### listInboxes()
Get list of all inboxes
```javascript
const inboxes = await client.listInboxes();
```

#### deleteInbox(inboxId)
Delete specified inbox
```javascript
await client.deleteInbox('inbox_id');
```

#### listMails(inboxId)
Get all emails from specified inbox
```javascript
const emails = await client.listMails('inbox_id');
```

#### getMail(inboxId, mailId)
Get detailed content of specified email
```javascript
const email = await client.getMail('inbox_id', 'mail_id');
```

#### deleteMail(inboxId, mailId)
Delete specified email
```javascript
await client.deleteMail('inbox_id', 'mail_id');
```

## Error Handling

The SDK uses Promises for asynchronous operations. We recommend using try-catch for error handling:

```javascript
try {
    const inbox = await client.createInbox('test', 'example.com', 1800);
} catch (error) {
    console.error('Failed to create inbox:', error.message);
}
```

## License

MIT License - See [LICENSE](LICENSE) file for more details.

## Links

- [TempMail.so Website](https://tempmail.so)
- [API Documentation](https://tempmail.so/temp-mail-api)
- [Issue Tracker](https://github.com/TempMailAPI/Temp-Mail-API/issues)

## Support

If you encounter any issues while using this SDK, please get help through the following channels:

1. Check the [API Documentation](https://tempmail.so/temp-mail-api)
2. Submit a [GitHub Issue](https://github.com/TempMailAPI/Temp-Mail-API/issues)
3. Contact [Technical Support](https://tempmail.so/contact)
