# TempMailAPI SDK for PHP

The **TempMailAPI SDK** is a PHP library designed to simplify interaction with the [TempMail.so](https://tempmail.so) API. With this SDK, developers can easily manage temporary email inboxes, retrieve messages, and perform various inbox and message-related actions.

## Features

- **Domain Management**: Retrieve the list of available email domains.
- **Inbox Management**: Create, list, and delete temporary email inboxes.
- **Message Management**: Retrieve messages from inboxes, view message details, and delete messages.
- **Easy Integration**: Simple and clean methods for interacting with the TempMail.so API.

## Requirements

- PHP 7.2 or higher
- cURL extension enabled
- A [RapidAPI key](https://rapidapi.com/) and a TempMail.so authentication token.

## Installation

Include the class in your PHP project:

    require_once 'TempMailAPI.php';

## Usage

1. Initialize the `TempMailAPI` class with your RapidAPI key and TempMail.so authentication token:

```php
$apiKey = 'YOUR_RAPIDAPI_KEY';
$authToken = 'YOUR_AUTH_TOKEN';

$tempMail = new TempMailAPI($apiKey, $authToken);
```

2. Use the provided methods to interact with the TempMail.so API:

### Example: List Available Domains

```php
$domains = $tempMail->listDomains();
print_r($domains);
```

### Example: Create a New Inbox

```php
$name = 'example';
$domain = 'tempmail.so';
$lifespan = 3600; // Inbox lifespan in seconds

$newInbox = $tempMail->createInbox($name, $domain, $lifespan);
print_r($newInbox);
```

### Example: List Inboxes

```php
$inboxes = $tempMail->listInboxes();
print_r($inboxes);
```

### Example: Retrieve Messages

```php
$inboxId = 'INBOX_ID_HERE';

$messages = $tempMail->listMessages($inboxId);
print_r($messages);
```

## Error Handling

If a request fails, the SDK throws an `Exception` with details about the error:

```php
try {
    $domains = $tempMail->listDomains();
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
```

## License

This SDK is licensed under the **TempMail.so** terms. See the repository for details.

## Contributing

Feel free to open issues or submit pull requests to enhance the SDK.

---

Make sure to replace placeholders like `YOUR_RAPIDAPI_KEY` and `YOUR_AUTH_TOKEN` with actual credentials in your implementation.
