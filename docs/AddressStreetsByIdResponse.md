# AddressStreetsByIdResponse

Streets by ids response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streets** | [**List[AddressStreetById]**](AddressStreetById.md) | Found streets. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 

## Example

```python
from iikocloud_client.models.address_streets_by_id_response import AddressStreetsByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetsByIdResponse from a JSON string
address_streets_by_id_response_instance = AddressStreetsByIdResponse.from_json(json)
# print the JSON string representation of the object
print(AddressStreetsByIdResponse.to_json())

# convert the object into a dict
address_streets_by_id_response_dict = address_streets_by_id_response_instance.to_dict()
# create an instance of AddressStreetsByIdResponse from a dict
address_streets_by_id_response_from_dict = AddressStreetsByIdResponse.from_dict(address_streets_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


