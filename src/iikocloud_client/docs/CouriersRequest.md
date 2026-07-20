# CouriersRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | List of organizations. | 

## Example

```python
from iikocloud_client.models.couriers_request import CouriersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouriersRequest from a JSON string
couriers_request_instance = CouriersRequest.from_json(json)
# print the JSON string representation of the object
print(CouriersRequest.to_json())

# convert the object into a dict
couriers_request_dict = couriers_request_instance.to_dict()
# create an instance of CouriersRequest from a dict
couriers_request_from_dict = CouriersRequest.from_dict(couriers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


