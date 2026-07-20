# ChangeExternalDataRequest

Request for change of delivery or table order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_data** | [**List[DeliveryOrderCreateExternalData]**](DeliveryOrderCreateExternalData.md) | External data to change. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID. | 

## Example

```python
from iikocloud_client.models.change_external_data_request import ChangeExternalDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeExternalDataRequest from a JSON string
change_external_data_request_instance = ChangeExternalDataRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeExternalDataRequest.to_json())

# convert the object into a dict
change_external_data_request_dict = change_external_data_request_instance.to_dict()
# create an instance of ChangeExternalDataRequest from a dict
change_external_data_request_from_dict = ChangeExternalDataRequest.from_dict(change_external_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


