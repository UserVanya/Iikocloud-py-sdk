# RmsCityItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddressDirectoryCity]**](AddressDirectoryCity.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_city_items_response import RmsCityItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsCityItemsResponse from a JSON string
rms_city_items_response_instance = RmsCityItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsCityItemsResponse.to_json())

# convert the object into a dict
rms_city_items_response_dict = rms_city_items_response_instance.to_dict()
# create an instance of RmsCityItemsResponse from a dict
rms_city_items_response_from_dict = RmsCityItemsResponse.from_dict(rms_city_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


