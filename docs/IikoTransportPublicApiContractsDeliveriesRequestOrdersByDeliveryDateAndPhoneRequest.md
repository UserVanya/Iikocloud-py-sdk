# IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest

Request for a list of orders by phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Delivery order phone number. | 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**start_revision** | **int** | Revision start number beginning from which (but not including) new/edited orders will be returned. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**rows_count** | **int** | Maximum number of items returned.  &lt;remarks&gt;  If null, all items will be returned.  &lt;/remarks&gt; | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request_instance = IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request_dict = iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


