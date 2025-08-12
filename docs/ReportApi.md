# iikocloud_client.ReportApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_customer_transactions_by_date_post**](ReportApi.md#loyalty_iiko_customer_transactions_by_date_post) | **POST** /loyalty/iiko/customer/transactions/by_date | Get transaction report by period.
[**loyalty_iiko_customer_transactions_by_revision_post**](ReportApi.md#loyalty_iiko_customer_transactions_by_revision_post) | **POST** /loyalty/iiko/customer/transactions/by_revision | Get transaction report by revision.


# **loyalty_iiko_customer_transactions_by_date_post**
> NetReportGetTransactionsReportByPeriodResponse loyalty_iiko_customer_transactions_by_date_post(timeout=timeout, net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request)

Get transaction report by period.

Get transaction report for specified customer by provided date range.

 > Restriction group: `Guests: info`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_report_get_transactions_report_by_period_request import NetReportGetTransactionsReportByPeriodRequest
from iikocloud_client.models.net_report_get_transactions_report_by_period_response import NetReportGetTransactionsReportByPeriodResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_report_get_transactions_report_by_period_request = iikocloud_client.NetReportGetTransactionsReportByPeriodRequest() # NetReportGetTransactionsReportByPeriodRequest |  (optional)

    try:
        # Get transaction report by period.
        api_response = await api_instance.loyalty_iiko_customer_transactions_by_date_post(timeout=timeout, net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request)
        print("The response of ReportApi->loyalty_iiko_customer_transactions_by_date_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->loyalty_iiko_customer_transactions_by_date_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_report_get_transactions_report_by_period_request** | [**NetReportGetTransactionsReportByPeriodRequest**](NetReportGetTransactionsReportByPeriodRequest.md)|  | [optional] 

### Return type

[**NetReportGetTransactionsReportByPeriodResponse**](NetReportGetTransactionsReportByPeriodResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **loyalty_iiko_customer_transactions_by_revision_post**
> NetReportGetTransactionsReportByRevisionResponse loyalty_iiko_customer_transactions_by_revision_post(timeout=timeout, net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request)

Get transaction report by revision.

Get transaction report for specified customer by provided revision.

 > Restriction group: `Guests: info`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_report_get_transactions_report_by_revision_request import NetReportGetTransactionsReportByRevisionRequest
from iikocloud_client.models.net_report_get_transactions_report_by_revision_response import NetReportGetTransactionsReportByRevisionResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_report_get_transactions_report_by_revision_request = iikocloud_client.NetReportGetTransactionsReportByRevisionRequest() # NetReportGetTransactionsReportByRevisionRequest |  (optional)

    try:
        # Get transaction report by revision.
        api_response = await api_instance.loyalty_iiko_customer_transactions_by_revision_post(timeout=timeout, net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request)
        print("The response of ReportApi->loyalty_iiko_customer_transactions_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->loyalty_iiko_customer_transactions_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_report_get_transactions_report_by_revision_request** | [**NetReportGetTransactionsReportByRevisionRequest**](NetReportGetTransactionsReportByRevisionRequest.md)|  | [optional] 

### Return type

[**NetReportGetTransactionsReportByRevisionResponse**](NetReportGetTransactionsReportByRevisionResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

