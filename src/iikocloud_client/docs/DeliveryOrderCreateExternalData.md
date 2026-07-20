# DeliveryOrderCreateExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_public** | **bool** | The transmitted data may contain both technical identifiers and information useful for the restaurant employee.  If it is necessary for the data to be included in the sales report, then this parameter must be set to TRUE, otherwise to FALSE. | [optional] 
**key** | **str** | Key. | 
**value** | **str** | Value. | 

## Example

```python
from iikocloud_client.models.delivery_order_create_external_data import DeliveryOrderCreateExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateExternalData from a JSON string
delivery_order_create_external_data_instance = DeliveryOrderCreateExternalData.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateExternalData.to_json())

# convert the object into a dict
delivery_order_create_external_data_dict = delivery_order_create_external_data_instance.to_dict()
# create an instance of DeliveryOrderCreateExternalData from a dict
delivery_order_create_external_data_from_dict = DeliveryOrderCreateExternalData.from_dict(delivery_order_create_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


