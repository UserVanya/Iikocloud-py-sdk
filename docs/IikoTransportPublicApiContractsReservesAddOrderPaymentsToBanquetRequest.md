# IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest

Request for add order payments to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **UUID** | Reserve ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request import IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest from a JSON string
iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request_instance = IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request_dict = iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest from a dict
iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request_from_dict = IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest.from_dict(iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


