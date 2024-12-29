/**
 * TempMail.so API SDK Usage Example
 */

const TempMailSo = require('../src/TempMailSo');

// Replace with your actual keys
const RAPID_API_KEY = 'your-rapid-api-key';
const AUTH_TOKEN = 'your-auth-token';

async function main() {
    try {
        // Create client instance
        const client = new TempMailSo(RAPID_API_KEY, AUTH_TOKEN);

        // 1. Get available domains
        console.log('Getting available domains...');
        const domains = await client.getDomains();
        console.log('Available domains:', domains);

        // 2. Create temporary inbox
        console.log('\nCreating temporary inbox...');
        const inbox = await client.createInbox('test123', 'mailnuo.com', 600);
        console.log('Created inbox:', inbox);

        // 3. Get all inboxes
        console.log('\nGetting inbox list...');
        const inboxes = await client.listInboxes();
        console.log('Inbox list:', inboxes);

        // 4. Get email list
        console.log('\nGetting email list...');
        const mails = await client.listMails(inbox.id);
        console.log('Email list:', mails);

        // If there are emails, get details of the first email
        if (mails && mails.length > 0) {
            console.log('\nGetting email details...');
            const mailDetail = await client.getMail(inbox.id, mails[0].id);
            console.log('Email details:', mailDetail);

            // Delete email
            console.log('\nDeleting email...');
            await client.deleteMail(inbox.id, mails[0].id);
            console.log('Email deleted');
        }

        // 5. Finally delete the inbox
        console.log('\nDeleting inbox...');
        await client.deleteInbox(inbox.id);
        console.log('Inbox deleted');

    } catch (error) {
        console.error('Error occurred:', error.message);
    }
}

// Run example
main(); 
