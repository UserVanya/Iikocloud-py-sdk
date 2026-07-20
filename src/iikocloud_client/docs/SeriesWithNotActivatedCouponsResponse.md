# SeriesWithNotActivatedCouponsResponse

Series with not activated coupons response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_with_not_activated_coupons** | [**List[SeriesWithNotActivatedCoupons]**](SeriesWithNotActivatedCoupons.md) | Series with not activated coupons. | [optional] 

## Example

```python
from iikocloud_client.models.series_with_not_activated_coupons_response import SeriesWithNotActivatedCouponsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesWithNotActivatedCouponsResponse from a JSON string
series_with_not_activated_coupons_response_instance = SeriesWithNotActivatedCouponsResponse.from_json(json)
# print the JSON string representation of the object
print(SeriesWithNotActivatedCouponsResponse.to_json())

# convert the object into a dict
series_with_not_activated_coupons_response_dict = series_with_not_activated_coupons_response_instance.to_dict()
# create an instance of SeriesWithNotActivatedCouponsResponse from a dict
series_with_not_activated_coupons_response_from_dict = SeriesWithNotActivatedCouponsResponse.from_dict(series_with_not_activated_coupons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


