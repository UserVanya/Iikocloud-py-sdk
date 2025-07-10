# TransportAddressStreetsByIdResponse

Streets by ids response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streets** | [**List[TransportAddressStreetById]**](TransportAddressStreetById.md) | Found streets. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_address_streets_by_id_response import TransportAddressStreetsByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreetsByIdResponse from a JSON string
transport_address_streets_by_id_response_instance = TransportAddressStreetsByIdResponse.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreetsByIdResponse.to_json())

# convert the object into a dict
transport_address_streets_by_id_response_dict = transport_address_streets_by_id_response_instance.to_dict()
# create an instance of TransportAddressStreetsByIdResponse from a dict
transport_address_streets_by_id_response_from_dict = TransportAddressStreetsByIdResponse.from_dict(transport_address_streets_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


