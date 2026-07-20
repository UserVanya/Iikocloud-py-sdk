# OrdersHistoryByDeliveryDateAndPhoneRequest

Request for a list of historical orders by phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                Order details are stored for 90 days. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit.                Order details are stored for 90 days. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**phone** | **str** | Delivery order phone number. | 
**rows_count** | **int** | Maximum number of items returned.                &gt; Maximum numbers of items to request - &#x60;200&#x60;. | 
**source_keys** | **List[str]** | Source keys. | [optional] 
**start_revision** | **int** | Revision start number beginning from which (but not including) orders will be returned.                &gt; Maximum revision offset to request - &#x60;3 hours&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.orders_history_by_delivery_date_and_phone_request import OrdersHistoryByDeliveryDateAndPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersHistoryByDeliveryDateAndPhoneRequest from a JSON string
orders_history_by_delivery_date_and_phone_request_instance = OrdersHistoryByDeliveryDateAndPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersHistoryByDeliveryDateAndPhoneRequest.to_json())

# convert the object into a dict
orders_history_by_delivery_date_and_phone_request_dict = orders_history_by_delivery_date_and_phone_request_instance.to_dict()
# create an instance of OrdersHistoryByDeliveryDateAndPhoneRequest from a dict
orders_history_by_delivery_date_and_phone_request_from_dict = OrdersHistoryByDeliveryDateAndPhoneRequest.from_dict(orders_history_by_delivery_date_and_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


