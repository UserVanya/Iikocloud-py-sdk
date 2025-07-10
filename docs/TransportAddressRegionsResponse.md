# TransportAddressRegionsResponse

Service response with list of districts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**regions** | [**List[TransportCommonRmsItemsResponseWrapperRegion]**](TransportCommonRmsItemsResponseWrapperRegion.md) | List of districts. | 

## Example

```python
from iiko_cloud_client.models.transport_address_regions_response import TransportAddressRegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressRegionsResponse from a JSON string
transport_address_regions_response_instance = TransportAddressRegionsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportAddressRegionsResponse.to_json())

# convert the object into a dict
transport_address_regions_response_dict = transport_address_regions_response_instance.to_dict()
# create an instance of TransportAddressRegionsResponse from a dict
transport_address_regions_response_from_dict = TransportAddressRegionsResponse.from_dict(transport_address_regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


