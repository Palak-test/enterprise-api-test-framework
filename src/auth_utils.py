"""
API authentication header utility for enterprise-api-test-framework
"""
def get_auth_headers(api_key):
    return {"Authorization": f"Bearer {api_key}"}
