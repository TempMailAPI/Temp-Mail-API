# TempMail.so C# SDK

A C# SDK for interacting with the [TempMail.so](https://tempmail.so) API to create and manage temporary email addresses.

## Features

- Create temporary email inboxes
- List available domains
- Manage inboxes and emails
- Retrieve email contents
- Full async/await support
- Strong typed models
- Simple and intuitive API

## Installation

1. Copy `TempMailSo.cs` to your project
2. Add the following NuGet packages:
   - System.Text.Json
   - System.Net.Http

## Prerequisites

To use this SDK, you'll need:

- A RapidAPI key from [TempMail.so RapidAPI page](https://rapidapi.com/tempmail-api/api/tempmail-so)
- An auth token from TempMail.so
- .NET Core 3.1 or later

## Quick Start

```csharp
// Initialize the client
var client = new TempMailSoClient("YOUR_RAPIDAPI_KEY", "YOUR_AUTH_TOKEN");

// Create a new inbox
var inbox = await client.CreateInboxAsync();
Console.WriteLine($"New email address: {inbox.Email}");

// Get available domains
var domains = await client.GetDomainsAsync();
foreach (var domain in domains)
{
    Console.WriteLine($"Available domain: {domain}");
}

// Get messages from inbox
var messages = await client.GetMessagesAsync(inbox.Email);
foreach (var message in messages)
{
    Console.WriteLine($"Subject: {message.Subject}");
    
    // Get message details
    var messageDetails = await client.GetMessageAsync(message.Id);
    Console.WriteLine($"Message content: {messageDetails.TextBody}");
}
```

## API Reference

### TempMailSoClient

The main class for interacting with the TempMail.so API.

#### Constructor

```csharp
public TempMailSoClient(string rapidApiKey, string authToken)
```

#### Methods

- `CreateInboxAsync()`: Creates a new temporary email inbox
- `GetDomainsAsync()`: Retrieves list of available domains
- `GetMessagesAsync(string email)`: Gets all messages for a specific email address
- `GetMessageAsync(string messageId)`: Gets detailed information about a specific message
- `DeleteMessageAsync(string messageId)`: Deletes a specific message
- `DeleteInboxAsync(string email)`: Deletes an inbox and all its messages

### Models

#### Inbox
- `Email`: The full email address
- `CreatedAt`: Timestamp of inbox creation

#### Message
- `Id`: Unique message identifier
- `From`: Sender's email address
- `Subject`: Message subject
- `Preview`: Short preview of message content
- `HasAttachments`: Boolean indicating if message has attachments
- `CreatedAt`: Timestamp of message receipt

#### MessageDetails
- `Id`: Unique message identifier
- `From`: Sender's email address
- `Subject`: Message subject
- `TextBody`: Plain text content
- `HtmlBody`: HTML content
- `Attachments`: List of attachments
- `Headers`: Email headers
- `CreatedAt`: Timestamp of message receipt

## Error Handling

The SDK throws `TempMailSoException` when API requests fail. Always wrap API calls in try-catch blocks:

```csharp
try
{
    var inbox = await client.CreateInboxAsync();
}
catch (TempMailSoException ex)
{
    Console.WriteLine($"API Error: {ex.Message}");
}
catch (Exception ex)
{
    Console.WriteLine($"General Error: {ex.Message}");
}
```

## Rate Limiting

The API has rate limits based on your RapidAPI subscription plan. The SDK will throw a `TempMailSoException` with appropriate error message when rate limits are exceeded.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For API-related issues, please contact TempMail.so support through their RapidAPI page.
For SDK-specific issues, please open an issue in this repository.
