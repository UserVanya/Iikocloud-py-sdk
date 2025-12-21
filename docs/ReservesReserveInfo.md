# ReservesReserveInfo

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Banquet/reserve ID. | 
**external_number** | **str** | Banquet/reserve external number. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**timestamp** | **int** | Timestamp of most recent banquet/reserve change that took place on iikoTransport server. | 
**creation_status** | [**DeliveriesResponseOrderCreationStatus**](DeliveriesResponseOrderCreationStatus.md) | Banquet/reserve creation status. In case of asynchronous creation, it allows to track the instance an banquet/reserve was validated/created in iikoFront. | 
**error_info** | [**ErrorsErrorInfo**](ErrorsErrorInfo.md) | Banquet/reserve creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**is_deleted** | **bool** | Banquet/reserve is deleted. | 
**reserve** | [**ReservesReserve**](ReservesReserve.md) | Banquet/reserve. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_reserve_info import ReservesReserveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesReserveInfo from a JSON string
reserves_reserve_info_instance = ReservesReserveInfo.from_json(json)
# print the JSON string representation of the object
print(ReservesReserveInfo.to_json())

# convert the object into a dict
reserves_reserve_info_dict = reserves_reserve_info_instance.to_dict()
# create an instance of ReservesReserveInfo from a dict
reserves_reserve_info_from_dict = ReservesReserveInfo.from_dict(reserves_reserve_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


