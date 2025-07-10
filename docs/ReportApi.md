# iiko_cloud_client.ReportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_loyalty_iiko_customer_transactions_by_date_post**](ReportApi.md#api1_loyalty_iiko_customer_transactions_by_date_post) | **POST** /api/1/loyalty/iiko/customer/transactions/by_date | Get transaction report by period.
[**api1_loyalty_iiko_customer_transactions_by_revision_post**](ReportApi.md#api1_loyalty_iiko_customer_transactions_by_revision_post) | **POST** /api/1/loyalty/iiko/customer/transactions/by_revision | Get transaction report by revision.


# **api1_loyalty_iiko_customer_transactions_by_date_post**
> NetReportGetTransactionsReportByPeriodResponse api1_loyalty_iiko_customer_transactions_by_date_post(authorization, timeout=timeout, net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request)

Get transaction report by period.

Get transaction report for specified customer by provided date range.

 > Restriction group: `Guests: info`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_report_get_transactions_report_by_period_request import NetReportGetTransactionsReportByPeriodRequest
from iiko_cloud_client.models.net_report_get_transactions_report_by_period_response import NetReportGetTransactionsReportByPeriodResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.ReportApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_report_get_transactions_report_by_period_request = iiko_cloud_client.NetReportGetTransactionsReportByPeriodRequest() # NetReportGetTransactionsReportByPeriodRequest |  (optional)

    try:
        # Get transaction report by period.
        api_response = await api_instance.api1_loyalty_iiko_customer_transactions_by_date_post(authorization, timeout=timeout, net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request)
        print("The response of ReportApi->api1_loyalty_iiko_customer_transactions_by_date_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->api1_loyalty_iiko_customer_transactions_by_date_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_report_get_transactions_report_by_period_request** | [**NetReportGetTransactionsReportByPeriodRequest**](NetReportGetTransactionsReportByPeriodRequest.md)|  | [optional] 

### Return type

[**NetReportGetTransactionsReportByPeriodResponse**](NetReportGetTransactionsReportByPeriodResponse.md)

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

# **api1_loyalty_iiko_customer_transactions_by_revision_post**
> NetReportGetTransactionsReportByRevisionResponse api1_loyalty_iiko_customer_transactions_by_revision_post(authorization, timeout=timeout, net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request)

Get transaction report by revision.

Get transaction report for specified customer by provided revision.

 > Restriction group: `Guests: info`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_report_get_transactions_report_by_revision_request import NetReportGetTransactionsReportByRevisionRequest
from iiko_cloud_client.models.net_report_get_transactions_report_by_revision_response import NetReportGetTransactionsReportByRevisionResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.ReportApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_report_get_transactions_report_by_revision_request = iiko_cloud_client.NetReportGetTransactionsReportByRevisionRequest() # NetReportGetTransactionsReportByRevisionRequest |  (optional)

    try:
        # Get transaction report by revision.
        api_response = await api_instance.api1_loyalty_iiko_customer_transactions_by_revision_post(authorization, timeout=timeout, net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request)
        print("The response of ReportApi->api1_loyalty_iiko_customer_transactions_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->api1_loyalty_iiko_customer_transactions_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_report_get_transactions_report_by_revision_request** | [**NetReportGetTransactionsReportByRevisionRequest**](NetReportGetTransactionsReportByRevisionRequest.md)|  | [optional] 

### Return type

[**NetReportGetTransactionsReportByRevisionResponse**](NetReportGetTransactionsReportByRevisionResponse.md)

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

