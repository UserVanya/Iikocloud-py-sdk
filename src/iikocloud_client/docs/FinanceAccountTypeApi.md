# iikocloud_client.FinanceAccountTypeApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_account_types**](FinanceAccountTypeApi.md#list_finance_account_types) | **POST** /api/finance/v1/account-type/list | List of account types


# **list_finance_account_types**
> List[AccountType] list_finance_account_types(body, timeout=timeout)

List of account types

Returns the list of valid account types

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_type import AccountType
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
    api_instance = iikocloud_client.FinanceAccountTypeApi(api_client)
    body = None # object | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List of account types
        api_response = await api_instance.list_finance_account_types(body, timeout=timeout)
        print("The response of FinanceAccountTypeApi->list_finance_account_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountTypeApi->list_finance_account_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**List[AccountType]**](AccountType.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

