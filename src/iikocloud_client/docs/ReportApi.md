# iikocloud_client.ReportApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_transactions_by_date**](ReportApi.md#get_customer_transactions_by_date) | **POST** /api/1/loyalty/iiko/customer/transactions/by_date | Get transaction report by period.
[**get_customer_transactions_by_revision**](ReportApi.md#get_customer_transactions_by_revision) | **POST** /api/1/loyalty/iiko/customer/transactions/by_revision | Get transaction report by revision.


# **get_customer_transactions_by_date**
> GetTransactionsReportByPeriodResponse get_customer_transactions_by_date(timeout=timeout, get_transactions_report_by_period_request=get_transactions_report_by_period_request)

Get transaction report by period.

Get transaction report for specified customer by provided date range.

 > Restriction group: `Guests: info`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_transactions_report_by_period_request import GetTransactionsReportByPeriodRequest
from iikocloud_client.models.get_transactions_report_by_period_response import GetTransactionsReportByPeriodResponse
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
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_transactions_report_by_period_request = iikocloud_client.GetTransactionsReportByPeriodRequest() # GetTransactionsReportByPeriodRequest |  (optional)

    try:
        # Get transaction report by period.
        api_response = await api_instance.get_customer_transactions_by_date(timeout=timeout, get_transactions_report_by_period_request=get_transactions_report_by_period_request)
        print("The response of ReportApi->get_customer_transactions_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_customer_transactions_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_transactions_report_by_period_request** | [**GetTransactionsReportByPeriodRequest**](GetTransactionsReportByPeriodRequest.md)|  | [optional] 

### Return type

[**GetTransactionsReportByPeriodResponse**](GetTransactionsReportByPeriodResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_transactions_by_revision**
> GetTransactionsReportByRevisionResponse get_customer_transactions_by_revision(timeout=timeout, get_transactions_report_by_revision_request=get_transactions_report_by_revision_request)

Get transaction report by revision.

Get transaction report for specified customer by provided revision.

 > Restriction group: `Guests: info`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_transactions_report_by_revision_request import GetTransactionsReportByRevisionRequest
from iikocloud_client.models.get_transactions_report_by_revision_response import GetTransactionsReportByRevisionResponse
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
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_transactions_report_by_revision_request = iikocloud_client.GetTransactionsReportByRevisionRequest() # GetTransactionsReportByRevisionRequest |  (optional)

    try:
        # Get transaction report by revision.
        api_response = await api_instance.get_customer_transactions_by_revision(timeout=timeout, get_transactions_report_by_revision_request=get_transactions_report_by_revision_request)
        print("The response of ReportApi->get_customer_transactions_by_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_customer_transactions_by_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_transactions_report_by_revision_request** | [**GetTransactionsReportByRevisionRequest**](GetTransactionsReportByRevisionRequest.md)|  | [optional] 

### Return type

[**GetTransactionsReportByRevisionResponse**](GetTransactionsReportByRevisionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

