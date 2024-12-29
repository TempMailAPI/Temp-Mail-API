/**
 * Example usage of TempMailSo SDK
 */
public class Example {
    public static void main(String[] args) {
        // Initialize client with your API keys
        TempMailSo client = new TempMailSo("your-rapidapi-key", "your-auth-token");

        try {
            // List available domains
            System.out.println("Available domains:");
            System.out.println(client.listDomains());

            // Create a new inbox
            System.out.println("\nCreating new inbox:");
            String inboxResponse = client.createInbox("test123", "mailnuo.com", 600);
            System.out.println(inboxResponse);

            // List all inboxes
            System.out.println("\nListing all inboxes:");
            System.out.println(client.listInboxes());

            // Assuming we have an inbox ID and email ID
            String inboxId = "your-inbox-id";
            String emailId = "your-email-id";

            // List emails in inbox
            System.out.println("\nListing emails in inbox:");
            System.out.println(client.listEmails(inboxId));

            // Get specific email
            System.out.println("\nGetting specific email:");
            System.out.println(client.getEmail(inboxId, emailId));

            // Delete email
            System.out.println("\nDeleting email:");
            System.out.println(client.deleteEmail(inboxId, emailId));

            // Delete inbox
            System.out.println("\nDeleting inbox:");
            System.out.println(client.deleteInbox(inboxId));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
} 