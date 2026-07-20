# GetCustomerInfoRequest

Base class for customer info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | [optional] 
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.get_customer_info_request import GetCustomerInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoRequest from a JSON string
get_customer_info_request_instance = GetCustomerInfoRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoRequest.to_json())

# convert the object into a dict
get_customer_info_request_dict = get_customer_info_request_instance.to_dict()
# create an instance of GetCustomerInfoRequest from a dict
get_customer_info_request_from_dict = GetCustomerInfoRequest.from_dict(get_customer_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


