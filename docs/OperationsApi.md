# iikocloud_client.OperationsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_commands_status_post**](OperationsApi.md#api1_commands_status_post) | **POST** /api/1/commands/status | Get status of command.


# **api1_commands_status_post**
> TransportCommandsGetCommandStatusResponse api1_commands_status_post(timeout=timeout, transport_commands_get_command_status_request=transport_commands_get_command_status_request)

Get status of command.

> Response code `410` means that the correlationId value specified in the method is no longer supported.
Please do not request methods that include such a value.

 > Restriction group: `Commands`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_commands_get_command_status_request import TransportCommandsGetCommandStatusRequest
from iikocloud_client.models.transport_commands_get_command_status_response import TransportCommandsGetCommandStatusResponse
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

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OperationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_commands_get_command_status_request = iikocloud_client.TransportCommandsGetCommandStatusRequest() # TransportCommandsGetCommandStatusRequest |  (optional)

    try:
        # Get status of command.
        api_response = await api_instance.api1_commands_status_post(timeout=timeout, transport_commands_get_command_status_request=transport_commands_get_command_status_request)
        print("The response of OperationsApi->api1_commands_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->api1_commands_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_commands_get_command_status_request** | [**TransportCommandsGetCommandStatusRequest**](TransportCommandsGetCommandStatusRequest.md)|  | [optional] 

### Return type

[**TransportCommandsGetCommandStatusResponse**](TransportCommandsGetCommandStatusResponse.md)

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
**410** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

