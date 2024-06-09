
import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors='ignore'))

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, 'html.parser')
        return parsed_html.find_all("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urljoin(url, action)
        method = form.get("method")

        inputs_list = form.find_all("input")
        post_data = {}
        for input_item in inputs_list:
            input_name = input_item.get("name")
            input_type = input_item.get("type")
            input_value = input_item.get("value")
            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
        
        if method == "post":
            return self.session.post(post_url, data=post_data)
        
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print("[+] Testing Forms in " + link)

            if "=" in link:
                print("[+] Testing" + link)

    def test_xss_in_form(self, form, value, url):
        xss_test_script = "<sCriPt>alert('test')</sCriPt>"
        
        response = self.submit_form(form, xss_test_script, url)
        
        if xss_test_script in response.content.decode():
            return True








# import requests
# import re
# from urllib.parse import urljoin
# from Beautifulsoup import Beautifulsoup

# class Scanner:
#     def __init__(self, url):

#     # def __init__(self, url, ignore_links):
#         self.session = requests.Session()
#         self.target_url = url
#         self.target_links = []
#         # self.links_to_ignore = ignore_links

#     def extract_links_from(self, url):
#         response = self.session.get(url)
#         return re.findall('(?:href=")(.*?)"', response.content.decode(errors='ignore'))

#     def crawl(self, url=None):
#         if url == None:
#             url = self.target_url
#         href_links = self.extract_links_from(url)
#         for link in href_links:
#             link = urljoin(url, link)

#             if "#" in link:
#                 link = link.split("#")[0]

#             if self.target_url in link and link not in self.target_links:
#                 self.target_links.append(link)
#                 print(link)
#                 self.crawl(link)

#     def extract_forms(self, url):
#         response = self.session.get(url)
#         parsed_html = Beautifulsoup(response.content)
#         return parsed_html.findall("form")

#     def submit_form(self, form, value, url):
#         action = form.get("action")
#         post_url = urljoin(url, action)
#         method = form.get("method")

#         inputs_list = form.findall("input")
#         post_data = {}
#         for input in inputs_list:
#             input_name = input.get("name")
#             input_type = input.get("type")
#             input_value = input.get("value")
#             if input_type == "text":
#                 input_value = value

#             post_data[input_name] = input_value
#         if method == "post":
#             return self.session(post_url, data=post_data)
#         return self.session.get(post_url, params=post_data)


            print("[*] XSS discovered in " + str(form) + " where " + str(value))