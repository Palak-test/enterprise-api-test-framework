"""
API response parser and validator for enterprise-api-test-framework
"""
def parse_json_response(response):
    try:
        return response.json()
    except Exception as e:
        raise ValueError(f"Invalid JSON response: {e}")

def validate_status_code(response, expected=200):
    if response.status_code != expected:
        raise AssertionError(f"Expected status {expected}, got {response.status_code}")
