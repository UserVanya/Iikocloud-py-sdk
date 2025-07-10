# TransportAddressRegion

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
from iiko_cloud_client.models.transport_address_region import TransportAddressRegion

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressRegion from a JSON string
transport_address_region_instance = TransportAddressRegion.from_json(json)
# print the JSON string representation of the object
print(TransportAddressRegion.to_json())

# convert the object into a dict
transport_address_region_dict = transport_address_region_instance.to_dict()
# create an instance of TransportAddressRegion from a dict
transport_address_region_from_dict = TransportAddressRegion.from_dict(transport_address_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


