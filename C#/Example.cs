using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Initialize the client with your API credentials
        var client = new TempMailSo(
            apiKey: "your-rapidapi-key",
            authToken: "your-auth-token"
        );

        try
        {
            // Get available domains
            Console.WriteLine("Getting available domains...");
            var domains = await client.GetDomainsAsync();
            foreach (var domain in domains)
            {
                Console.WriteLine($"Domain: {domain.Domain}");
            }

            // Create a new inbox
            Console.WriteLine("\nCreating new inbox...");
            var inboxId = await client.CreateInboxAsync(
                address: "test123",
                domain: domains[0].Domain,
                lifespan: 600 // 10 minutes
            );
            Console.WriteLine($"Created inbox with ID: {inboxId}");

            // List all inboxes
            Console.WriteLine("\nListing all inboxes...");
            var inboxes = await client.GetInboxesAsync();
            foreach (var inbox in inboxes)
            {
                Console.WriteLine($"Inbox: {inbox.Name} (ID: {inbox.Id})");
            }

            // Get emails in the inbox
            Console.WriteLine("\nChecking for emails...");
            var emails = await client.GetEmailsAsync(inboxId);
            foreach (var email in emails)
            {
                Console.WriteLine($"Email: {email.Subject} from {email.From}");

                // Get email content
                var content = await client.GetEmailContentAsync(inboxId, email.Id);
                Console.WriteLine($"Content: {content.TextContent}");
            }

            // Delete the inbox
            Console.WriteLine("\nDeleting inbox...");
            await client.DeleteInboxAsync(inboxId);
            Console.WriteLine("Inbox deleted successfully");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
} 