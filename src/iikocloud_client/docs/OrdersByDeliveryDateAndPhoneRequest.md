# OrdersByDeliveryDateAndPhoneRequest

Request for a list of orders by phone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**phone** | **str** | Delivery order phone number. | 
**rows_count** | **int** | Maximum number of items returned.  &lt;remarks&gt;  If null, all items will be returned.  &lt;/remarks&gt; | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**start_revision** | **int** | Revision start number beginning from which (but not including) new/edited orders will be returned. | [optional] 

## Example

```python
from iikocloud_client.models.orders_by_delivery_date_and_phone_request import OrdersByDeliveryDateAndPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersByDeliveryDateAndPhoneRequest from a JSON string
orders_by_delivery_date_and_phone_request_instance = OrdersByDeliveryDateAndPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersByDeliveryDateAndPhoneRequest.to_json())

# convert the object into a dict
orders_by_delivery_date_and_phone_request_dict = orders_by_delivery_date_and_phone_request_instance.to_dict()
# create an instance of OrdersByDeliveryDateAndPhoneRequest from a dict
orders_by_delivery_date_and_phone_request_from_dict = OrdersByDeliveryDateAndPhoneRequest.from_dict(orders_by_delivery_date_and_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


