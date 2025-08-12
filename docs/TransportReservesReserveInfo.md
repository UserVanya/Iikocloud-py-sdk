# TransportReservesReserveInfo

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Banquet/reserve ID. | 
**external_number** | **str** | Banquet/reserve external number. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**timestamp** | **int** | Timestamp of most recent banquet/reserve change that took place on iikoTransport server. | 
**creation_status** | [**TransportDeliveriesResponseOrderCreationStatus**](TransportDeliveriesResponseOrderCreationStatus.md) | Banquet/reserve creation status. In case of asynchronous creation, it allows to track the instance an banquet/reserve was validated/created in iikoFront. | 
**error_info** | [**TransportErrorsErrorInfo**](TransportErrorsErrorInfo.md) | Banquet/reserve creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**is_deleted** | **bool** | Banquet/reserve is deleted. | 
**reserve** | [**TransportReservesReserve**](TransportReservesReserve.md) | Banquet/reserve. | [optional] 

## Example

```python
from iikocloud_client.models.transport_reserves_reserve_info import TransportReservesReserveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReserveInfo from a JSON string
transport_reserves_reserve_info_instance = TransportReservesReserveInfo.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReserveInfo.to_json())

# convert the object into a dict
transport_reserves_reserve_info_dict = transport_reserves_reserve_info_instance.to_dict()
# create an instance of TransportReservesReserveInfo from a dict
transport_reserves_reserve_info_from_dict = TransportReservesReserveInfo.from_dict(transport_reserves_reserve_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


