# TransportAddressStreetsResponse

Service response with list of streets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**streets** | [**List[TransportAddressStreet]**](TransportAddressStreet.md) | List of streets. | 

## Example

```python
from iikocloud_client.models.transport_address_streets_response import TransportAddressStreetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreetsResponse from a JSON string
transport_address_streets_response_instance = TransportAddressStreetsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreetsResponse.to_json())

# convert the object into a dict
transport_address_streets_response_dict = transport_address_streets_response_instance.to_dict()
# create an instance of TransportAddressStreetsResponse from a dict
transport_address_streets_response_from_dict = TransportAddressStreetsResponse.from_dict(transport_address_streets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


