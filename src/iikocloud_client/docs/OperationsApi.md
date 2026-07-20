# iikocloud_client.OperationsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_command_status**](OperationsApi.md#get_command_status) | **POST** /api/1/commands/status | Get status of command.


# **get_command_status**
> GetCommandStatusResponse get_command_status(timeout=timeout, get_command_status_request=get_command_status_request)

Get status of command.

> Response code `410` means that the correlationId value specified in the method is no longer supported.
Please do not request methods that include such a value.

 > Restriction group: `Commands`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_command_status_request import GetCommandStatusRequest
from iikocloud_client.models.get_command_status_response import GetCommandStatusResponse
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
    api_instance = iikocloud_client.OperationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_command_status_request = iikocloud_client.GetCommandStatusRequest() # GetCommandStatusRequest |  (optional)

    try:
        # Get status of command.
        api_response = await api_instance.get_command_status(timeout=timeout, get_command_status_request=get_command_status_request)
        print("The response of OperationsApi->get_command_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->get_command_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_command_status_request** | [**GetCommandStatusRequest**](GetCommandStatusRequest.md)|  | [optional] 

### Return type

[**GetCommandStatusResponse**](GetCommandStatusResponse.md)

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
**410** | Client Error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

