# TransportDeliveriesRequestCreateOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier_id** | **str** | Street ID in classifier, e.g., address database.  \\n &gt; For using in the Russian Federation only. | [optional] 
**id** | **str** | ID.                 Can be obtained by &#x60;/streets/by_city&#x60; operation. | [optional] 
**name** | **str** | Name. | [optional] 
**city** | **str** | City name. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_street import TransportDeliveriesRequestCreateOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderStreet from a JSON string
transport_deliveries_request_create_order_street_instance = TransportDeliveriesRequestCreateOrderStreet.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderStreet.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_street_dict = transport_deliveries_request_create_order_street_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderStreet from a dict
transport_deliveries_request_create_order_street_from_dict = TransportDeliveriesRequestCreateOrderStreet.from_dict(transport_deliveries_request_create_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


