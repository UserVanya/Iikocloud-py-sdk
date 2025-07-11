# TransportDeliveriesRequestCreateOrderExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key. | 
**value** | **str** | Value. | 
**is_public** | **bool** | The transmitted data may contain both technical identifiers and information useful for the restaurant employee.  If it is necessary for the data to be included in the sales report, then this parameter must be set to TRUE, otherwise to FALSE. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_external_data import TransportDeliveriesRequestCreateOrderExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderExternalData from a JSON string
transport_deliveries_request_create_order_external_data_instance = TransportDeliveriesRequestCreateOrderExternalData.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderExternalData.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_external_data_dict = transport_deliveries_request_create_order_external_data_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderExternalData from a dict
transport_deliveries_request_create_order_external_data_from_dict = TransportDeliveriesRequestCreateOrderExternalData.from_dict(transport_deliveries_request_create_order_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


