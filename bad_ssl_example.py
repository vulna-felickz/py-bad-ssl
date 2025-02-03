import ssl
import urllib.request

def create_insecure_ssl_context():
    # BAD: Using an old version of SSL and not doing certificate checking
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    context.check_hostname = False
    return context

def fetch_url(url):
    context = create_insecure_ssl_context()
    with urllib.request.urlopen(url, context=context) as response:
        return response.read()

if __name__ == "__main__":
    url = "https://example.com"
    try:
        content = fetch_url(url)
        print(content)
    except Exception as e:
        print(f"Failed to fetch URL: {e}")
