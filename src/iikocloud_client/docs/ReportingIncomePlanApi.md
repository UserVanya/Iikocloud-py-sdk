# iikocloud_client.ReportingIncomePlanApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_income_plan**](ReportingIncomePlanApi.md#get_income_plan) | **POST** /api/reporting/v1/income-plan/list | Get income plan


# **get_income_plan**
> GetIncomePlanResponse get_income_plan(get_income_plan_request, timeout=timeout)

Get income plan

Returns daily planned income values for an organization over the requested period.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_income_plan_request import GetIncomePlanRequest
from iikocloud_client.models.get_income_plan_response import GetIncomePlanResponse
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
    api_instance = iikocloud_client.ReportingIncomePlanApi(api_client)
    get_income_plan_request = iikocloud_client.GetIncomePlanRequest() # GetIncomePlanRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get income plan
        api_response = await api_instance.get_income_plan(get_income_plan_request, timeout=timeout)
        print("The response of ReportingIncomePlanApi->get_income_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingIncomePlanApi->get_income_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_income_plan_request** | [**GetIncomePlanRequest**](GetIncomePlanRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**GetIncomePlanResponse**](GetIncomePlanResponse.md)

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

