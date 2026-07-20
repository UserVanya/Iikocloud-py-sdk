# PayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_from** | **str** | Debit account identifier (GUID) | 
**account_to** | **str** | Credit account identifier (GUID) | [optional] 
**var_date** | **str** | Payment date (YYYY-MM-DD format) | 
**document_id** | **str** | Incoming invoice identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**sum** | **float** | Payment amount | 

## Example

```python
from iikocloud_client.models.pay_request import PayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayRequest from a JSON string
pay_request_instance = PayRequest.from_json(json)
# print the JSON string representation of the object
print(PayRequest.to_json())

# convert the object into a dict
pay_request_dict = pay_request_instance.to_dict()
# create an instance of PayRequest from a dict
pay_request_from_dict = PayRequest.from_dict(pay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


