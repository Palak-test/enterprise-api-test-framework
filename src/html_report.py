"""
HTML test report generator for enterprise-api-test-framework
"""
def generate_html_report(results, filename="test_report.html"):
    with open(filename, "w") as f:
        f.write("<html><head><title>Test Report</title></head><body>")
        f.write("<h1>Test Results</h1><ul>")
        for result in results:
            status = "PASS" if result["passed"] else "FAIL"
            f.write(f"<li>{result['name']}: {status}</li>")
        f.write("</ul></body></html>")
