# iikocloud_client.WebhooksApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_settings_post**](WebhooksApi.md#webhooks_settings_post) | **POST** /webhooks/settings | Get webhooks settings for specified organization and authorized API login.
[**webhooks_update_settings_post**](WebhooksApi.md#webhooks_update_settings_post) | **POST** /webhooks/update_settings | Update webhooks settings for specified organization and authorized API login.


# **webhooks_settings_post**
> TransportWebHooksGetWebHookSettingsResponse webhooks_settings_post(timeout=timeout, transport_web_hooks_get_web_hook_settings_request=transport_web_hooks_get_web_hook_settings_request)

Get webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_web_hooks_get_web_hook_settings_request import TransportWebHooksGetWebHookSettingsRequest
from iikocloud_client.models.transport_web_hooks_get_web_hook_settings_response import TransportWebHooksGetWebHookSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_web_hooks_get_web_hook_settings_request = iikocloud_client.TransportWebHooksGetWebHookSettingsRequest() # TransportWebHooksGetWebHookSettingsRequest |  (optional)

    try:
        # Get webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.webhooks_settings_post(timeout=timeout, transport_web_hooks_get_web_hook_settings_request=transport_web_hooks_get_web_hook_settings_request)
        print("The response of WebhooksApi->webhooks_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_web_hooks_get_web_hook_settings_request** | [**TransportWebHooksGetWebHookSettingsRequest**](TransportWebHooksGetWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**TransportWebHooksGetWebHookSettingsResponse**](TransportWebHooksGetWebHookSettingsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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
> TransportCommonCorrelationIdResponse webhooks_update_settings_post(timeout=timeout, transport_web_hooks_update_web_hook_settings_request=transport_web_hooks_update_web_hook_settings_request)

Update webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_web_hooks_update_web_hook_settings_request import TransportWebHooksUpdateWebHookSettingsRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_web_hooks_update_web_hook_settings_request = iikocloud_client.TransportWebHooksUpdateWebHookSettingsRequest() # TransportWebHooksUpdateWebHookSettingsRequest |  (optional)

    try:
        # Update webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.webhooks_update_settings_post(timeout=timeout, transport_web_hooks_update_web_hook_settings_request=transport_web_hooks_update_web_hook_settings_request)
        print("The response of WebhooksApi->webhooks_update_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_update_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_web_hooks_update_web_hook_settings_request** | [**TransportWebHooksUpdateWebHookSettingsRequest**](TransportWebHooksUpdateWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

