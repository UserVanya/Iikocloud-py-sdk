# AddressLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** | Building. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**flat** | **str** | Apartment.  &gt; In case useUaeAddressingSystem enabled max length - 100, otherwise - 10. | [optional] 
**floor** | **str** | Floor. | [optional] 
**house** | **str** | House. | 
**index** | **str** | Postcode. | [optional] 
**region_id** | **UUID** | Delivery area ID. | [optional] 
**street** | [**DeliveryOrderCreateStreet**](DeliveryOrderCreateStreet.md) | Street.  &gt; It&#39;s required specify only \&quot;classifierId\&quot; or \&quot;id\&quot; or \&quot;name\&quot; and \&quot;city\&quot;. | 

## Example

```python
from iikocloud_client.models.address_legacy import AddressLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLegacy from a JSON string
address_legacy_instance = AddressLegacy.from_json(json)
# print the JSON string representation of the object
print(AddressLegacy.to_json())

# convert the object into a dict
address_legacy_dict = address_legacy_instance.to_dict()
# create an instance of AddressLegacy from a dict
address_legacy_from_dict = AddressLegacy.from_dict(address_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


