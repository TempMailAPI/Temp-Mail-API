using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Text;

/*
 * TempMail.so SDK
 * 
 * This SDK provides a simple interface to interact with TempMail.so's API
 * for creating and managing temporary email addresses.
 * 
 * Features:
 * - Create temporary email inboxes
 * - List available domains
 * - Manage inboxes and emails
 * - Retrieve email contents
 * 
 * Author: TempMail.so
 * Version: 1.0.0
 * Documentation: https://tempmail.so/us/blog/how-to-use-the-temporary-email-service-api
 */

public class TempMailSo
{
    private readonly HttpClient _httpClient;
    private readonly string _apiKey;
    private readonly string _authToken;
    private const string BaseUrl = "https://tempmail-so.p.rapidapi.com";

    public TempMailSo(string apiKey, string authToken)
    {
        _apiKey = apiKey;
        _authToken = authToken;
        _httpClient = new HttpClient();
        _httpClient.DefaultRequestHeaders.Add("x-rapidapi-key", _apiKey);
        _httpClient.DefaultRequestHeaders.Add("Authorization", $"Bearer {_authToken}");
    }

    // Get list of available domains
    public async Task<List<DomainInfo>> GetDomainsAsync()
    {
        var response = await SendRequestAsync<DomainsResponse>(HttpMethod.Get, "/domains");
        return response.Data;
    }

    // Create a new inbox
    public async Task<string> CreateInboxAsync(string address, string domain, int lifespan)
    {
        var content = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("name", address),
            new KeyValuePair<string, string>("domain", domain),
            new KeyValuePair<string, string>("lifespan", lifespan.ToString())
        });

        var response = await SendRequestAsync<CreateInboxResponse>(HttpMethod.Post, "/inboxes", content);
        return response.Data.Id;
    }

    // Get all inboxes
    public async Task<List<InboxInfo>> GetInboxesAsync()
    {
        var response = await SendRequestAsync<InboxesResponse>(HttpMethod.Get, "/inboxes");
        return response.Data;
    }

    // Delete an inbox
    public async Task<string> DeleteInboxAsync(string inboxId)
    {
        var response = await SendRequestAsync<DeleteResponse>(HttpMethod.Delete, $"/inboxes/{inboxId}");
        return response.Data.Id;
    }

    // Get all emails in an inbox
    public async Task<List<EmailInfo>> GetEmailsAsync(string inboxId)
    {
        var response = await SendRequestAsync<EmailsResponse>(HttpMethod.Get, $"/inboxes/{inboxId}/mails");
        return response.Data;
    }

    // Get specific email content
    public async Task<EmailContent> GetEmailContentAsync(string inboxId, string emailId)
    {
        var response = await SendRequestAsync<EmailContentResponse>(HttpMethod.Get, $"/inboxes/{inboxId}/mails/{emailId}");
        return response.Data;
    }

    // Delete specific email
    public async Task<string> DeleteEmailAsync(string inboxId, string emailId)
    {
        var response = await SendRequestAsync<DeleteResponse>(HttpMethod.Delete, $"/inboxes/{inboxId}/mails/{emailId}");
        return response.Data.Id;
    }

    // Helper method to send HTTP requests
    private async Task<T> SendRequestAsync<T>(HttpMethod method, string endpoint, HttpContent content = null)
    {
        var request = new HttpRequestMessage(method, $"{BaseUrl}{endpoint}");
        if (content != null)
        {
            request.Content = content;
        }

        var response = await _httpClient.SendAsync(request);
        response.EnsureSuccessStatusCode();
        
        var jsonString = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<T>(jsonString);
    }

    // Response models
    private class BaseResponse<T>
    {
        public string RequestId { get; set; }
        public string Message { get; set; }
        public T Data { get; set; }
        public int Code { get; set; }
    }

    private class DomainsResponse : BaseResponse<List<DomainInfo>> { }
    private class CreateInboxResponse : BaseResponse<IdResponse> { }
    private class InboxesResponse : BaseResponse<List<InboxInfo>> { }
    private class EmailsResponse : BaseResponse<List<EmailInfo>> { }
    private class EmailContentResponse : BaseResponse<EmailContent> { }
    private class DeleteResponse : BaseResponse<IdResponse> { }

    private class IdResponse
    {
        public string Id { get; set; }
    }
}

// Public models
public class DomainInfo
{
    public string Domain { get; set; }
    public bool? Alternate { get; set; }
    public bool? Custom { get; set; }
}

public class InboxInfo
{
    public long Created { get; set; }
    public int Lifespan { get; set; }
    public string Id { get; set; }
    public string Name { get; set; }
    public bool Permanent { get; set; }
}

public class EmailInfo
{
    public long Received { get; set; }
    public string From { get; set; }
    public bool Read { get; set; }
    public string Id { get; set; }
    public string Subject { get; set; }
}

public class EmailContent
{
    public string TextContent { get; set; }
    public bool Forwarded { get; set; }
    public string HtmlContent { get; set; }
    public long Received { get; set; }
    public string From { get; set; }
    public bool Read { get; set; }
    public string Id { get; set; }
    public string Subject { get; set; }
} 
