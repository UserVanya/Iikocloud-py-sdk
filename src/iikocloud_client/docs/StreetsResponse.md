# StreetsResponse

Service response with list of streets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**streets** | [**List[AddressStreet]**](AddressStreet.md) | List of streets. | 

## Example

```python
from iikocloud_client.models.streets_response import StreetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreetsResponse from a JSON string
streets_response_instance = StreetsResponse.from_json(json)
# print the JSON string representation of the object
print(StreetsResponse.to_json())

# convert the object into a dict
streets_response_dict = streets_response_instance.to_dict()
# create an instance of StreetsResponse from a dict
streets_response_from_dict = StreetsResponse.from_dict(streets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


