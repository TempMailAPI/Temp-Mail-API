/**
 * TempMail.so API SDK
 * A Node.js client for interacting with TempMail.so API
 * 
 * @link https://tempmail.so/temp-mail-api
 * 
 * Features:
 * - Create temporary mailboxes
 * - Manage mailbox lifecycle
 * - Receive and manage emails
 * 
 * @author TempMail.so
 */

const axios = require('axios');

class TempMailSo {
    /**
     * @param {string} rapidApiKey - RapidAPI Key
     * @param {string} authToken - TempMail.so Authorization Token
     */
    constructor(rapidApiKey, authToken) {
        this.baseURL = 'https://tempmail-so.p.rapidapi.com';
        this.client = axios.create({
            baseURL: this.baseURL,
            headers: {
                'x-rapidapi-key': rapidApiKey,
                'Authorization': `Bearer ${authToken}`,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
    }

    /**
     * Get list of available domains
     * @returns {Promise<Array>} List of available domains
     */
    async getDomains() {
        const response = await this.client.get('/domains');
        return response.data.data;
    }

    /**
     * Create a new temporary inbox
     * @param {string} address - Email prefix
     * @param {string} domain - Domain name
     * @param {number} lifespan - Lifetime in seconds, available values: 0, 300, 600, 900, 1200, 1800
     * @returns {Promise<Object>} Created inbox information
     */
    async createInbox(address, domain, lifespan) {
        const params = new URLSearchParams();
        params.append('name', address);
        params.append('domain', domain);
        params.append('lifespan', lifespan);

        const response = await this.client.post('/inboxes', params);
        return response.data.data;
    }

    /**
     * Get list of all inboxes
     * @returns {Promise<Array>} List of inboxes
     */
    async listInboxes() {
        const response = await this.client.get('/inboxes');
        return response.data.data;
    }

    /**
     * Delete specified inbox
     * @param {string} inboxId - Inbox ID
     * @returns {Promise<Object>} Delete result
     */
    async deleteInbox(inboxId) {
        const response = await this.client.delete(`/inboxes/${inboxId}`);
        return response.data.data;
    }

    /**
     * Get all emails from specified inbox
     * @param {string} inboxId - Inbox ID
     * @returns {Promise<Array>} List of emails
     */
    async listMails(inboxId) {
        const response = await this.client.get(`/inboxes/${inboxId}/mails`);
        return response.data.data;
    }

    /**
     * Get detailed content of specified email
     * @param {string} inboxId - Inbox ID
     * @param {string} mailId - Email ID
     * @returns {Promise<Object>} Detailed email content
     */
    async getMail(inboxId, mailId) {
        const response = await this.client.get(`/inboxes/${inboxId}/mails/${mailId}`);
        return response.data.data;
    }

    /**
     * Delete specified email
     * @param {string} inboxId - Inbox ID
     * @param {string} mailId - Email ID
     * @returns {Promise<Object>} Delete result
     */
    async deleteMail(inboxId, mailId) {
        const response = await this.client.delete(`/inboxes/${inboxId}/mails/${mailId}`);
        return response.data.data;
    }
}

module.exports = TempMailSo;
