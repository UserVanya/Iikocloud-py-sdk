# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint

Delivery location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**IikoTransportPublicApiContractsDeliveriesCommonCoordinates**](IikoTransportPublicApiContractsDeliveriesCommonCoordinates.md) | Delivery address coordinates.  &gt; Allowed from version &#x60;7.7.3&#x60;. | [optional] 
**address** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddress**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddress.md) | Order delivery address.                &gt; The use of type **City** is allowed if the parameter **addressFormatType &#x3D;&#x3D; City**.                &gt; Can be obtained by &#x60;/organizations&#x60; or &#x60;/organizations/settings&#x60; operations (&#x60;addressFormatType&#x60; parameter). | [optional] 
**external_cartography_id** | **str** | Delivery location custom code in customer&#39;s API system. | [optional] 
**comment** | **str** | Additional information. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_delivery_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


