# Image

Unified image object.  Replaces the deprecated buttonImageUrl field across all entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | SHA-1 hash of the image file bytes.  Used for detecting changes without re-downloading. | [optional] 
**updated_at** | **str** | Date and time of the last image update (UTC). | [optional] 
**url** | **str** | Public URL of the image in the file storage. | 

## Example

```python
from iikocloud_client.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


