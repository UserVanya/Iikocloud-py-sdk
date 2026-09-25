# iikocloud_client.FinanceChartOfAccountsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_chart_of_accounts**](FinanceChartOfAccountsApi.md#list_finance_chart_of_accounts) | **POST** /api/finance/v1/chart-of-accounts/list | Chart of accounts


# **list_finance_chart_of_accounts**
> ChartOfAccountsListResponse list_finance_chart_of_accounts(chart_of_accounts_list_request, timeout=timeout)

Chart of accounts

Returns the chart of financial accounts

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.chart_of_accounts_list_request import ChartOfAccountsListRequest
from iikocloud_client.models.chart_of_accounts_list_response import ChartOfAccountsListResponse
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
    api_instance = iikocloud_client.FinanceChartOfAccountsApi(api_client)
    chart_of_accounts_list_request = iikocloud_client.ChartOfAccountsListRequest() # ChartOfAccountsListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Chart of accounts
        api_response = await api_instance.list_finance_chart_of_accounts(chart_of_accounts_list_request, timeout=timeout)
        print("The response of FinanceChartOfAccountsApi->list_finance_chart_of_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceChartOfAccountsApi->list_finance_chart_of_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart_of_accounts_list_request** | [**ChartOfAccountsListRequest**](ChartOfAccountsListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ChartOfAccountsListResponse**](ChartOfAccountsListResponse.md)

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

