import ssl
import urllib.request

def create_insecure_ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23) #This is an alias to PROTOCOL_TLS - which when coupled with SSLContext will by default disable SSLv2/v3 (see https://docs.python.org/3/library/ssl.html#ssl.SSLContext)

    # Ensure that options to disable SSLv2 and SSLv3 are not set (default behavior)
    context.options &= ~ssl.OP_NO_SSLv2
    context.options &= ~ssl.OP_NO_SSLv3

    
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
