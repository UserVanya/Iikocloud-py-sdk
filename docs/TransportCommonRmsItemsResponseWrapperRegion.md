# TransportCommonRmsItemsResponseWrapperRegion

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[TransportAddressRegion]**](TransportAddressRegion.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.transport_common_rms_items_response_wrapper_region import TransportCommonRmsItemsResponseWrapperRegion

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperRegion from a JSON string
transport_common_rms_items_response_wrapper_region_instance = TransportCommonRmsItemsResponseWrapperRegion.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperRegion.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_region_dict = transport_common_rms_items_response_wrapper_region_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperRegion from a dict
transport_common_rms_items_response_wrapper_region_from_dict = TransportCommonRmsItemsResponseWrapperRegion.from_dict(transport_common_rms_items_response_wrapper_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


