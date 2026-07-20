# Counteragent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number | [optional] 
**cell_phone** | **str** | Mobile phone | [optional] 
**client** | **bool** | Is client | [optional] 
**code** | **str** | Counteragent code | [optional] 
**company** | **str** | Company | [optional] 
**email** | **str** | Email | [optional] 
**employee** | **bool** | Is employee | [optional] 
**first_name** | **str** | First name | [optional] 
**id** | **str** | Counteragent identifier (GUID) | [optional] 
**last_name** | **str** | Last name | [optional] 
**middle_name** | **str** | Middle name | [optional] 
**name** | **str** | Counteragent name | [optional] 
**phone** | **str** | Phone | [optional] 
**supplier** | **bool** | Is supplier | [optional] 
**supplier_type** | **str** | Supplier type | [optional] 
**taxpayer_id_number** | **str** | Taxpayer ID number | [optional] 

## Example

```python
from iikocloud_client.models.counteragent import Counteragent

# TODO update the JSON string below
json = "{}"
# create an instance of Counteragent from a JSON string
counteragent_instance = Counteragent.from_json(json)
# print the JSON string representation of the object
print(Counteragent.to_json())

# convert the object into a dict
counteragent_dict = counteragent_instance.to_dict()
# create an instance of Counteragent from a dict
counteragent_from_dict = Counteragent.from_dict(counteragent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


