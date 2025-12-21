# DeliveriesRequestCreateOrderRmsDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type_id** | **UUID** | Discount type.                 Can be obtained by &#x60;/discounts&#x60; operation. | 
**sum** | **float** | Discount/surcharge sum. | [optional] 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_rms_discount import DeliveriesRequestCreateOrderRmsDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderRmsDiscount from a JSON string
deliveries_request_create_order_rms_discount_instance = DeliveriesRequestCreateOrderRmsDiscount.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderRmsDiscount.to_json())

# convert the object into a dict
deliveries_request_create_order_rms_discount_dict = deliveries_request_create_order_rms_discount_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderRmsDiscount from a dict
deliveries_request_create_order_rms_discount_from_dict = DeliveriesRequestCreateOrderRmsDiscount.from_dict(deliveries_request_create_order_rms_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


