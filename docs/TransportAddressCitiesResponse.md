# TransportAddressCitiesResponse

Service response with list of cities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**cities** | [**List[TransportCommonRmsItemsResponseWrapperCity]**](TransportCommonRmsItemsResponseWrapperCity.md) | List of cities. | 

## Example

```python
from iiko_cloud_client.models.transport_address_cities_response import TransportAddressCitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressCitiesResponse from a JSON string
transport_address_cities_response_instance = TransportAddressCitiesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportAddressCitiesResponse.to_json())

# convert the object into a dict
transport_address_cities_response_dict = transport_address_cities_response_instance.to_dict()
# create an instance of TransportAddressCitiesResponse from a dict
transport_address_cities_response_from_dict = TransportAddressCitiesResponse.from_dict(transport_address_cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


