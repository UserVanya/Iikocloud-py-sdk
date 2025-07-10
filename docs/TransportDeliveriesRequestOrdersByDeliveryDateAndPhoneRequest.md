# TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest

Request for a list of orders by phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Delivery order phone number. | 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**organization_ids** | **List[str]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**start_revision** | **int** | Revision start number beginning from which (but not including) new/edited orders will be returned. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**rows_count** | **int** | Maximum number of items returned.  &lt;remarks&gt;  If null, all items will be returned.  &lt;/remarks&gt; | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_phone_request import TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest from a JSON string
transport_deliveries_request_orders_by_delivery_date_and_phone_request_instance = TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.to_json())

# convert the object into a dict
transport_deliveries_request_orders_by_delivery_date_and_phone_request_dict = transport_deliveries_request_orders_by_delivery_date_and_phone_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest from a dict
transport_deliveries_request_orders_by_delivery_date_and_phone_request_from_dict = TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.from_dict(transport_deliveries_request_orders_by_delivery_date_and_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


