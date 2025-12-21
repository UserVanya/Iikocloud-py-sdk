# iikocloud_client.MarketingSourcesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketing_sources_post**](MarketingSourcesApi.md#marketing_sources_post) | **POST** /marketing_sources | Marketing sources.


# **marketing_sources_post**
> IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse marketing_sources_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request=iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request)

Marketing sources.



 > Allowed from version `7.2.5`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request import IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_marketing_sources_marketing_sources_response import IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse
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
    api_instance = iikocloud_client.MarketingSourcesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request = iikocloud_client.IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest() # IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest |  (optional)

    try:
        # Marketing sources.
        api_response = await api_instance.marketing_sources_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request=iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request)
        print("The response of MarketingSourcesApi->marketing_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingSourcesApi->marketing_sources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_marketing_sources_marketing_sources_request** | [**IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest**](IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse**](IikoTransportPublicApiContractsMarketingSourcesMarketingSourcesResponse.md)

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

