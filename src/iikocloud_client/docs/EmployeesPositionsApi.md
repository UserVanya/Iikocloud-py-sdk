# iikocloud_client.EmployeesPositionsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_position**](EmployeesPositionsApi.md#get_employee_position) | **POST** /api/employees/v1/positions/get | Get employee position by identifier
[**list_employee_positions**](EmployeesPositionsApi.md#list_employee_positions) | **POST** /api/employees/v1/positions/list | List employee positions


# **get_employee_position**
> EmployeePositionResponse get_employee_position(get_position_request, timeout=timeout)

Get employee position by identifier

Returns full information about an employee position by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.employee_position_response import EmployeePositionResponse
from iikocloud_client.models.get_position_request import GetPositionRequest
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
    api_instance = iikocloud_client.EmployeesPositionsApi(api_client)
    get_position_request = iikocloud_client.GetPositionRequest() # GetPositionRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get employee position by identifier
        api_response = await api_instance.get_employee_position(get_position_request, timeout=timeout)
        print("The response of EmployeesPositionsApi->get_employee_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesPositionsApi->get_employee_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_position_request** | [**GetPositionRequest**](GetPositionRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**EmployeePositionResponse**](EmployeePositionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden (organization not in scope of the API key) |  -  |
**404** | Employee position not found |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_positions**
> ListPositionsResponse list_employee_positions(list_positions_request, timeout=timeout)

List employee positions

Returns a paginated list of employee positions with filter support

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_positions_request import ListPositionsRequest
from iikocloud_client.models.list_positions_response import ListPositionsResponse
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
    api_instance = iikocloud_client.EmployeesPositionsApi(api_client)
    list_positions_request = iikocloud_client.ListPositionsRequest() # ListPositionsRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List employee positions
        api_response = await api_instance.list_employee_positions(list_positions_request, timeout=timeout)
        print("The response of EmployeesPositionsApi->list_employee_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesPositionsApi->list_employee_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_positions_request** | [**ListPositionsRequest**](ListPositionsRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ListPositionsResponse**](ListPositionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

