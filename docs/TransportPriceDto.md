# TransportPriceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id | [optional] 
**price** | **float** | Product size prices for the organization, if the value is null, then the product/size is not for sale, the price always belongs to the price category that was selected at the time of the request | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_price_dto import TransportPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportPriceDto from a JSON string
transport_price_dto_instance = TransportPriceDto.from_json(json)
# print the JSON string representation of the object
print(TransportPriceDto.to_json())

# convert the object into a dict
transport_price_dto_dict = transport_price_dto_instance.to_dict()
# create an instance of TransportPriceDto from a dict
transport_price_dto_from_dict = TransportPriceDto.from_dict(transport_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


