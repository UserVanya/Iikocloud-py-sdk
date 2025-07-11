# TransportCommonExternalData

External data key and value pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | External data key. | 
**value** | **str** | External data value. | 

## Example

```python
from iikocloud_client.models.transport_common_external_data import TransportCommonExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonExternalData from a JSON string
transport_common_external_data_instance = TransportCommonExternalData.from_json(json)
# print the JSON string representation of the object
print(TransportCommonExternalData.to_json())

# convert the object into a dict
transport_common_external_data_dict = transport_common_external_data_instance.to_dict()
# create an instance of TransportCommonExternalData from a dict
transport_common_external_data_from_dict = TransportCommonExternalData.from_dict(transport_common_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


