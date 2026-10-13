# PayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account identifier (GUID) | 
**amount** | **float** | Payment amount | 
**cfo_item_id** | **str** | Cash flow item identifier (GUID) | [optional] 
**document_id** | **str** | Incoming invoice identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**payment_date** | **str** | Payment date (ISO 8601, e.g. 2026-08-15T12:00:00.00+00:00) | 

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


