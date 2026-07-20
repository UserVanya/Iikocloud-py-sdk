# ReserveInfo

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_status** | [**CreationStatus**](CreationStatus.md) | Banquet/reserve creation status. In case of asynchronous creation, it allows to track the instance an banquet/reserve was validated/created in iikoFront. | 
**error_info** | [**ErrorInfo**](ErrorInfo.md) | Banquet/reserve creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**external_number** | **str** | Banquet/reserve external number. | [optional] 
**id** | **UUID** | Banquet/reserve ID. | 
**is_deleted** | **bool** | Banquet/reserve is deleted. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve** | [**Reserve**](Reserve.md) | Banquet/reserve. | [optional] 
**timestamp** | **int** | Timestamp of most recent banquet/reserve change that took place on iikoTransport server. | 

## Example

```python
from iikocloud_client.models.reserve_info import ReserveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveInfo from a JSON string
reserve_info_instance = ReserveInfo.from_json(json)
# print the JSON string representation of the object
print(ReserveInfo.to_json())

# convert the object into a dict
reserve_info_dict = reserve_info_instance.to_dict()
# create an instance of ReserveInfo from a dict
reserve_info_from_dict = ReserveInfo.from_dict(reserve_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


