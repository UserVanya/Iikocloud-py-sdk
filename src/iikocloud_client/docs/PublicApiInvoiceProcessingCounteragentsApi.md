# iikocloud_client.PublicApiInvoiceProcessingCounteragentsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_counteragents**](PublicApiInvoiceProcessingCounteragentsApi.md#get_inventory_counteragents) | **POST** /api/inventory/v1/counteragents | Get counteragents list


# **get_inventory_counteragents**
> GetCounteragentsResponse get_inventory_counteragents(get_counteragents_request)

Get counteragents list

Gets a list of counteragents with pagination and type filtering support

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_counteragents_request import GetCounteragentsRequest
from iikocloud_client.models.get_counteragents_response import GetCounteragentsResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingCounteragentsApi(api_client)
    get_counteragents_request = iikocloud_client.GetCounteragentsRequest() # GetCounteragentsRequest | Request parameters

    try:
        # Get counteragents list
        api_response = await api_instance.get_inventory_counteragents(get_counteragents_request)
        print("The response of PublicApiInvoiceProcessingCounteragentsApi->get_inventory_counteragents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingCounteragentsApi->get_inventory_counteragents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_counteragents_request** | [**GetCounteragentsRequest**](GetCounteragentsRequest.md)| Request parameters | 

### Return type

[**GetCounteragentsResponse**](GetCounteragentsResponse.md)

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
**403** | Access forbidden |  -  |
**405** | Method not allowed |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

