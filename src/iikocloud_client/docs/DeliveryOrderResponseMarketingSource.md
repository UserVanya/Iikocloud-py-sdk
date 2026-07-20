# DeliveryOrderResponseMarketingSource

Marketing source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_marketing_source import DeliveryOrderResponseMarketingSource

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseMarketingSource from a JSON string
delivery_order_response_marketing_source_instance = DeliveryOrderResponseMarketingSource.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseMarketingSource.to_json())

# convert the object into a dict
delivery_order_response_marketing_source_dict = delivery_order_response_marketing_source_instance.to_dict()
# create an instance of DeliveryOrderResponseMarketingSource from a dict
delivery_order_response_marketing_source_from_dict = DeliveryOrderResponseMarketingSource.from_dict(delivery_order_response_marketing_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


