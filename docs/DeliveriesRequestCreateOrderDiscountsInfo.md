# DeliveriesRequestCreateOrderDiscountsInfo

Information on discounts/surcharges to be applied to order.  <remarks>  Whether map or non-blank list of discounts must be set.  </remarks>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**DeliveriesRequestCreateOrderDiscountCard**](DeliveriesRequestCreateOrderDiscountCard.md) | Track of discount card to be applied to order. | [optional] 
**discounts** | [**List[DeliveriesRequestCreateOrderDiscount]**](DeliveriesRequestCreateOrderDiscount.md) | Discounts/surcharges.   &gt; Type **iikoCard** allowed from version &#x60;7.4.4&#x60;. | [optional] 
**fixed_loyalty_discounts** | **bool** | Whether loyalty discounts should be fixed. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_discounts_info import DeliveriesRequestCreateOrderDiscountsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderDiscountsInfo from a JSON string
deliveries_request_create_order_discounts_info_instance = DeliveriesRequestCreateOrderDiscountsInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderDiscountsInfo.to_json())

# convert the object into a dict
deliveries_request_create_order_discounts_info_dict = deliveries_request_create_order_discounts_info_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderDiscountsInfo from a dict
deliveries_request_create_order_discounts_info_from_dict = DeliveriesRequestCreateOrderDiscountsInfo.from_dict(deliveries_request_create_order_discounts_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


