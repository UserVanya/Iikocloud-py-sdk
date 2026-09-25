# iikocloud_client.LicensesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_licenses**](LicensesApi.md#list_licenses) | **POST** /api/licenses/v2/list | Get license list information for the API login.


# **list_licenses**
> GetLicenseListResponse list_licenses(timeout=timeout, get_license_list_request=get_license_list_request)

Get license list information for the API login.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_license_list_request import GetLicenseListRequest
from iikocloud_client.models.get_license_list_response import GetLicenseListResponse
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
    api_instance = iikocloud_client.LicensesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_license_list_request = iikocloud_client.GetLicenseListRequest() # GetLicenseListRequest |  (optional)

    try:
        # Get license list information for the API login.
        api_response = await api_instance.list_licenses(timeout=timeout, get_license_list_request=get_license_list_request)
        print("The response of LicensesApi->list_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->list_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_license_list_request** | [**GetLicenseListRequest**](GetLicenseListRequest.md)|  | [optional] 

### Return type

[**GetLicenseListResponse**](GetLicenseListResponse.md)

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

