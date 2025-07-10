# NetCustomerGuestCategoryShortInfo

Guest category info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id. | [optional] 
**name** | **str** | Category name. | [optional] 
**is_active** | **bool** | Is category active or not. | [optional] 
**is_default_for_new_guests** | **bool** | Is category default for new guests or not. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_customer_guest_category_short_info import NetCustomerGuestCategoryShortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGuestCategoryShortInfo from a JSON string
net_customer_guest_category_short_info_instance = NetCustomerGuestCategoryShortInfo.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGuestCategoryShortInfo.to_json())

# convert the object into a dict
net_customer_guest_category_short_info_dict = net_customer_guest_category_short_info_instance.to_dict()
# create an instance of NetCustomerGuestCategoryShortInfo from a dict
net_customer_guest_category_short_info_from_dict = NetCustomerGuestCategoryShortInfo.from_dict(net_customer_guest_category_short_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


