# DeliveryOrderResponsePaymentType

Payment type.                 Can be obtained by `/api/1/payment_types` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**kind** | [**DeliveryPaymentTypeKind**](DeliveryPaymentTypeKind.md) | Payment type classifier. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_payment_type import DeliveryOrderResponsePaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponsePaymentType from a JSON string
delivery_order_response_payment_type_instance = DeliveryOrderResponsePaymentType.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponsePaymentType.to_json())

# convert the object into a dict
delivery_order_response_payment_type_dict = delivery_order_response_payment_type_instance.to_dict()
# create an instance of DeliveryOrderResponsePaymentType from a dict
delivery_order_response_payment_type_from_dict = DeliveryOrderResponsePaymentType.from_dict(delivery_order_response_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


