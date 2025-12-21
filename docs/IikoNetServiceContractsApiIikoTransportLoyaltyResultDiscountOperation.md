# IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation

Discount operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultOperationCode**](IikoNetServiceContractsApiIikoTransportLoyaltyResultOperationCode.md) | Operation Type Code.  &lt;br&gt;0 - fixed discount for the entire order,&lt;br /&gt;1 - fixed discount for the item,&lt;br /&gt;2 - free product,&lt;br /&gt;3 - other type of discounts. | [optional] 
**order_item_id** | **UUID** | Deprecated, use positionId. | [optional] 
**position_id** | **UUID** | Id of item the discount is applied to. If null - discount applied to whole orders. | [optional] 
**discount_sum** | **float** | Discount sum. | [optional] 
**amount** | **float** | Amount. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation import IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_discount_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


