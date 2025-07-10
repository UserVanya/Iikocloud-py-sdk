# TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest

Request for change of delivery or table order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 
**external_data** | [**List[TransportDeliveriesRequestCreateOrderExternalData]**](TransportDeliveriesRequestCreateOrderExternalData.md) | External data to change. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_external_data_request import TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest from a JSON string
transport_deliveries_request_update_order_change_external_data_request_instance = TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_external_data_request_dict = transport_deliveries_request_update_order_change_external_data_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest from a dict
transport_deliveries_request_update_order_change_external_data_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest.from_dict(transport_deliveries_request_update_order_change_external_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


