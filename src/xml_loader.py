"""
XML data loader for enterprise-api-test-framework
"""
import xml.etree.ElementTree as ET
import os

def load_xml_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"XML file not found: {file_path}")
    tree = ET.parse(file_path)
    return tree.getroot()
