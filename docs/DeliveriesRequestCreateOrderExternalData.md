# DeliveriesRequestCreateOrderExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key. | 
**value** | **str** | Value. | 
**is_public** | **bool** | The transmitted data may contain both technical identifiers and information useful for the restaurant employee.  If it is necessary for the data to be included in the sales report, then this parameter must be set to TRUE, otherwise to FALSE. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_external_data import DeliveriesRequestCreateOrderExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderExternalData from a JSON string
deliveries_request_create_order_external_data_instance = DeliveriesRequestCreateOrderExternalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderExternalData.to_json())

# convert the object into a dict
deliveries_request_create_order_external_data_dict = deliveries_request_create_order_external_data_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderExternalData from a dict
deliveries_request_create_order_external_data_from_dict = DeliveriesRequestCreateOrderExternalData.from_dict(deliveries_request_create_order_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


