# GetCustomerInfoByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.get_customer_info_by_id_request import GetCustomerInfoByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoByIdRequest from a JSON string
get_customer_info_by_id_request_instance = GetCustomerInfoByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoByIdRequest.to_json())

# convert the object into a dict
get_customer_info_by_id_request_dict = get_customer_info_by_id_request_instance.to_dict()
# create an instance of GetCustomerInfoByIdRequest from a dict
get_customer_info_by_id_request_from_dict = GetCustomerInfoByIdRequest.from_dict(get_customer_info_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


