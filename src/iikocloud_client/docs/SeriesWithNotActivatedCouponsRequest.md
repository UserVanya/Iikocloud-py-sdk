# SeriesWithNotActivatedCouponsRequest

Series with not activated coupons request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.series_with_not_activated_coupons_request import SeriesWithNotActivatedCouponsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesWithNotActivatedCouponsRequest from a JSON string
series_with_not_activated_coupons_request_instance = SeriesWithNotActivatedCouponsRequest.from_json(json)
# print the JSON string representation of the object
print(SeriesWithNotActivatedCouponsRequest.to_json())

# convert the object into a dict
series_with_not_activated_coupons_request_dict = series_with_not_activated_coupons_request_instance.to_dict()
# create an instance of SeriesWithNotActivatedCouponsRequest from a dict
series_with_not_activated_coupons_request_from_dict = SeriesWithNotActivatedCouponsRequest.from_dict(series_with_not_activated_coupons_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


