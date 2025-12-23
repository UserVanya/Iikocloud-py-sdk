# DeliveriesResponseOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**city** | [**DeliveriesResponseOrderCity**](DeliveriesResponseOrderCity.md) | City. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_street import DeliveriesResponseOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderStreet from a JSON string
deliveries_response_order_street_instance = DeliveriesResponseOrderStreet.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderStreet.to_json())

# convert the object into a dict
deliveries_response_order_street_dict = deliveries_response_order_street_instance.to_dict()
# create an instance of DeliveriesResponseOrderStreet from a dict
deliveries_response_order_street_from_dict = DeliveriesResponseOrderStreet.from_dict(deliveries_response_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


