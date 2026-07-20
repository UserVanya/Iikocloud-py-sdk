# SeriesWithNotActivatedCoupons

Series with not activated coupons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.series_with_not_activated_coupons import SeriesWithNotActivatedCoupons

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesWithNotActivatedCoupons from a JSON string
series_with_not_activated_coupons_instance = SeriesWithNotActivatedCoupons.from_json(json)
# print the JSON string representation of the object
print(SeriesWithNotActivatedCoupons.to_json())

# convert the object into a dict
series_with_not_activated_coupons_dict = series_with_not_activated_coupons_instance.to_dict()
# create an instance of SeriesWithNotActivatedCoupons from a dict
series_with_not_activated_coupons_from_dict = SeriesWithNotActivatedCoupons.from_dict(series_with_not_activated_coupons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


