#menu_test_organization_id = UUID('815bb8fd-b393-477a-8abc-fb962ab408d6'), menu_id = '23311'
import iikocloud_client as icc
import json
def main():
    with open('response_text.json', 'r') as f:
        response_text = f.read()
    menu = icc.ExternalMenuV2.from_json(response_text)
    print(menu)
main()