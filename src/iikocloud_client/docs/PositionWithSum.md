# PositionWithSum

Order item positions with position discount sum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** | Order item position ID. | 
**sum** | **float** | Position discount sum. | 

## Example

```python
from iikocloud_client.models.position_with_sum import PositionWithSum

# TODO update the JSON string below
json = "{}"
# create an instance of PositionWithSum from a JSON string
position_with_sum_instance = PositionWithSum.from_json(json)
# print the JSON string representation of the object
print(PositionWithSum.to_json())

# convert the object into a dict
position_with_sum_dict = position_with_sum_instance.to_dict()
# create an instance of PositionWithSum from a dict
position_with_sum_from_dict = PositionWithSum.from_dict(position_with_sum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


