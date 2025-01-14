# How to Check API Usage and Remaining Requests for TempMail.so

This guide explains how to retrieve the remaining API request quota and rate limit information from the TempMail.so API. The steps are described in a way that is applicable to all programming languages, ensuring ease of implementation.

## Steps to Retrieve Rate Limit Information

### 1. Prepare Your API Credentials
You will need the following to authenticate your API requests:
- **`x-rapidapi-key`**: Your API key from RapidAPI.
- **`Authorization` token**: A bearer token provided by TempMail.so.

### 2. Construct Your API Request
Send an HTTP `GET` request to the following endpoint:
```
https://tempmail-so.p.rapidapi.com/domains
```

Include the following headers in your request:
- **`x-rapidapi-key`**: Your RapidAPI key.
- **`Authorization`**: A bearer token in the format `Bearer <your_auth_token>`.
- **`Content-Type`**: Set this to `application/x-www-form-urlencoded`.

### 3. Check the Response Headers
After the API responds, look at the response headers to find the following information about your API usage:
- **`X-RateLimit-Requests-Limit`**: The total number of API requests allowed per day.
- **`X-RateLimit-Requests-Remaining`**: The number of requests remaining for the current day.
- **`X-RateLimit-Requests-Reset`**: The number of seconds until the daily limit resets.

### 4. Interpret the Results
These headers allow you to monitor your API usage and manage it effectively:
- **Example**: If the header `X-RateLimit-Requests-Limit` shows `1000` and `X-RateLimit-Requests-Remaining` shows `800`, it means you have 800 requests left out of a daily limit of 1000.

## Adapting to Your Programming Language
The process described above is not language-specific. You can use any HTTP client library available in your preferred programming language to:
1. Send a `GET` request to the TempMail.so API.
2. Include the required headers.
3. Extract the rate limit information from the response headers.

For example:
- In JavaScript, use libraries like `axios` or `fetch`.
- In Java, you might use `HttpURLConnection` or libraries like `OkHttp`.
- In C#, the `HttpClient` class is commonly used.

### Example Workflow
1. Construct the HTTP request with the correct endpoint and headers.
2. Send the request.
3. Inspect the response headers for `X-RateLimit-Requests-Limit`, `X-RateLimit-Requests-Remaining`, and `X-RateLimit-Requests-Reset`.

## Troubleshooting Tips
- **Invalid API Key**: Ensure that the `x-rapidapi-key` is correct and active.
- **Expired Authorization Token**: Verify that the `Authorization` token is valid and has not expired.
- **Missing Headers**: If the expected headers are not present in the response, confirm that the endpoint and request headers are correct.

## Additional Information
For more details about the TempMail.so API, refer to the [official documentation](https://tempmail.so/temp-mail-api).
