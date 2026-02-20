"""
JSON schema validation utility for enterprise-api-test-framework
"""
import jsonschema

def validate_json_schema(instance, schema):
    jsonschema.validate(instance=instance, schema=schema)
