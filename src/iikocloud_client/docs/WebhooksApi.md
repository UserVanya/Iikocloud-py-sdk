# iikocloud_client.WebhooksApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook_settings**](WebhooksApi.md#get_webhook_settings) | **POST** /api/1/webhooks/settings | Get webhooks settings for specified organization and authorized API login.
[**update_webhook_settings**](WebhooksApi.md#update_webhook_settings) | **POST** /api/1/webhooks/update_settings | Update webhooks settings for specified organization and authorized API login.


# **get_webhook_settings**
> GetWebHookSettingsResponse get_webhook_settings(timeout=timeout, get_web_hook_settings_request=get_web_hook_settings_request)

Get webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_web_hook_settings_request import GetWebHookSettingsRequest
from iikocloud_client.models.get_web_hook_settings_response import GetWebHookSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_web_hook_settings_request = iikocloud_client.GetWebHookSettingsRequest() # GetWebHookSettingsRequest |  (optional)

    try:
        # Get webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.get_webhook_settings(timeout=timeout, get_web_hook_settings_request=get_web_hook_settings_request)
        print("The response of WebhooksApi->get_webhook_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_web_hook_settings_request** | [**GetWebHookSettingsRequest**](GetWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**GetWebHookSettingsResponse**](GetWebHookSettingsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_settings**
> CorrelationIdResponse update_webhook_settings(timeout=timeout, update_web_hook_settings_request=update_web_hook_settings_request)

Update webhooks settings for specified organization and authorized API login.



 > Restriction group: `WebHooks: settings`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_web_hook_settings_request import UpdateWebHookSettingsRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.WebhooksApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_web_hook_settings_request = iikocloud_client.UpdateWebHookSettingsRequest() # UpdateWebHookSettingsRequest |  (optional)

    try:
        # Update webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.update_webhook_settings(timeout=timeout, update_web_hook_settings_request=update_web_hook_settings_request)
        print("The response of WebhooksApi->update_webhook_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_web_hook_settings_request** | [**UpdateWebHookSettingsRequest**](UpdateWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

