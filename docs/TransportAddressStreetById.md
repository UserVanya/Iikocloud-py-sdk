# TransportAddressStreetById

Street by id response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Street id. | 
**classifier_id** | **str** | Street classifierId. | [optional] 
**city_id** | **str** | City id. | 
**city_name** | **str** | City name. | 
**street_name** | **str** | Street name. | 

## Example

```python
from iiko_cloud_client.models.transport_address_street_by_id import TransportAddressStreetById

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreetById from a JSON string
transport_address_street_by_id_instance = TransportAddressStreetById.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreetById.to_json())

# convert the object into a dict
transport_address_street_by_id_dict = transport_address_street_by_id_instance.to_dict()
# create an instance of TransportAddressStreetById from a dict
transport_address_street_by_id_from_dict = TransportAddressStreetById.from_dict(transport_address_street_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


