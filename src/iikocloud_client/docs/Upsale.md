# Upsale

user tip.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_for_user** | **str** | Description for user. | [optional] 
**product_codes** | **List[str]** | Codes of products that suggested to be added to order. | [optional] 
**products** | [**List[UpsaleProduct]**](UpsaleProduct.md) | Products that suggested to be added to order. | [optional] 
**source_action_id** | **UUID** | Id of action that caused the suggestion. | [optional] 
**suggestion_text** | **str** | Suggestion text. | [optional] 

## Example

```python
from iikocloud_client.models.upsale import Upsale

# TODO update the JSON string below
json = "{}"
# create an instance of Upsale from a JSON string
upsale_instance = Upsale.from_json(json)
# print the JSON string representation of the object
print(Upsale.to_json())

# convert the object into a dict
upsale_dict = upsale_instance.to_dict()
# create an instance of Upsale from a dict
upsale_from_dict = Upsale.from_dict(upsale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


