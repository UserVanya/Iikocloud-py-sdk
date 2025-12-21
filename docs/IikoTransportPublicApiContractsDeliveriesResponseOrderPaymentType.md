# IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType

Payment type.                 Can be obtained by `/payment_types` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**kind** | [**IikoTransportPublicApiContractsDeliveriesCommonPaymentTypeKind**](IikoTransportPublicApiContractsDeliveriesCommonPaymentTypeKind.md) | Payment type classifier. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_payment_type import IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_payment_type_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_payment_type_dict = iiko_transport_public_api_contracts_deliveries_response_order_payment_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType from a dict
iiko_transport_public_api_contracts_deliveries_response_order_payment_type_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentType.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


