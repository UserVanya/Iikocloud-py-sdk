# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

Request for change delivery comment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. | 
**order_id** | **UUID** | Order ID. | 
**comment** | **str** | New delivery comment. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


