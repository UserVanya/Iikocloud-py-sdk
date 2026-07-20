# RmsDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type_id** | **UUID** | Discount type.                 Can be obtained by &#x60;/api/1/discounts&#x60; operation. | 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 
**sum** | **float** | Discount/surcharge sum. | [optional] 

## Example

```python
from iikocloud_client.models.rms_discount import RmsDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of RmsDiscount from a JSON string
rms_discount_instance = RmsDiscount.from_json(json)
# print the JSON string representation of the object
print(RmsDiscount.to_json())

# convert the object into a dict
rms_discount_dict = rms_discount_instance.to_dict()
# create an instance of RmsDiscount from a dict
rms_discount_from_dict = RmsDiscount.from_dict(rms_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


