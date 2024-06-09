class VulnScanner:
    def test_xss_in_form(self, form, value, url):
        xss_test_script = "<sCriPt>alert('test')</sCriPt>"
        response = self.submit_form(form, xss_test_script, url)

        if xss_test_script in response.content.decode():
            return True
        return False

    def submit_form(self, form, value, url):
        # Assuming submit_form is already implemented and returns a response
        pass

#  Example usage:
vuln_scanner = VulnScanner()
response = vuln_scanner.test_xss_in_form(forms[0], "example_value", target_url)
print(response)