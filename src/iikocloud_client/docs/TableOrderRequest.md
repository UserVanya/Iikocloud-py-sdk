# TableOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**ChequeAdditionalInfo**](ChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**combos** | [**List[Combo]**](Combo.md) | Combos included in order. | [optional] 
**customer** | [**DeliveryOrderCreateRegularCustomer**](DeliveryOrderCreateRegularCustomer.md) | Guest.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**discounts_info** | [**DiscountsInfo**](DiscountsInfo.md) | Discounts/surcharges. | [optional] 
**external_data** | [**List[DeliveryOrderCreateExternalData]**](DeliveryOrderCreateExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**external_number** | **str** | Order external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**guest_count** | **int** | Amount of guests in the order.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**guests** | [**TableOrderGuestsInfo**](TableOrderGuestsInfo.md) | Guests information.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**id** | **UUID** | Order ID. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items. | 
**loyalty_info** | [**DeliveryOrderCreateLoyaltyInfo**](DeliveryOrderCreateLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**order_type_id** | **UUID** | Order type ID.                 Can be obtained by &#x60;/api/1/deliveries/order_types&#x60; operation | [optional] 
**payments** | [**List[Payment]**](Payment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**phone** | **str** | Guest phone.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**price_category_id** | **UUID** | Price category id of the order.    Can be obtained by &#x60;/api/2/menu&#x60; operation.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**tab_name** | **str** | Tab name (only for fastfood terminals group in tab mode).   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**table_ids** | **List[UUID]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | [optional] 
**tips** | [**List[TipsPayment]**](TipsPayment.md) | Order tips components. | [optional] 

## Example

```python
from iikocloud_client.models.table_order_request import TableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderRequest from a JSON string
table_order_request_instance = TableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrderRequest.to_json())

# convert the object into a dict
table_order_request_dict = table_order_request_instance.to_dict()
# create an instance of TableOrderRequest from a dict
table_order_request_from_dict = TableOrderRequest.from_dict(table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


