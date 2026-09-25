# iikocloud_client.TerminalsCashRegistersApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_terminal_cash_registers**](TerminalsCashRegistersApi.md#list_terminal_cash_registers) | **POST** /api/terminals/v1/cash-registers/list | List of cash registers


# **list_terminal_cash_registers**
> CashRegisterListResponse list_terminal_cash_registers(cash_register_list_request, timeout=timeout)

List of cash registers

Returns the list of cash registers of the organization

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_register_list_request import CashRegisterListRequest
from iikocloud_client.models.cash_register_list_response import CashRegisterListResponse
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
    api_instance = iikocloud_client.TerminalsCashRegistersApi(api_client)
    cash_register_list_request = iikocloud_client.CashRegisterListRequest() # CashRegisterListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List of cash registers
        api_response = await api_instance.list_terminal_cash_registers(cash_register_list_request, timeout=timeout)
        print("The response of TerminalsCashRegistersApi->list_terminal_cash_registers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsCashRegistersApi->list_terminal_cash_registers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_register_list_request** | [**CashRegisterListRequest**](CashRegisterListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashRegisterListResponse**](CashRegisterListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

