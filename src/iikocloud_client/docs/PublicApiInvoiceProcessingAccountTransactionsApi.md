# iikocloud_client.PublicApiInvoiceProcessingAccountTransactionsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_account_transactions**](PublicApiInvoiceProcessingAccountTransactionsApi.md#list_finance_account_transactions) | **POST** /api/finance/v1/account_transactions/list | Get account transactions


# **list_finance_account_transactions**
> AccountTransactionsResponse list_finance_account_transactions(account_transactions_list_request)

Get account transactions

Returns a list of transactions for the specified account

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_transactions_list_request import AccountTransactionsListRequest
from iikocloud_client.models.account_transactions_response import AccountTransactionsResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingAccountTransactionsApi(api_client)
    account_transactions_list_request = iikocloud_client.AccountTransactionsListRequest() # AccountTransactionsListRequest | Request parameters

    try:
        # Get account transactions
        api_response = await api_instance.list_finance_account_transactions(account_transactions_list_request)
        print("The response of PublicApiInvoiceProcessingAccountTransactionsApi->list_finance_account_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingAccountTransactionsApi->list_finance_account_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_transactions_list_request** | [**AccountTransactionsListRequest**](AccountTransactionsListRequest.md)| Request parameters | 

### Return type

[**AccountTransactionsResponse**](AccountTransactionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

