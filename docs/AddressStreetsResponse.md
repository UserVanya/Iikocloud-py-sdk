# AddressStreetsResponse

Service response with list of streets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**streets** | [**List[AddressStreet]**](AddressStreet.md) | List of streets. | 

## Example

```python
from iikocloud_client.models.address_streets_response import AddressStreetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetsResponse from a JSON string
address_streets_response_instance = AddressStreetsResponse.from_json(json)
# print the JSON string representation of the object
print(AddressStreetsResponse.to_json())

# convert the object into a dict
address_streets_response_dict = address_streets_response_instance.to_dict()
# create an instance of AddressStreetsResponse from a dict
address_streets_response_from_dict = AddressStreetsResponse.from_dict(address_streets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


