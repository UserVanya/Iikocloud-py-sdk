# TransportReservesCreateReserveRequest

Banquet/reserve creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID of a new banquet/reserve.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID an banquet/reserve must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 
**id** | **str** | Banquet/reserve ID. Must be unique. | [optional] 
**external_number** | **str** | Banquet/reserve external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**order** | [**TransportReservesRequestReserveOrder**](TransportReservesRequestReserveOrder.md) | Order. Used only at a banquet. | [optional] 
**customer** | [**TransportDeliveriesRequestCreateOrderRegularCustomer**](TransportDeliveriesRequestCreateOrderRegularCustomer.md) | Customer. | 
**phone** | **str** | Telephone number.  &gt; Must begin with symbol \&quot;+\&quot; and must be at least 8 digits. | 
**guests_count** | **int** | Number of guests. | [optional] 
**comment** | **str** | Banquet/reserve comment. | [optional] 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**should_remind** | **bool** | Whether to remind staff to prepare table beforehand. | 
**table_ids** | **List[str]** | Reserved tables. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started (Local for the terminal).  Reservation can be made up to 90 days prior to the date. | 
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for banquet/reserve to reach iikoFront.   After this time, banquet/reserve is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 
**guests** | [**TransportReservesGuestsInfo**](TransportReservesGuestsInfo.md) | Guests information. | [optional] 
**event_type** | **str** | Event type.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**create_reserve_settings** | [**TransportOrdersCommonCreateOrderSettings**](TransportOrdersCommonCreateOrderSettings.md) | Reserve creation parameters. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_create_reserve_request import TransportReservesCreateReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesCreateReserveRequest from a JSON string
transport_reserves_create_reserve_request_instance = TransportReservesCreateReserveRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesCreateReserveRequest.to_json())

# convert the object into a dict
transport_reserves_create_reserve_request_dict = transport_reserves_create_reserve_request_instance.to_dict()
# create an instance of TransportReservesCreateReserveRequest from a dict
transport_reserves_create_reserve_request_from_dict = TransportReservesCreateReserveRequest.from_dict(transport_reserves_create_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


