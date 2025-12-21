# DeliveriesResponseOrderExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key. | 
**value** | **str** | Public. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_external_data import DeliveriesResponseOrderExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderExternalData from a JSON string
deliveries_response_order_external_data_instance = DeliveriesResponseOrderExternalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderExternalData.to_json())

# convert the object into a dict
deliveries_response_order_external_data_dict = deliveries_response_order_external_data_instance.to_dict()
# create an instance of DeliveriesResponseOrderExternalData from a dict
deliveries_response_order_external_data_from_dict = DeliveriesResponseOrderExternalData.from_dict(deliveries_response_order_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


