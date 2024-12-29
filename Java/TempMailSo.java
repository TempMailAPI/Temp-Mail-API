/**
 * TempMailSo SDK
 * A Java SDK for the TempMailSo API (https://tempmail.so)
 * 
 * This SDK provides methods to:
 * - List available domains
 * - Create temporary inboxes
 * - List all inboxes
 * - Delete inboxes
 * - List emails in an inbox
 * - Retrieve email details
 * - Delete emails
 * 
 * @author TempMailSo SDK Team
 * @version 1.0.0
 */

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

public class TempMailSo {
    private final String apiKey;
    private final String authToken;
    private final String baseUrl = "https://tempmail-so.p.rapidapi.com";
    private final HttpClient client;

    /**
     * Initialize TempMailSo client
     * @param apiKey RapidAPI key
     * @param authToken TempMailSo authorization token
     */
    public TempMailSo(String apiKey, String authToken) {
        this.apiKey = apiKey;
        this.authToken = authToken;
        this.client = HttpClient.newHttpClient();
    }

    /**
     * List all available domains
     * @return JSON response containing available domains
     */
    public String listDomains() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/domains"))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .GET()
            .build();

        return sendRequest(request);
    }

    /**
     * Create a new temporary inbox
     * @param address Custom email prefix
     * @param domain Selected domain
     * @param lifespan Lifespan in seconds (0, 300, 600, 900, 1200, 1800)
     * @return JSON response containing inbox details
     */
    public String createInbox(String address, String domain, int lifespan) throws IOException, InterruptedException {
        String formData = String.format("name=%s&domain=%s&lifespan=%d", address, domain, lifespan);
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes"))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        return sendRequest(request);
    }

    /**
     * List all inboxes
     * @return JSON response containing all inboxes
     */
    public String listInboxes() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes"))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .GET()
            .build();

        return sendRequest(request);
    }

    /**
     * Delete an inbox
     * @param inboxId ID of the inbox to delete
     * @return JSON response confirming deletion
     */
    public String deleteInbox(String inboxId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes/" + inboxId))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .DELETE()
            .build();

        return sendRequest(request);
    }

    /**
     * List all emails in an inbox
     * @param inboxId ID of the inbox
     * @return JSON response containing emails
     */
    public String listEmails(String inboxId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes/" + inboxId + "/mails"))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .GET()
            .build();

        return sendRequest(request);
    }

    /**
     * Get details of a specific email
     * @param inboxId ID of the inbox
     * @param emailId ID of the email
     * @return JSON response containing email details
     */
    public String getEmail(String inboxId, String emailId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes/" + inboxId + "/mails/" + emailId))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .GET()
            .build();

        return sendRequest(request);
    }

    /**
     * Delete a specific email
     * @param inboxId ID of the inbox
     * @param emailId ID of the email to delete
     * @return JSON response confirming deletion
     */
    public String deleteEmail(String inboxId, String emailId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/inboxes/" + inboxId + "/mails/" + emailId))
            .header("x-rapidapi-key", apiKey)
            .header("Authorization", "Bearer " + authToken)
            .DELETE()
            .build();

        return sendRequest(request);
    }

    // Helper method to send HTTP requests
    private String sendRequest(HttpRequest request) throws IOException, InterruptedException {
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        return response.body();
    }
} 