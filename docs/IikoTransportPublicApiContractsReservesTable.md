# IikoTransportPublicApiContractsReservesTable

Table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Table ID. | 
**number** | **int** | Number of table. | 
**name** | **str** | Table name specified in the organization settings. | 
**seating_capacity** | **int** | Seating capacity of the table. | 
**revision** | **int** | Last modified time. | 
**is_deleted** | **bool** | Is table deleted. | 
**pos_id** | **UUID** | POS table Id. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_table import IikoTransportPublicApiContractsReservesTable

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesTable from a JSON string
iiko_transport_public_api_contracts_reserves_table_instance = IikoTransportPublicApiContractsReservesTable.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesTable.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_table_dict = iiko_transport_public_api_contracts_reserves_table_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesTable from a dict
iiko_transport_public_api_contracts_reserves_table_from_dict = IikoTransportPublicApiContractsReservesTable.from_dict(iiko_transport_public_api_contracts_reserves_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


