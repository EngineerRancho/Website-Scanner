import requests

def scan_subdomains(web_name):
    target_url = web_name
    # with open("/home/rancho/Hacking_Tools_by_Engineer_Rancho/Website Scanner/subdomain_test.txt", "r") as wordlist_file:
    with open("subdomain_test.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                print(" [-] Discovered domain --> " + test_url)

def scan_urls(web_name):
    target_url = web_name
    # with open("/home/rancho/Hacking_Tools_by_Engineer_Rancho/Website Scanner/url_filenames.txt", "r") as wordlist_file:
    with open("/url_filenames.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print(" [+] Discovered URL --> " + test_url)

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

web_name = input("Enter the website domain: ")
print("[1] Subdomains")
print("[2] URL files")
print("[3] Both(time taking) - Not recomended")
choice = input("Pass Scan Type ")

if choice == '1':
    scan_subdomains(web_name)
elif choice == '2':
    scan_urls(web_name)
elif choice == '3':
    scan_subdomains(web_name)
    scan_urls(web_name)
else:
    print("Invalid choice")