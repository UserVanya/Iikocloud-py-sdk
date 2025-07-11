# TransportDeliveriesRequestOrdersByIdRequest

Request for information about orders using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_ids** | **List[str]** | IDs of orders information on which is required.                &gt; Required if \&quot;posOrderIds\&quot; is null. Must be null if \&quot;posOrderIds\&quot; is not null.                &gt; Maximum allowed \&quot;orderIds\&quot; to request - &#x60;200&#x60;.    The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**pos_order_ids** | **List[str]** | POS order IDs information on which is required.                &gt; Required if \&quot;orderIds\&quot; is null. Must be null if \&quot;orderIds\&quot; is not null.                &gt; Maximum allowed \&quot;posOrderIds\&quot; to request - &#x60;200&#x60;.    The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**return_external_data_keys** | **List[str]** | Keys for retrun external data information. | [optional] 
**return_locked_by_user** | **bool** | Whether to check and return LockedByUser property (see FullOrderUpdateRequest.EmployeeId). | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_orders_by_id_request import TransportDeliveriesRequestOrdersByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestOrdersByIdRequest from a JSON string
transport_deliveries_request_orders_by_id_request_instance = TransportDeliveriesRequestOrdersByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestOrdersByIdRequest.to_json())

# convert the object into a dict
transport_deliveries_request_orders_by_id_request_dict = transport_deliveries_request_orders_by_id_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestOrdersByIdRequest from a dict
transport_deliveries_request_orders_by_id_request_from_dict = TransportDeliveriesRequestOrdersByIdRequest.from_dict(transport_deliveries_request_orders_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


