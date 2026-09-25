# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[Organization]**](Organization.md) | Child organizations with the same recursive structure; an empty array is returned for a leaf node | [optional] 
**code** | **str** | User-defined organization code; null if the code is not set | [optional] 
**crm_id** | **int** | Numeric organization identifier in CRM | [optional] 
**iiko_uid** | **str** | Organization identifier; null if not provided by the source | [optional] 
**is_cloud** | **bool** | Flag indicating that the organization runs on cloud infrastructure | [optional] 
**name** | **str** | Display name of the organization; null if the name is not provided by the source | [optional] 
**organization_id** | **str** | UOC organization identifier | [optional] 
**parent_id** | **str** | UOC identifier of the parent organization; null for the root node | [optional] 
**rating** | **float** | Organization rating as represented by the source; null if the rating is absent | [optional] 
**type** | **str** | Organization type. Confirmed values: Chain — a chain, Rms — an organization | [optional] 
**version** | **str** | internal API server version of the organization; null if the version is unknown | [optional] 

## Example

```python
from iikocloud_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


