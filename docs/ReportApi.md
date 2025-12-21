# iikocloud_client.ReportApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_customer_transactions_by_date_post**](ReportApi.md#loyalty_iiko_customer_transactions_by_date_post) | **POST** /loyalty/iiko/customer/transactions/by_date | Get transaction report by period.
[**loyalty_iiko_customer_transactions_by_revision_post**](ReportApi.md#loyalty_iiko_customer_transactions_by_revision_post) | **POST** /loyalty/iiko/customer/transactions/by_revision | Get transaction report by revision.


# **loyalty_iiko_customer_transactions_by_date_post**
> IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse loyalty_iiko_customer_transactions_by_date_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request=iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request)

Get transaction report by period.

Get transaction report for specified customer by provided date range.

 > Restriction group: `Guests: info`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_response import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest() # IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest |  (optional)

    try:
        # Get transaction report by period.
        api_response = await api_instance.loyalty_iiko_customer_transactions_by_date_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request=iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request)
        print("The response of ReportApi->loyalty_iiko_customer_transactions_by_date_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->loyalty_iiko_customer_transactions_by_date_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_period_request** | [**IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest**](IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse**](IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByPeriodResponse.md)

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

# **loyalty_iiko_customer_transactions_by_revision_post**
> IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse loyalty_iiko_customer_transactions_by_revision_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request=iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request)

Get transaction report by revision.

Get transaction report for specified customer by provided revision.

 > Restriction group: `Guests: info`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_response import IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.ReportApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest() # IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest |  (optional)

    try:
        # Get transaction report by revision.
        api_response = await api_instance.loyalty_iiko_customer_transactions_by_revision_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request=iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request)
        print("The response of ReportApi->loyalty_iiko_customer_transactions_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->loyalty_iiko_customer_transactions_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_report_get_transactions_report_by_revision_request** | [**IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest**](IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse**](IikoNetServiceContractsApiIikoTransportReportGetTransactionsReportByRevisionResponse.md)

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

