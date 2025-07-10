# TransportDeliveriesRequestCreateOrderDeliveryPoint

Delivery location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**TransportDeliveriesCommonCoordinates**](TransportDeliveriesCommonCoordinates.md) | Delivery address coordinates.  &gt; Allowed from version &#x60;7.7.3&#x60;. | [optional] 
**address** | [**TransportDeliveriesRequestCreateOrderAddress**](TransportDeliveriesRequestCreateOrderAddress.md) | Order delivery address.                &gt; The use of type **City** is allowed if the parameter **addressFormatType &#x3D;&#x3D; City**.                &gt; Can be obtained by &#x60;/api/1/organizations&#x60; or &#x60;/api/1/organizations/settings&#x60; operations (&#x60;addressFormatType&#x60; parameter). | [optional] 
**external_cartography_id** | **str** | Delivery location custom code in customer&#39;s API system. | [optional] 
**comment** | **str** | Additional information. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_delivery_point import TransportDeliveriesRequestCreateOrderDeliveryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderDeliveryPoint from a JSON string
transport_deliveries_request_create_order_delivery_point_instance = TransportDeliveriesRequestCreateOrderDeliveryPoint.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderDeliveryPoint.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_delivery_point_dict = transport_deliveries_request_create_order_delivery_point_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderDeliveryPoint from a dict
transport_deliveries_request_create_order_delivery_point_from_dict = TransportDeliveriesRequestCreateOrderDeliveryPoint.from_dict(transport_deliveries_request_create_order_delivery_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


