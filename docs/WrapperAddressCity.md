# WrapperAddressCity

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[AddressCity]**](AddressCity.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_address_city import WrapperAddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperAddressCity from a JSON string
wrapper_address_city_instance = WrapperAddressCity.from_json(json)
# print the JSON string representation of the object
print(WrapperAddressCity.to_json())

# convert the object into a dict
wrapper_address_city_dict = wrapper_address_city_instance.to_dict()
# create an instance of WrapperAddressCity from a dict
wrapper_address_city_from_dict = WrapperAddressCity.from_dict(wrapper_address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


