# AddressRegion

Delivery district DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Region ID in RMS. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External revision. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 

## Example

```python
from iikocloud_client.models.address_region import AddressRegion

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegion from a JSON string
address_region_instance = AddressRegion.from_json(json)
# print the JSON string representation of the object
print(AddressRegion.to_json())

# convert the object into a dict
address_region_dict = address_region_instance.to_dict()
# create an instance of AddressRegion from a dict
address_region_from_dict = AddressRegion.from_dict(address_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


