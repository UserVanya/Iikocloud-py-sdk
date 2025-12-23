# ExternalMenuPriceByDepartmentsDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | **List[str]** | List of organization GUIDs | [optional] 
**price** | **float** | Product size prices for the organization, if the value is null, then the product/size is not for sale, the price always belongs to the price category that was selected at the time of the request | 
**tax_category_id** | **str** | taxCategory id | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_price_by_departments_dto2 import ExternalMenuPriceByDepartmentsDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuPriceByDepartmentsDto2 from a JSON string
external_menu_price_by_departments_dto2_instance = ExternalMenuPriceByDepartmentsDto2.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuPriceByDepartmentsDto2.to_json())

# convert the object into a dict
external_menu_price_by_departments_dto2_dict = external_menu_price_by_departments_dto2_instance.to_dict()
# create an instance of ExternalMenuPriceByDepartmentsDto2 from a dict
external_menu_price_by_departments_dto2_from_dict = ExternalMenuPriceByDepartmentsDto2.from_dict(external_menu_price_by_departments_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


