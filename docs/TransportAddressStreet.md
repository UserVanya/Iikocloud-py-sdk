# TransportAddressStreet

Street DTO in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External system revision No. | [optional] 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 

## Example

```python
from iikocloud_client.models.transport_address_street import TransportAddressStreet

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreet from a JSON string
transport_address_street_instance = TransportAddressStreet.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreet.to_json())

# convert the object into a dict
transport_address_street_dict = transport_address_street_instance.to_dict()
# create an instance of TransportAddressStreet from a dict
transport_address_street_from_dict = TransportAddressStreet.from_dict(transport_address_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


