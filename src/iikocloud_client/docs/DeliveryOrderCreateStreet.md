# DeliveryOrderCreateStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City name. | [optional] 
**classifier_id** | **str** | Street ID in classifier, e.g., address database.  \\n &gt; For using in the Russian Federation only. | [optional] 
**id** | **UUID** | ID.                 Can be obtained by &#x60;/api/1/streets/by_city&#x60; operation. | [optional] 
**name** | **str** | Name. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_create_street import DeliveryOrderCreateStreet

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateStreet from a JSON string
delivery_order_create_street_instance = DeliveryOrderCreateStreet.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateStreet.to_json())

# convert the object into a dict
delivery_order_create_street_dict = delivery_order_create_street_instance.to_dict()
# create an instance of DeliveryOrderCreateStreet from a dict
delivery_order_create_street_from_dict = DeliveryOrderCreateStreet.from_dict(delivery_order_create_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


