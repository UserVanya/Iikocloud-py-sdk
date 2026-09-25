# MenuRequestV3

Request for menu by id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_menu_id** | **str** | External menu id                Can be obtained by &#x60;api/2/menu&#x60; operation. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**price_category_id** | **UUID** | Price category id.                Can be obtained by &#x60;api/2/menu&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.menu_request_v3 import MenuRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of MenuRequestV3 from a JSON string
menu_request_v3_instance = MenuRequestV3.from_json(json)
# print the JSON string representation of the object
print(MenuRequestV3.to_json())

# convert the object into a dict
menu_request_v3_dict = menu_request_v3_instance.to_dict()
# create an instance of MenuRequestV3 from a dict
menu_request_v3_from_dict = MenuRequestV3.from_dict(menu_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


