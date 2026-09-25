# iikocloud_client.ReportingOlapApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_olap_report**](ReportingOlapApi.md#get_olap_report) | **POST** /api/reporting/v1/olap/get | Run OLAP report
[**get_olap_report_columns**](ReportingOlapApi.md#get_olap_report_columns) | **POST** /api/reporting/v1/olap/columns/get | Get OLAP report columns


# **get_olap_report**
> GetOlapReportResponse get_olap_report(get_olap_report_request, timeout=timeout)

Run OLAP report

Builds an OLAP report on sales, transactions or deliveries with an arbitrary configuration and returns its data (`data`) and totals (`summary`). This is the main way for an integrator to build analytical data marts and management reporting: the client defines the row and column grouping fields, aggregate fields and filters.
Field names (`groupByRowFields`, `groupByColFields`, `aggregateFields`, `filters`) are taken from the metadata of the `olap/columns/get` method. The set of available fields changes between versions of the server's internal API, so request the current metadata before building a report.
Every request must contain a date filter. Recommended date fields: `OpenDate.Typed` for SALES and DELIVERIES, `DateTime.DateTyped` (or `DateTime.Typed`) for TRANSACTIONS.
<b>Caution!</> A query that is too broad: a long period, a large number of restaurants or fields/groupings, as well as balance fields (`StartBalance.*`, `FinalBalance.*`), which are calculated over the entire transaction history, may take a long time to run or return no result. Split large queries into smaller sequential queries with a narrow period. To get balances, use specialized methods instead of OLAP.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_olap_report_request import GetOlapReportRequest
from iikocloud_client.models.get_olap_report_response import GetOlapReportResponse
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
    api_instance = iikocloud_client.ReportingOlapApi(api_client)
    get_olap_report_request = iikocloud_client.GetOlapReportRequest() # GetOlapReportRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Run OLAP report
        api_response = await api_instance.get_olap_report(get_olap_report_request, timeout=timeout)
        print("The response of ReportingOlapApi->get_olap_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingOlapApi->get_olap_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_olap_report_request** | [**GetOlapReportRequest**](GetOlapReportRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**GetOlapReportResponse**](GetOlapReportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | RMS returned a technical error |  -  |
**504** | RMS did not respond in time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_olap_report_columns**
> List[OlapColumn] get_olap_report_columns(get_olap_columns_request, timeout=timeout)

Get OLAP report columns

Returns the list of columns available in the OLAP report of the given type (`reportType`)

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_olap_columns_request import GetOlapColumnsRequest
from iikocloud_client.models.olap_column import OlapColumn
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
    api_instance = iikocloud_client.ReportingOlapApi(api_client)
    get_olap_columns_request = iikocloud_client.GetOlapColumnsRequest() # GetOlapColumnsRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get OLAP report columns
        api_response = await api_instance.get_olap_report_columns(get_olap_columns_request, timeout=timeout)
        print("The response of ReportingOlapApi->get_olap_report_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingOlapApi->get_olap_report_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_olap_columns_request** | [**GetOlapColumnsRequest**](GetOlapColumnsRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**List[OlapColumn]**](OlapColumn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | RMS returned a technical error |  -  |
**504** | RMS did not respond in time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

