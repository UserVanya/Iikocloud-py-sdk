# IikoTransportPublicApiContractsReservesRequestReserveOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**menu_id** | **str** | External menu ID. | [optional] 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.md) | Order items. | 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.md) | Combos included in order. | [optional] 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**tips** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.md) | Order tips components. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**discounts_info** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDiscountsInfo**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDiscountsInfo.md) | Discounts/surcharges. | [optional] 
**loyalty_info** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**order_type_id** | **UUID** | Order type ID.                 Can be obtained by &#x60;/deliveries/order_types&#x60; operation | [optional] 
**cheque_additional_info** | [**IikoTransportPublicApiContractsDeliveriesCommonChequeAdditionalInfo**](IikoTransportPublicApiContractsDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**external_data** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_request_reserve_order import IikoTransportPublicApiContractsReservesRequestReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesRequestReserveOrder from a JSON string
iiko_transport_public_api_contracts_reserves_request_reserve_order_instance = IikoTransportPublicApiContractsReservesRequestReserveOrder.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesRequestReserveOrder.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_request_reserve_order_dict = iiko_transport_public_api_contracts_reserves_request_reserve_order_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesRequestReserveOrder from a dict
iiko_transport_public_api_contracts_reserves_request_reserve_order_from_dict = IikoTransportPublicApiContractsReservesRequestReserveOrder.from_dict(iiko_transport_public_api_contracts_reserves_request_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


