#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file"""
    try:
        root = ET.Element("root")
        for key, value in dictionary.items():
            ET.SubElement(root, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
    except:
        return None


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except:
        return None


if __name__ == "__main__":
    data = {
        "name": "John",
                "age": 28,
                "city": "New York"
    }
    filename = "data.xml"
    serialize_to_xml(data, filename)
    print(deserialize_from_xml(filename))
