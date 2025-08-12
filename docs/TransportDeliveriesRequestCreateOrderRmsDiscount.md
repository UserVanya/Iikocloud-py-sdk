# TransportDeliveriesRequestCreateOrderRmsDiscount

RMS discount/surcharge.  <remarks>  Amount must be specified only if discount has \"assign amount\" setting enabled.  In any other case, amount must not be specified.   </remarks>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type_id** | **str** | Discount type.                 Can be obtained by &#x60;/discounts&#x60; operation. | 
**sum** | **float** | Discount/surcharge sum. | [optional] 
**selective_positions** | **List[str]** | Order item positions. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_rms_discount import TransportDeliveriesRequestCreateOrderRmsDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderRmsDiscount from a JSON string
transport_deliveries_request_create_order_rms_discount_instance = TransportDeliveriesRequestCreateOrderRmsDiscount.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderRmsDiscount.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_rms_discount_dict = transport_deliveries_request_create_order_rms_discount_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderRmsDiscount from a dict
transport_deliveries_request_create_order_rms_discount_from_dict = TransportDeliveriesRequestCreateOrderRmsDiscount.from_dict(transport_deliveries_request_create_order_rms_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


