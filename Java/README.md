# Temp Mail API SDK

The TempMailSo SDK is a Java-based library that allows developers to interact with the TempMailSo API for managing temporary email addresses. This SDK simplifies the process of integrating TempMailSo's email services into Java applications.

### Key Features:
- **List Available Domains**: Retrieve a list of available temporary email domains.
- **Create Temporary Inboxes**: Easily create temporary inboxes with custom prefixes, selected domains, and lifespan settings.
- **Manage Inboxes**: List, delete, or fetch details of temporary inboxes.
- **Manage Emails**: List, retrieve details, and delete emails from a specific inbox.

### Supported Operations:
- List available email domains
- Create and manage temporary inboxes
- List and manage emails within an inbox
- Delete inboxes and emails

### Requirements:
- A valid RapidAPI key for authentication
- TempMailSo authorization token

### Installation:

1. Import the `TempMailSo` class into your Java project.
2. Initialize the SDK with your RapidAPI key and TempMailSo authorization token.

### Usage Example:
```java
TempMailSo tempMail = new TempMailSo("your-api-key", "your-auth-token");

// List available domains
String domains = tempMail.listDomains();

// Create a new inbox
String inbox = tempMail.createInbox("myaddress", "tempmail.com", 300);

// List all inboxes
String inboxes = tempMail.listInboxes();

// Delete an inbox
String result = tempMail.deleteInbox("inboxId");

// List all emails in an inbox
String emails = tempMail.listEmails("inboxId");
```

For detailed documentation, please refer to the [TempMailSo API documentation](https://tempmail.so).
