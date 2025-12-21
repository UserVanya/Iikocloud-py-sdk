# IikoTransportPublicApiContractsReservesReserveInfo

Banquet/reserve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Banquet/reserve ID. | 
**external_number** | **str** | Banquet/reserve external number. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**timestamp** | **int** | Timestamp of most recent banquet/reserve change that took place on iikoTransport server. | 
**creation_status** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCreationStatus**](IikoTransportPublicApiContractsDeliveriesResponseOrderCreationStatus.md) | Banquet/reserve creation status. In case of asynchronous creation, it allows to track the instance an banquet/reserve was validated/created in iikoFront. | 
**error_info** | [**IikoTransportPublicApiContractsErrorsErrorInfo**](IikoTransportPublicApiContractsErrorsErrorInfo.md) | Banquet/reserve creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**is_deleted** | **bool** | Banquet/reserve is deleted. | 
**reserve** | [**IikoTransportPublicApiContractsReservesReserve**](IikoTransportPublicApiContractsReservesReserve.md) | Banquet/reserve. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserve_info import IikoTransportPublicApiContractsReservesReserveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesReserveInfo from a JSON string
iiko_transport_public_api_contracts_reserves_reserve_info_instance = IikoTransportPublicApiContractsReservesReserveInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesReserveInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_reserve_info_dict = iiko_transport_public_api_contracts_reserves_reserve_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesReserveInfo from a dict
iiko_transport_public_api_contracts_reserves_reserve_info_from_dict = IikoTransportPublicApiContractsReservesReserveInfo.from_dict(iiko_transport_public_api_contracts_reserves_reserve_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


