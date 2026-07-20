# Reserve

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_reason** | [**ReserveCancelReason**](ReserveCancelReason.md) | The reserve cancellation reason or null if the reserve hasn&#39;t been canceled. | [optional] 
**comment** | **str** | Optional comment for reserve or banquet. | [optional] 
**customer** | [**DeliveryOrderResponseCustomer**](DeliveryOrderResponseCustomer.md) | Client that placed the reserve. | 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started. | 
**event_type** | **str** | Event type.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**guests_coming_time** | **str** | Time when guests came and reserve was closed or banquet was started. | [optional] 
**guests_count** | **int** | Estimated guests count. | 
**order** | [**ReserveOrderResponse**](ReserveOrderResponse.md) | Order. Used only at a banquet. | [optional] 
**phone** | **str** | Telephone number. | [optional] 
**should_remind** | **bool** | Whether to remind staff to prepare table beforehand. | 
**status** | [**ReserveStatus**](ReserveStatus.md) | Status of the reserve or banquet. | 
**table_ids** | **List[UUID]** | Reserved table IDs. | 

## Example

```python
from iikocloud_client.models.reserve import Reserve

# TODO update the JSON string below
json = "{}"
# create an instance of Reserve from a JSON string
reserve_instance = Reserve.from_json(json)
# print the JSON string representation of the object
print(Reserve.to_json())

# convert the object into a dict
reserve_dict = reserve_instance.to_dict()
# create an instance of Reserve from a dict
reserve_from_dict = Reserve.from_dict(reserve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


