# AssemblyChartItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the ingredient line | [optional] 
**package_count** | **float** | Package count | [optional] 
**package_type_id** | **UUID** | UUID of the package type | [optional] 
**product_id** | **UUID** | UUID of the ingredient product | [optional] 
**product_size_id** | **UUID** | UUID of the product size this line applies to. null — applies to all sizes | [optional] 
**quantity_in** | **float** | Gross quantity (brutto) | [optional] 
**quantity_in1** | **float** | Additional gross quantity #1 | [optional] 
**quantity_in2** | **float** | Additional gross quantity #2 | [optional] 
**quantity_in3** | **float** | Additional gross quantity #3 | [optional] 
**quantity_middle** | **float** | Semi-processed quantity (netto) | [optional] 
**quantity_out** | **float** | Finished quantity (yield) | [optional] 
**quantity_out1** | **float** | Additional yield quantity #1 | [optional] 
**quantity_out2** | **float** | Additional yield quantity #2 | [optional] 
**quantity_out3** | **float** | Additional yield quantity #3 | [optional] 
**sort_weight** | **int** | Display order weight | [optional] 
**store_specification** | [**StoreSpecification**](StoreSpecification.md) | Organization (structural unit) applicability filter for the ingredient line | [optional] 

## Example

```python
from iikocloud_client.models.assembly_chart_item import AssemblyChartItem

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyChartItem from a JSON string
assembly_chart_item_instance = AssemblyChartItem.from_json(json)
# print the JSON string representation of the object
print(AssemblyChartItem.to_json())

# convert the object into a dict
assembly_chart_item_dict = assembly_chart_item_instance.to_dict()
# create an instance of AssemblyChartItem from a dict
assembly_chart_item_from_dict = AssemblyChartItem.from_dict(assembly_chart_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


