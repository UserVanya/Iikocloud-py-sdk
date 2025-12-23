# DeliveriesRequestUpdateOrderChangeExternalDataRequest

Request for change of delivery or table order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 
**external_data** | [**List[DeliveriesRequestCreateOrderExternalData]**](DeliveriesRequestCreateOrderExternalData.md) | External data to change. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_external_data_request import DeliveriesRequestUpdateOrderChangeExternalDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeExternalDataRequest from a JSON string
deliveries_request_update_order_change_external_data_request_instance = DeliveriesRequestUpdateOrderChangeExternalDataRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeExternalDataRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_change_external_data_request_dict = deliveries_request_update_order_change_external_data_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeExternalDataRequest from a dict
deliveries_request_update_order_change_external_data_request_from_dict = DeliveriesRequestUpdateOrderChangeExternalDataRequest.from_dict(deliveries_request_update_order_change_external_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


