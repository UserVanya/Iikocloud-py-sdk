# DeliveriesResponseOrderPaymentType

Payment type.                 Can be obtained by `/payment_types` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**kind** | [**DeliveriesCommonPaymentTypeKind**](DeliveriesCommonPaymentTypeKind.md) | Payment type classifier. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_payment_type import DeliveriesResponseOrderPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderPaymentType from a JSON string
deliveries_response_order_payment_type_instance = DeliveriesResponseOrderPaymentType.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderPaymentType.to_json())

# convert the object into a dict
deliveries_response_order_payment_type_dict = deliveries_response_order_payment_type_instance.to_dict()
# create an instance of DeliveriesResponseOrderPaymentType from a dict
deliveries_response_order_payment_type_from_dict = DeliveriesResponseOrderPaymentType.from_dict(deliveries_response_order_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


