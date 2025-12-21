# iikocloud_client.MarketingSourcesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketing_sources_post**](MarketingSourcesApi.md#marketing_sources_post) | **POST** /marketing_sources | Marketing sources.


# **marketing_sources_post**
> MarketingSourcesMarketingSourcesResponse marketing_sources_post(timeout=timeout, marketing_sources_marketing_sources_request=marketing_sources_marketing_sources_request)

Marketing sources.



 > Allowed from version `7.2.5`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.marketing_sources_marketing_sources_request import MarketingSourcesMarketingSourcesRequest
from iikocloud_client.models.marketing_sources_marketing_sources_response import MarketingSourcesMarketingSourcesResponse
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
    api_instance = iikocloud_client.MarketingSourcesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    marketing_sources_marketing_sources_request = iikocloud_client.MarketingSourcesMarketingSourcesRequest() # MarketingSourcesMarketingSourcesRequest |  (optional)

    try:
        # Marketing sources.
        api_response = await api_instance.marketing_sources_post(timeout=timeout, marketing_sources_marketing_sources_request=marketing_sources_marketing_sources_request)
        print("The response of MarketingSourcesApi->marketing_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingSourcesApi->marketing_sources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **marketing_sources_marketing_sources_request** | [**MarketingSourcesMarketingSourcesRequest**](MarketingSourcesMarketingSourcesRequest.md)|  | [optional] 

### Return type

[**MarketingSourcesMarketingSourcesResponse**](MarketingSourcesMarketingSourcesResponse.md)

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

