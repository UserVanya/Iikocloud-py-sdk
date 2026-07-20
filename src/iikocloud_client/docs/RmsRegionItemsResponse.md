# RmsRegionItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddressRegion]**](AddressRegion.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_region_items_response import RmsRegionItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsRegionItemsResponse from a JSON string
rms_region_items_response_instance = RmsRegionItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsRegionItemsResponse.to_json())

# convert the object into a dict
rms_region_items_response_dict = rms_region_items_response_instance.to_dict()
# create an instance of RmsRegionItemsResponse from a dict
rms_region_items_response_from_dict = RmsRegionItemsResponse.from_dict(rms_region_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


