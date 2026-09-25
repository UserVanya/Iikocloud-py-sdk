# NomenclatureProductContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **UUID** | UUID of the container/packaging. The list of values can be retrieved via the \&quot;Get a list of containers\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**container_weight** | **float** | Container weight without the product | [optional] 
**franchise_master_id** | **UUID** | UUID of the parent container in the Franchise master nomenclature | [optional] 
**franchise_unique_id** | **UUID** | Globally unique UUID of the container within Franchise | [optional] 
**full_container_weight** | **float** | Full container weight with the product | [optional] 
**is_deleted** | **bool** | Container deletion flag | [optional] 
**line_number** | **str** | Container number (line number of the container within the product) | [optional] 
**max_container_weight** | **float** | Maximum container weight | [optional] 
**min_container_weight** | **float** | Minimum container weight | [optional] 
**name** | **str** | Container name | [optional] 
**quantity** | **float** | Amount of product in the container | [optional] 
**use_in_front** | **bool** | Use the container in POS | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_container import NomenclatureProductContainer

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductContainer from a JSON string
nomenclature_product_container_instance = NomenclatureProductContainer.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductContainer.to_json())

# convert the object into a dict
nomenclature_product_container_dict = nomenclature_product_container_instance.to_dict()
# create an instance of NomenclatureProductContainer from a dict
nomenclature_product_container_from_dict = NomenclatureProductContainer.from_dict(nomenclature_product_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


