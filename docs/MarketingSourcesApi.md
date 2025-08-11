# iikocloud_client.MarketingSourcesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_marketing_sources_post**](MarketingSourcesApi.md#api1_marketing_sources_post) | **POST** /api/1/marketing_sources | Marketing sources.


# **api1_marketing_sources_post**
> TransportMarketingSourcesMarketingSourcesResponse api1_marketing_sources_post(timeout=timeout, transport_marketing_sources_marketing_sources_request=transport_marketing_sources_marketing_sources_request)

Marketing sources.



 > Allowed from version `7.2.5`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_marketing_sources_marketing_sources_request import TransportMarketingSourcesMarketingSourcesRequest
from iikocloud_client.models.transport_marketing_sources_marketing_sources_response import TransportMarketingSourcesMarketingSourcesResponse
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

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.MarketingSourcesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_marketing_sources_marketing_sources_request = iikocloud_client.TransportMarketingSourcesMarketingSourcesRequest() # TransportMarketingSourcesMarketingSourcesRequest |  (optional)

    try:
        # Marketing sources.
        api_response = await api_instance.api1_marketing_sources_post(timeout=timeout, transport_marketing_sources_marketing_sources_request=transport_marketing_sources_marketing_sources_request)
        print("The response of MarketingSourcesApi->api1_marketing_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingSourcesApi->api1_marketing_sources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_marketing_sources_marketing_sources_request** | [**TransportMarketingSourcesMarketingSourcesRequest**](TransportMarketingSourcesMarketingSourcesRequest.md)|  | [optional] 

### Return type

[**TransportMarketingSourcesMarketingSourcesResponse**](TransportMarketingSourcesMarketingSourcesResponse.md)

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

