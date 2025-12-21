# iikocloud_client.TerminalGroupsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_groups_awake_post**](TerminalGroupsApi.md#terminal_groups_awake_post) | **POST** /terminal_groups/awake | Awake terminal groups from sleep mode.
[**terminal_groups_is_alive_post**](TerminalGroupsApi.md#terminal_groups_is_alive_post) | **POST** /terminal_groups/is_alive | Returns information on availability of group of terminals.
[**terminal_groups_post**](TerminalGroupsApi.md#terminal_groups_post) | **POST** /terminal_groups | Method that returns information on groups of delivery terminals.


# **terminal_groups_awake_post**
> IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse terminal_groups_awake_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request=iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request)

Awake terminal groups from sleep mode.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request import IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response import IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request = iikocloud_client.IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest() # IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest |  (optional)

    try:
        # Awake terminal groups from sleep mode.
        api_response = await api_instance.terminal_groups_awake_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request=iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request)
        print("The response of TerminalGroupsApi->terminal_groups_awake_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_awake_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request** | [**IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest**](IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse**](IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse.md)

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

# **terminal_groups_is_alive_post**
> IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse terminal_groups_is_alive_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request=iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request)

Returns information on availability of group of terminals.



 > Restriction group: `POS: availability`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request import IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response import IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request = iikocloud_client.IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveRequest() # IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveRequest |  (optional)

    try:
        # Returns information on availability of group of terminals.
        api_response = await api_instance.terminal_groups_is_alive_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request=iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request)
        print("The response of TerminalGroupsApi->terminal_groups_is_alive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_is_alive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_request** | [**IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveRequest**](IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse**](IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse.md)

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

# **terminal_groups_post**
> IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse terminal_groups_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_terminal_groups_request=iiko_transport_public_api_contracts_terminals_terminal_groups_request)

Method that returns information on groups of delivery terminals.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_request import IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_response import IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_terminals_terminal_groups_request = iikocloud_client.IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest() # IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest |  (optional)

    try:
        # Method that returns information on groups of delivery terminals.
        api_response = await api_instance.terminal_groups_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_terminal_groups_request=iiko_transport_public_api_contracts_terminals_terminal_groups_request)
        print("The response of TerminalGroupsApi->terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_terminals_terminal_groups_request** | [**IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest**](IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse**](IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse.md)

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

