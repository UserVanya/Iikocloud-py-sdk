# TransportAddressCity

City DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | City ID in RMS. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External revision. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**additional_info** | **str** | City additional information. | [optional] 

## Example

```python
from iikocloud_client.models.transport_address_city import TransportAddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressCity from a JSON string
transport_address_city_instance = TransportAddressCity.from_json(json)
# print the JSON string representation of the object
print(TransportAddressCity.to_json())

# convert the object into a dict
transport_address_city_dict = transport_address_city_instance.to_dict()
# create an instance of TransportAddressCity from a dict
transport_address_city_from_dict = TransportAddressCity.from_dict(transport_address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


