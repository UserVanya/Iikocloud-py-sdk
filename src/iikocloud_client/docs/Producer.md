# Producer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the directory entry | [optional] 
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.producer import Producer

# TODO update the JSON string below
json = "{}"
# create an instance of Producer from a JSON string
producer_instance = Producer.from_json(json)
# print the JSON string representation of the object
print(Producer.to_json())

# convert the object into a dict
producer_dict = producer_instance.to_dict()
# create an instance of Producer from a dict
producer_from_dict = Producer.from_dict(producer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


