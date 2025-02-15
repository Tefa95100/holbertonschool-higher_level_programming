#!/usr/bin/python3
"""
Contains function for serialize and deserialize XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function for serialize a dictionary in XMl

    Args:
        dictionary (dict): A dictionary for serialize
        filename (str): Path for save XML
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value

    ET.ElementTree(root).write(filename, encoding="utf-8",
                               xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function for deserialize a XML in a dictionary

    Args:
        filename (str): Path of file XML

    Returns:
        dict: Return dictionary afeter deserialize
    """
    with open(filename, encoding="utf-8") as data_xml:
        data = ET.parse(data_xml)
        root = data.getroot()
        dict_read = {word.tag: word.text for word in root}
        return dict_read
