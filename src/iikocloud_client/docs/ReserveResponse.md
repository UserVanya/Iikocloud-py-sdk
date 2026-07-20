# ReserveResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserve_info** | [**ReserveInfo**](ReserveInfo.md) | Banquet/reserve. | 

## Example

```python
from iikocloud_client.models.reserve_response import ReserveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveResponse from a JSON string
reserve_response_instance = ReserveResponse.from_json(json)
# print the JSON string representation of the object
print(ReserveResponse.to_json())

# convert the object into a dict
reserve_response_dict = reserve_response_instance.to_dict()
# create an instance of ReserveResponse from a dict
reserve_response_from_dict = ReserveResponse.from_dict(reserve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


