# TransportDeliveriesResponseOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**city** | [**TransportDeliveriesResponseOrderCity**](TransportDeliveriesResponseOrderCity.md) | City. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_street import TransportDeliveriesResponseOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderStreet from a JSON string
transport_deliveries_response_order_street_instance = TransportDeliveriesResponseOrderStreet.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderStreet.to_json())

# convert the object into a dict
transport_deliveries_response_order_street_dict = transport_deliveries_response_order_street_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderStreet from a dict
transport_deliveries_response_order_street_from_dict = TransportDeliveriesResponseOrderStreet.from_dict(transport_deliveries_response_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


