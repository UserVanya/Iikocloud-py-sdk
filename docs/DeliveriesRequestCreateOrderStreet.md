# DeliveriesRequestCreateOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier_id** | **str** | Street ID in classifier, e.g., address database.  \\n &gt; For using in the Russian Federation only. | [optional] 
**id** | **UUID** | ID.                 Can be obtained by &#x60;/streets/by_city&#x60; operation. | [optional] 
**name** | **str** | Name. | [optional] 
**city** | **str** | City name. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_street import DeliveriesRequestCreateOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderStreet from a JSON string
deliveries_request_create_order_street_instance = DeliveriesRequestCreateOrderStreet.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderStreet.to_json())

# convert the object into a dict
deliveries_request_create_order_street_dict = deliveries_request_create_order_street_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderStreet from a dict
deliveries_request_create_order_street_from_dict = DeliveriesRequestCreateOrderStreet.from_dict(deliveries_request_create_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


