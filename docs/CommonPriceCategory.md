# CommonPriceCategory

Price category of the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of price category. | 
**name** | **str** | Name of price category. | [optional] 

## Example

```python
from iikocloud_client.models.common_price_category import CommonPriceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPriceCategory from a JSON string
common_price_category_instance = CommonPriceCategory.from_json(json)
# print the JSON string representation of the object
print(CommonPriceCategory.to_json())

# convert the object into a dict
common_price_category_dict = common_price_category_instance.to_dict()
# create an instance of CommonPriceCategory from a dict
common_price_category_from_dict = CommonPriceCategory.from_dict(common_price_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


