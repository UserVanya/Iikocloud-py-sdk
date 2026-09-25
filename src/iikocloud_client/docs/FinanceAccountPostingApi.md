# iikocloud_client.FinanceAccountPostingApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_account_postings**](FinanceAccountPostingApi.md#list_finance_account_postings) | **POST** /api/finance/v1/account-posting/list | Account postings


# **list_finance_account_postings**
> AccountPostingListResponse list_finance_account_postings(account_posting_list_request, timeout=timeout)

Account postings

Returns a list of postings for a financial account over a period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_posting_list_request import AccountPostingListRequest
from iikocloud_client.models.account_posting_list_response import AccountPostingListResponse
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
    api_instance = iikocloud_client.FinanceAccountPostingApi(api_client)
    account_posting_list_request = iikocloud_client.AccountPostingListRequest() # AccountPostingListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Account postings
        api_response = await api_instance.list_finance_account_postings(account_posting_list_request, timeout=timeout)
        print("The response of FinanceAccountPostingApi->list_finance_account_postings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountPostingApi->list_finance_account_postings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_posting_list_request** | [**AccountPostingListRequest**](AccountPostingListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountPostingListResponse**](AccountPostingListResponse.md)

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
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

