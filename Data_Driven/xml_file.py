import openpyxl
import os
import xml.etree.ElementTree as ET

def convert_excel_to_xml():
    file_path = 'test_data/login_data.xlsx'

    if not os.path.exists(file_path):
        print(f"Excel file not found at {file_path}. Run the Excel generator first.")
        return

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook['LoginTests']

    root = ET.Element("TestCases")

    # Skip header row (start at 2)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_case_id, username, password, expected_result = row

        test_case_elem = ET.SubElement(root, "TestCase", id=test_case_id)

        username_elem = ET.SubElement(test_case_elem, "Username")
        username_elem.text = username

        password_elem = ET.SubElement(test_case_elem, "Password")
        password_elem.text = password

        expected_elem = ET.SubElement(test_case_elem, "ExpectedResult")
        expected_elem.text = expected_result

    # Create XML tree and write to file
    tree = ET.ElementTree(root)

    xml_output_path = 'test_data/login_data.xml'
    tree.write(xml_output_path, encoding="utf-8", xml_declaration=True)
    print(f"XML file created successfully at: {xml_output_path}")

if __name__ == "__main__":
    convert_excel_to_xml()
