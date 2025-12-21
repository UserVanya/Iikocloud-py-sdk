# iikocloud_client.OperationsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_status_post**](OperationsApi.md#commands_status_post) | **POST** /commands/status | Get status of command.


# **commands_status_post**
> IikoTransportPublicApiContractsCommandsGetCommandStatusResponse commands_status_post(timeout=timeout, iiko_transport_public_api_contracts_commands_get_command_status_request=iiko_transport_public_api_contracts_commands_get_command_status_request)

Get status of command.

> Response code `410` means that the correlationId value specified in the method is no longer supported.
Please do not request methods that include such a value.

 > Restriction group: `Commands`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_commands_get_command_status_request import IikoTransportPublicApiContractsCommandsGetCommandStatusRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_commands_get_command_status_response import IikoTransportPublicApiContractsCommandsGetCommandStatusResponse
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
    api_instance = iikocloud_client.OperationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_commands_get_command_status_request = iikocloud_client.IikoTransportPublicApiContractsCommandsGetCommandStatusRequest() # IikoTransportPublicApiContractsCommandsGetCommandStatusRequest |  (optional)

    try:
        # Get status of command.
        api_response = await api_instance.commands_status_post(timeout=timeout, iiko_transport_public_api_contracts_commands_get_command_status_request=iiko_transport_public_api_contracts_commands_get_command_status_request)
        print("The response of OperationsApi->commands_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->commands_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_commands_get_command_status_request** | [**IikoTransportPublicApiContractsCommandsGetCommandStatusRequest**](IikoTransportPublicApiContractsCommandsGetCommandStatusRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommandsGetCommandStatusResponse**](IikoTransportPublicApiContractsCommandsGetCommandStatusResponse.md)

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
**410** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

