# AddressRegionsResponse

Service response with list of districts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**regions** | [**List[WrapperAddressRegion]**](WrapperAddressRegion.md) | List of districts. | 

## Example

```python
from iikocloud_client.models.address_regions_response import AddressRegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegionsResponse from a JSON string
address_regions_response_instance = AddressRegionsResponse.from_json(json)
# print the JSON string representation of the object
print(AddressRegionsResponse.to_json())

# convert the object into a dict
address_regions_response_dict = address_regions_response_instance.to_dict()
# create an instance of AddressRegionsResponse from a dict
address_regions_response_from_dict = AddressRegionsResponse.from_dict(address_regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


