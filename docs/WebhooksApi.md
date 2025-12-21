# iikocloud_client.WebhooksApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_settings_post**](WebhooksApi.md#webhooks_settings_post) | **POST** /webhooks/settings | Get webhooks settings for specified organization and authorized API login.
[**webhooks_update_settings_post**](WebhooksApi.md#webhooks_update_settings_post) | **POST** /webhooks/update_settings | Update webhooks settings for specified organization and authorized API login.


# **webhooks_settings_post**
> IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse webhooks_settings_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request=iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request)

Get webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request import IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response import IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request = iikocloud_client.IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest() # IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest |  (optional)

    try:
        # Get webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.webhooks_settings_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request=iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request)
        print("The response of WebhooksApi->webhooks_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request** | [**IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest**](IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse**](IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update_settings_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse webhooks_update_settings_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request=iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request)

Update webhooks settings for specified organization and authorized API login.



 > Restriction group: `WebHooks: settings`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request import IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request = iikocloud_client.IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest() # IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest |  (optional)

    try:
        # Update webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.webhooks_update_settings_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request=iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request)
        print("The response of WebhooksApi->webhooks_update_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_update_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request** | [**IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest**](IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

