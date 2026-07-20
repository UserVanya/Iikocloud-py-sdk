# CreateReserveRequest

Banquet/reserve creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Banquet/reserve comment. | [optional] 
**create_reserve_settings** | [**CreateOrderSettingsBase**](CreateOrderSettingsBase.md) | Reserve creation parameters. | [optional] 
**customer** | [**DeliveryOrderCreateRegularCustomer**](DeliveryOrderCreateRegularCustomer.md) | Customer. | 
**duration_in_minutes** | **int** | Estimated banquet duration. | 
**estimated_start_time** | **str** | Estimated time when reserve will be closed or banquet will be started (Local for the terminal).  Reservation can be made up to 90 days prior to the date. | 
**event_type** | **str** | Event type.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**external_number** | **str** | Banquet/reserve external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**guests** | [**ReserveGuestsInfo**](ReserveGuestsInfo.md) | Guests information. | [optional] 
**guests_count** | **int** | Number of guests. | [optional] 
**id** | **UUID** | Banquet/reserve ID. Must be unique. | [optional] 
**order** | [**ReserveOrderRequest**](ReserveOrderRequest.md) | Order. Used only at a banquet. | [optional] 
**organization_id** | **UUID** | Organization ID of a new banquet/reserve.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**phone** | **str** | Telephone number.  &gt; Must begin with symbol \&quot;+\&quot; and must be at least 8 digits. | 
**should_remind** | **bool** | Whether to remind staff to prepare table beforehand. | 
**table_ids** | **List[UUID]** | Reserved tables. | 
**terminal_group_id** | **UUID** | Front group ID an banquet/reserve must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for banquet/reserve to reach iikoFront.   After this time, banquet/reserve is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 

## Example

```python
from iikocloud_client.models.create_reserve_request import CreateReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReserveRequest from a JSON string
create_reserve_request_instance = CreateReserveRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReserveRequest.to_json())

# convert the object into a dict
create_reserve_request_dict = create_reserve_request_instance.to_dict()
# create an instance of CreateReserveRequest from a dict
create_reserve_request_from_dict = CreateReserveRequest.from_dict(create_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


