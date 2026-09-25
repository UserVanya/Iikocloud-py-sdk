# LicenseItem

License Information of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **str** | License end date. | [optional] 
**license_start** | **str** | License start date. | [optional] 
**module_id** | **str** | Id license module. | 
**organization_id** | **UUID** | UoC organization ID. | 
**quantity** | **float** | Number of license \&quot;slots\&quot;. | 

## Example

```python
from iikocloud_client.models.license_item import LicenseItem

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseItem from a JSON string
license_item_instance = LicenseItem.from_json(json)
# print the JSON string representation of the object
print(LicenseItem.to_json())

# convert the object into a dict
license_item_dict = license_item_instance.to_dict()
# create an instance of LicenseItem from a dict
license_item_from_dict = LicenseItem.from_dict(license_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


