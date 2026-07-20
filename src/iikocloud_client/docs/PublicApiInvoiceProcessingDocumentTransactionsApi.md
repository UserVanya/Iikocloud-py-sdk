# iikocloud_client.PublicApiInvoiceProcessingDocumentTransactionsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_document_transactions**](PublicApiInvoiceProcessingDocumentTransactionsApi.md#list_finance_document_transactions) | **POST** /api/finance/v1/document_transactions/list | Get document transactions


# **list_finance_document_transactions**
> List[DocumentTransactionItem] list_finance_document_transactions(document_transactions_list_request)

Get document transactions

Returns a list of transactions for the specified document

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.document_transaction_item import DocumentTransactionItem
from iikocloud_client.models.document_transactions_list_request import DocumentTransactionsListRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDocumentTransactionsApi(api_client)
    document_transactions_list_request = iikocloud_client.DocumentTransactionsListRequest() # DocumentTransactionsListRequest | Request parameters

    try:
        # Get document transactions
        api_response = await api_instance.list_finance_document_transactions(document_transactions_list_request)
        print("The response of PublicApiInvoiceProcessingDocumentTransactionsApi->list_finance_document_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDocumentTransactionsApi->list_finance_document_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_transactions_list_request** | [**DocumentTransactionsListRequest**](DocumentTransactionsListRequest.md)| Request parameters | 

### Return type

[**List[DocumentTransactionItem]**](DocumentTransactionItem.md)

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

