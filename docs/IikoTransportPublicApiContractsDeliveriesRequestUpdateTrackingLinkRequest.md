# IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest

Request to update tracking link of a delivery order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | OrganizationId. | 
**order_id** | **UUID** | Delivery order id. | 
**tracking_link** | **str** | Tracking link of a delivery order. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


