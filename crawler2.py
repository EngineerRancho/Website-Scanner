import requests

# url = "mail.google.com"

web_name = input(" Enter the website domain : ")
def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = web_name
# with open("/home/rancho/Hacking_Tools_by_Engineer_Rancho/Website Scanner/url_filenames.txt", "r") as wordlist_file:
with open("url_filenames.txt", "r") as wordlist_file:
    # content = wordlist_file.read()
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + ("/") + word
        # print((test_url))
        response = request(test_url)
        if response:
            print((" [+] Discovered URL --> " + test_url))