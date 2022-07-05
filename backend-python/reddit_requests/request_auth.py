import requests, requests.auth, config

headers = { "User-Agent": config.USER_AGENT }

client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)

post_data = {
    "grant_type": "password", 
    "username": config.USERNAME, 
    "password": config.PASSWORD,
}

def get_access_token():
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token", 
        auth = client_auth, 
        data = post_data, 
        headers = headers,
    ).json()

    print(response["access_token"])
    return response["access_token"]

'''
Unfortunately, "App-only OAuth token requests never receive a refresh_token"

Clients must authenticate with OAuth2
Clients connecting via OAuth2 may make up to 60 requests per minute. 
Access tokens expire after 1 hour. 
Trying to request without a token will result in 401 Unauthorized.
https://www.reddit.com/prefs/apps


Monitor the following response headers to ensure that you're not exceeding the limits:
    X-Ratelimit-Used: Approximate number of requests used in this period
    X-Ratelimit-Remaining: Approximate number of requests left to use
    X-Ratelimit-Reset: Approximate number of seconds to end of period


Change your client's User-Agent string to something unique and descriptive, including the target platform, a unique application identifier, a version string, and your username as contact information, in the following format: <platform>:<app ID>:<version string> (by /u/<reddit username>)
    Example: User-Agent: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
    Many default User-Agents (like "Python/urllib" or "Java") are drastically limited to encourage unique and descriptive user-agent strings.
    Including the version number and updating it as you build your application allows us to safely block old buggy/broken versions of your app.
    NEVER lie about your user-agent. This includes spoofing popular browsers and spoofing other bots. We will ban liars with extreme prejudice.


Resources for using the Reddit API with Python and OAuth
- https://github.com/reddit-archive/reddit/wiki/OAuth2-Python-Example
- https://github.com/reddit-archive/reddit/wiki/API
- https://www.reddit.com/wiki/api
- https://www.reddit.com/dev/api/

'''