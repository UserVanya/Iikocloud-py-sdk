# GetAccessTokenV2Request

Authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key generated in iikoWeb under \&quot;Integrations → API Keys\&quot;.   The key determines which restaurant organizations the token grants access to. | 
**app_id** | **UUID** | Unique application identifier issued by the iiko Developer Portal (https://public-api.iikoweb.ru/portal).  You receive it when you register a new application in your developer account.  The &#x60;appId&#x60; never changes for the lifetime of the application. | 
**client_secret** | **str** | Application secret key issued by the iiko Developer Portal (https://public-api.iikoweb.ru/portal).  The secret is shown **only once** — right after the application is created.  Store it securely. If the secret is lost or compromised, regenerate it in the Developer Portal; the previous secret will be revoked immediately. | 

## Example

```python
from iikocloud_client.models.get_access_token_v2_request import GetAccessTokenV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessTokenV2Request from a JSON string
get_access_token_v2_request_instance = GetAccessTokenV2Request.from_json(json)
# print the JSON string representation of the object
print(GetAccessTokenV2Request.to_json())

# convert the object into a dict
get_access_token_v2_request_dict = get_access_token_v2_request_instance.to_dict()
# create an instance of GetAccessTokenV2Request from a dict
get_access_token_v2_request_from_dict = GetAccessTokenV2Request.from_dict(get_access_token_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


