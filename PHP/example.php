<?php

require_once('TempMailSo.php');

// Usage example
$apiKey = 'YOUR_RAPIDAPI_KEY';
$authToken = 'YOUR_AUTH_TOKEN';

$tempMail = new TempMailAPI($apiKey, $authToken);

try {
    // Get available domains
    $domains = $tempMail->listDomains();
    print_r($domains);

    // Create a new inbox
    $newInbox = $tempMail->createInbox('example', 'mailnuo.com', 600);
    print_r($newInbox);

    // Retrieve all inboxes
    $inboxes = $tempMail->listInboxes();
    print_r($inboxes);

    // Retrieve details of a single inbox
    if (!empty($inboxes['data'])) {
        $inboxId = $inboxes['data'][0]['id'];

        // Get the list of messages in the inbox
        $messages = $tempMail->listMails($inboxId);
        print_r($messages);

        // Retrieve details of a specific message
        if (!empty($messages['data'])) {
            $mailId = $messages['data'][0]['id'];
            $messageDetails = $tempMail->getMail($inboxId, $mailId);
            print_r($messageDetails);

            // Delete the message
            $deleteMessage = $tempMail->deleteMail($inboxId, $mailId);
            print_r($deleteMessage);
        }

        // Delete the inbox
        $deleteInbox = $tempMail->deleteInbox($inboxId);
        print_r($deleteInbox);
    }
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}

?>
