# TransportDeliveriesResponseOrderPaymentType

Payment type.                 Can be obtained by `/api/1/payment_types` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**kind** | [**TransportDeliveriesCommonPaymentTypeKind**](TransportDeliveriesCommonPaymentTypeKind.md) | Payment type classifier. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_payment_type import TransportDeliveriesResponseOrderPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderPaymentType from a JSON string
transport_deliveries_response_order_payment_type_instance = TransportDeliveriesResponseOrderPaymentType.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderPaymentType.to_json())

# convert the object into a dict
transport_deliveries_response_order_payment_type_dict = transport_deliveries_response_order_payment_type_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderPaymentType from a dict
transport_deliveries_response_order_payment_type_from_dict = TransportDeliveriesResponseOrderPaymentType.from_dict(transport_deliveries_response_order_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


