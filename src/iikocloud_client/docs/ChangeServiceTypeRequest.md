# ChangeServiceTypeRequest

Request for change order's delivery type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_service_type** | **str** |  | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.change_service_type_request import ChangeServiceTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeServiceTypeRequest from a JSON string
change_service_type_request_instance = ChangeServiceTypeRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeServiceTypeRequest.to_json())

# convert the object into a dict
change_service_type_request_dict = change_service_type_request_instance.to_dict()
# create an instance of ChangeServiceTypeRequest from a dict
change_service_type_request_from_dict = ChangeServiceTypeRequest.from_dict(change_service_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


