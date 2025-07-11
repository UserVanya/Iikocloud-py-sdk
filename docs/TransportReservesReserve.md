# TransportReservesReserve

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**TransportDeliveriesResponseOrderCustomer**](TransportDeliveriesResponseOrderCustomer.md) | Client that placed the reserve. | 
**guests_count** | **int** | Estimated guests count. | 
**comment** | **str** | Optional comment for reserve or banquet. | [optional] 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**should_remind** | **bool** | Whether to remind staff to prepare table beforehand. | 
**status** | [**TransportReservesReserveStatus**](TransportReservesReserveStatus.md) | Status of the reserve or banquet. | 
**cancel_reason** | [**TransportReservesReserveCancelReason**](TransportReservesReserveCancelReason.md) | The reserve cancellation reason or null if the reserve hasn&#39;t been canceled. | [optional] 
**table_ids** | **List[str]** | Reserved table IDs. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started. | 
**guests_coming_time** | **str** | Time when guests came and reserve was closed or banquet was started. | [optional] 
**phone** | **str** | Telephone number. | [optional] 
**event_type** | **str** | Event type.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**order** | [**TransportReservesResponseReserveOrder**](TransportReservesResponseReserveOrder.md) | Order. Used only at a banquet. | [optional] 

## Example

```python
from iikocloud_client.models.transport_reserves_reserve import TransportReservesReserve

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReserve from a JSON string
transport_reserves_reserve_instance = TransportReservesReserve.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReserve.to_json())

# convert the object into a dict
transport_reserves_reserve_dict = transport_reserves_reserve_instance.to_dict()
# create an instance of TransportReservesReserve from a dict
transport_reserves_reserve_from_dict = TransportReservesReserve.from_dict(transport_reserves_reserve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


