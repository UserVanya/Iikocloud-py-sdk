# GetAccessTokenV2Response

Response to authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Unique request identifier for tracing and support purposes.  Include this value when contacting support about a specific request. | 
**token** | **str** | JWT session token. Pass it in the &#x60;Authorization&#x60; header as &#x60;Bearer {token}&#x60;  in every subsequent API call.  The token is valid for 1 hour (see the &#x60;exp&#x60; claim in the decoded JWT).  When the token expires, call this method again to obtain a new one. | 

## Example

```python
from iikocloud_client.models.get_access_token_v2_response import GetAccessTokenV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessTokenV2Response from a JSON string
get_access_token_v2_response_instance = GetAccessTokenV2Response.from_json(json)
# print the JSON string representation of the object
print(GetAccessTokenV2Response.to_json())

# convert the object into a dict
get_access_token_v2_response_dict = get_access_token_v2_response_instance.to_dict()
# create an instance of GetAccessTokenV2Response from a dict
get_access_token_v2_response_from_dict = GetAccessTokenV2Response.from_dict(get_access_token_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


