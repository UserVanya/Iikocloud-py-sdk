# OrdersByRevisionRequest

Request for a list of edited orders starting from specified revision number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**source_keys** | **List[str]** | Source keys. | [optional] 
**start_revision** | **int** | Revision start number beginning from which (but not including) new/edited orders will be returned.                &gt; Maximum revision offset to request - &#x60;3 hours&#x60;. | 

## Example

```python
from iikocloud_client.models.orders_by_revision_request import OrdersByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersByRevisionRequest from a JSON string
orders_by_revision_request_instance = OrdersByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersByRevisionRequest.to_json())

# convert the object into a dict
orders_by_revision_request_dict = orders_by_revision_request_instance.to_dict()
# create an instance of OrdersByRevisionRequest from a dict
orders_by_revision_request_from_dict = OrdersByRevisionRequest.from_dict(orders_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


