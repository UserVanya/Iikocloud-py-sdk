# TransportDeliveriesRequestCreateOrderDiscountsInfo

Information on discounts/surcharges to be applied to order.  <remarks>  Whether map or non-blank list of discounts must be set.  </remarks>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**TransportDeliveriesRequestCreateOrderDiscountCard**](TransportDeliveriesRequestCreateOrderDiscountCard.md) | Track of discount card to be applied to order. | [optional] 
**discounts** | [**List[TransportDeliveriesRequestCreateOrderDiscount]**](TransportDeliveriesRequestCreateOrderDiscount.md) | Discounts/surcharges.   &gt; Type **iikoCard** allowed from version &#x60;7.4.4&#x60;. | [optional] 
**fixed_loyalty_discounts** | **bool** | Whether loyalty discounts should be fixed. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_discounts_info import TransportDeliveriesRequestCreateOrderDiscountsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderDiscountsInfo from a JSON string
transport_deliveries_request_create_order_discounts_info_instance = TransportDeliveriesRequestCreateOrderDiscountsInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderDiscountsInfo.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_discounts_info_dict = transport_deliveries_request_create_order_discounts_info_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderDiscountsInfo from a dict
transport_deliveries_request_create_order_discounts_info_from_dict = TransportDeliveriesRequestCreateOrderDiscountsInfo.from_dict(transport_deliveries_request_create_order_discounts_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


