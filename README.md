# Bulk Indexing with Google Indexing API

This script streamlines the process of indexing multiple pages of your website on Google, eliminating the need for individual URL submissions through the Search Console interface.

## Require

Use several Python libraries such as `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, `requests`, and `json`. First, you need to install these libraries if you haven't already. You can do this using pip:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 requests
```

Begin by setting up access to the Indexing API on the Google Cloud Platform. Follow these instructions to get started:

[Google Indexing API Setup Guide](https://developers.google.com/search/apis/indexing-api/v3/prereqs)

After gaining access, download the public/private key pair JSON file, named "service_account.json". This file contains your essential credentials.

Prepare a file named urls.txt and list all URLs you wish to have crawled/indexed.

## Site Ownership Verification in Search Console for URL Indexing

Ensure you have verified ownership of your website to submit URLs for indexing.

Locate your service account email address (found in "service_account.json" under client_email) and add it as a delegated owner of your web property in Search Console. This email is also visible in the Service Accounts section of the Developer Console and follows a format like "my-service-account@test-project-42.google.com.iam.gserviceaccount.com".

## To verify ownership:

1. Visit Google Webmaster Central.
2. Select your verified property.
3. Navigate to 'Add an owner'.
4. Enter your service account email as an owner of the property.

## Indexing Quotas

Maximum of 100 URLs per batch request.
Limit of 200 URLs per day.
