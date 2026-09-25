# EventAttributeDoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute code | [optional] 
**value** | **object** | Attribute value. The type depends on valueType: &#x60;bool&#x60; | &#x60;string&#x60; | &#x60;int&#x60; | &#x60;float&#x60; | &#x60;date&#x60; | &#x60;guid&#x60; | [optional] 

## Example

```python
from iikocloud_client.models.event_attribute_doc import EventAttributeDoc

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttributeDoc from a JSON string
event_attribute_doc_instance = EventAttributeDoc.from_json(json)
# print the JSON string representation of the object
print(EventAttributeDoc.to_json())

# convert the object into a dict
event_attribute_doc_dict = event_attribute_doc_instance.to_dict()
# create an instance of EventAttributeDoc from a dict
event_attribute_doc_from_dict = EventAttributeDoc.from_dict(event_attribute_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


