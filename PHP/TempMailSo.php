<?php

/**
 * TempMailAPI SDK
 * 
 * This PHP SDK provides methods to interact with the TempMail.so API.
 * Features include managing temporary email inboxes, retrieving mails,
 * and performing actions such as inbox or mail deletion.
 * 
 * Usage:
 * - Initialize the class with your RapidAPI key and authentication token.
 * - Call the provided methods to utilize TempMail.so API functionalities.
 * 
 * Note: Replace `YOUR_RAPIDAPI_KEY` and `YOUR_AUTH_TOKEN` with your actual credentials.
 * 
 * Author: TempMail.so
 * License: TempMail.so
 */

class TempMailAPI
{
    private $apiKey;
    private $authToken;
    private $baseUrl = 'https://tempmail-so.p.rapidapi.com';

    public function __construct($apiKey, $authToken)
    {
        $this->apiKey = $apiKey;
        $this->authToken = $authToken;
    }

    private function request($method, $endpoint, $data = null)
    {
        $url = $this->baseUrl . $endpoint;
        $headers = [
            'x-rapidapi-key: ' . $this->apiKey,
            'Authorization: Bearer ' . $this->authToken,
            'Content-Type: application/json'
        ];

        $options = [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST => $method,
            CURLOPT_HTTPHEADER => $headers
        ];

        if ($data) {
            $options[CURLOPT_POSTFIELDS] = json_encode($data);
        }

        $ch = curl_init($url);
        curl_setopt_array($ch, $options);
        $response = curl_exec($ch);
        $error = curl_error($ch);
        curl_close($ch);

        if ($error) {
            throw new Exception('Request Error: ' . $error);
        }

        return json_decode($response, true);
    }

    // Get available domains
    public function listDomains()
    {
        return $this->request('GET', '/domains');
    }

    // Create a new inbox
    public function createInbox($name, $domain, $lifespan)
    {
        $data = [
            'name' => $name,
            'domain' => $domain,
            'lifespan' => $lifespan
        ];
        return $this->request('POST', '/inboxes', $data);
    }

    // Retrieve all inboxes
    public function listInboxes()
    {
        return $this->request('GET', '/inboxes');
    }

    // Delete an inbox
    public function deleteInbox($inboxId)
    {
        return $this->request('DELETE', '/inboxes/' . $inboxId);
    }

    // Get the list of mails in an inbox
    public function listMails($inboxId)
    {
        return $this->request('GET', '/inboxes/' . $inboxId . '/mails');
    }

    // Retrieve details of a specific mail
    public function getMail($inboxId, $mailId)
    {
        return $this->request('GET', '/inboxes/' . $inboxId . '/mails/' . $mailId);
    }

    // Delete a mail
    public function deleteMail($inboxId, $mailId)
    {
        return $this->request('DELETE', '/inboxes/' . $inboxId . '/mails/' . $mailId);
    }
  
}

?>
