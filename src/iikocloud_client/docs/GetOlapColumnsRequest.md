# GetOlapColumnsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | Report type: &#x60;SALES&#x60; — sales, &#x60;TRANSACTIONS&#x60; — transactions, &#x60;DELIVERIES&#x60; — deliveries | 

## Example

```python
from iikocloud_client.models.get_olap_columns_request import GetOlapColumnsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOlapColumnsRequest from a JSON string
get_olap_columns_request_instance = GetOlapColumnsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOlapColumnsRequest.to_json())

# convert the object into a dict
get_olap_columns_request_dict = get_olap_columns_request_instance.to_dict()
# create an instance of GetOlapColumnsRequest from a dict
get_olap_columns_request_from_dict = GetOlapColumnsRequest.from_dict(get_olap_columns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


