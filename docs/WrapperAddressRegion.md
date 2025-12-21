# WrapperAddressRegion

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[AddressRegion]**](AddressRegion.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_address_region import WrapperAddressRegion

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperAddressRegion from a JSON string
wrapper_address_region_instance = WrapperAddressRegion.from_json(json)
# print the JSON string representation of the object
print(WrapperAddressRegion.to_json())

# convert the object into a dict
wrapper_address_region_dict = wrapper_address_region_instance.to_dict()
# create an instance of WrapperAddressRegion from a dict
wrapper_address_region_from_dict = WrapperAddressRegion.from_dict(wrapper_address_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


