# StreetsByIdResponse

Streets by ids response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**streets** | [**List[StreetById]**](StreetById.md) | Found streets. | [optional] 

## Example

```python
from iikocloud_client.models.streets_by_id_response import StreetsByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreetsByIdResponse from a JSON string
streets_by_id_response_instance = StreetsByIdResponse.from_json(json)
# print the JSON string representation of the object
print(StreetsByIdResponse.to_json())

# convert the object into a dict
streets_by_id_response_dict = streets_by_id_response_instance.to_dict()
# create an instance of StreetsByIdResponse from a dict
streets_by_id_response_from_dict = StreetsByIdResponse.from_dict(streets_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


