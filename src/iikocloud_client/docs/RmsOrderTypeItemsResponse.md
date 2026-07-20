# RmsOrderTypeItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrderTypeDefinition]**](OrderTypeDefinition.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_order_type_items_response import RmsOrderTypeItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsOrderTypeItemsResponse from a JSON string
rms_order_type_items_response_instance = RmsOrderTypeItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsOrderTypeItemsResponse.to_json())

# convert the object into a dict
rms_order_type_items_response_dict = rms_order_type_items_response_instance.to_dict()
# create an instance of RmsOrderTypeItemsResponse from a dict
rms_order_type_items_response_from_dict = RmsOrderTypeItemsResponse.from_dict(rms_order_type_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


