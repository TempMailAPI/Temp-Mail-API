# TempMail.so API SDK

A **Node.js** client for interacting with the [TempMail.so](https://tempmail.so) API, enabling developers to easily create and manage temporary email inboxes within their applications.

## Features

- **Create Temporary Mailboxes**: Generate disposable email addresses with customizable lifespans.
- **Manage Mailbox Lifecycle**: List, update, and delete temporary inboxes as needed.
- **Receive and Manage Emails**: Retrieve, view, and delete emails received in your temporary inboxes.
- **Seamless Integration**: Built with `axios` for efficient HTTP requests and easy integration into your Node.js projects.

## Usage

```javascript
const TempMailSo = require('TempMailSo');

// Initialize the TempMailSo client with your RapidAPI Key and Auth Token
const tempMail = new TempMailSo('YOUR_RAPIDAPI_KEY', 'YOUR_AUTH_TOKEN');

(async () => {
    try {
        // Get available domains
        const domains = await tempMail.getDomains();
        console.log('Available Domains:', domains);

        // Create a new temporary inbox
        const inbox = await tempMail.createInbox('mytempemail', domains[0], 600);
        console.log('Created Inbox:', inbox);

        // List all inboxes
        const inboxes = await tempMail.listInboxes();
        console.log('All Inboxes:', inboxes);

        // List emails in a specific inbox
        const mails = await tempMail.listMails(inbox.id);
        console.log('Emails:', mails);

        if (mails.length > 0) {
            // Get details of the first email
            const mailDetails = await tempMail.getMail(inbox.id, mails[0].id);
            console.log('Email Details:', mailDetails);

            // Delete the email
            const deleteMailResult = await tempMail.deleteMail(inbox.id, mails[0].id);
            console.log('Deleted Email:', deleteMailResult);
        }

        // Delete the inbox
        const deleteInboxResult = await tempMail.deleteInbox(inbox.id);
        console.log('Deleted Inbox:', deleteInboxResult);
    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
    }
})();
```

## API Reference

### `constructor(rapidApiKey, authToken)`

Creates an instance of the TempMailSo client.

- `rapidApiKey` *(string)*: Your RapidAPI Key.
- `authToken` *(string)*: Your TempMail.so Authorization Token.

### `getDomains()`

Retrieves a list of available email domains.

- **Returns**: `Promise<Array>` - List of available domains.

### `createInbox(address, domain, lifespan)`

Creates a new temporary inbox.

- `address` *(string)*: Email prefix.
- `domain` *(string)*: Domain name.
- `lifespan` *(number)*: Lifetime in seconds (available values: 0, 300, 600, 900, 1200, 1800).

- **Returns**: `Promise<Object>` - Created inbox information.

### `listInboxes()`

Lists all existing inboxes.

- **Returns**: `Promise<Array>` - List of inboxes.

### `deleteInbox(inboxId)`

Deletes a specified inbox.

- `inboxId` *(string)*: Inbox ID.

- **Returns**: `Promise<Object>` - Delete result.

### `listMails(inboxId)`

Retrieves all emails from a specified inbox.

- `inboxId` *(string)*: Inbox ID.

- **Returns**: `Promise<Array>` - List of emails.

### `getMail(inboxId, mailId)`

Gets detailed content of a specified email.

- `inboxId` *(string)*: Inbox ID.
- `mailId` *(string)*: Email ID.

- **Returns**: `Promise<Object>` - Detailed email content.

### `deleteMail(inboxId, mailId)`

Deletes a specified email.

- `inboxId` *(string)*: Inbox ID.
- `mailId` *(string)*: Email ID.

- **Returns**: `Promise<Object>` - Delete result.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

---

For more information, visit the [TempMail.so](https://tempmail.so) website.
