# iikocloud_client.AddressesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cities_post**](AddressesApi.md#cities_post) | **POST** /cities | Cities.
[**regions_post**](AddressesApi.md#regions_post) | **POST** /regions | Regions.
[**streets_by_city_post**](AddressesApi.md#streets_by_city_post) | **POST** /streets/by_city | Streets by city.
[**streets_by_id_post**](AddressesApi.md#streets_by_id_post) | **POST** /streets/by_id | Streets by id or by classifierId.


# **cities_post**
> AddressCitiesResponse cities_post(timeout=timeout, address_cities_request=address_cities_request)

Cities.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.address_cities_request import AddressCitiesRequest
from iikocloud_client.models.address_cities_response import AddressCitiesResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    address_cities_request = iikocloud_client.AddressCitiesRequest() # AddressCitiesRequest |  (optional)

    try:
        # Cities.
        api_response = await api_instance.cities_post(timeout=timeout, address_cities_request=address_cities_request)
        print("The response of AddressesApi->cities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->cities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **address_cities_request** | [**AddressCitiesRequest**](AddressCitiesRequest.md)|  | [optional] 

### Return type

[**AddressCitiesResponse**](AddressCitiesResponse.md)

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

# **regions_post**
> AddressRegionsResponse regions_post(timeout=timeout, address_regions_request=address_regions_request)

Regions.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.address_regions_request import AddressRegionsRequest
from iikocloud_client.models.address_regions_response import AddressRegionsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    address_regions_request = iikocloud_client.AddressRegionsRequest() # AddressRegionsRequest |  (optional)

    try:
        # Regions.
        api_response = await api_instance.regions_post(timeout=timeout, address_regions_request=address_regions_request)
        print("The response of AddressesApi->regions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->regions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **address_regions_request** | [**AddressRegionsRequest**](AddressRegionsRequest.md)|  | [optional] 

### Return type

[**AddressRegionsResponse**](AddressRegionsResponse.md)

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

# **streets_by_city_post**
> AddressStreetsResponse streets_by_city_post(timeout=timeout, address_streets_by_city_request=address_streets_by_city_request)

Streets by city.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.address_streets_by_city_request import AddressStreetsByCityRequest
from iikocloud_client.models.address_streets_response import AddressStreetsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    address_streets_by_city_request = iikocloud_client.AddressStreetsByCityRequest() # AddressStreetsByCityRequest |  (optional)

    try:
        # Streets by city.
        api_response = await api_instance.streets_by_city_post(timeout=timeout, address_streets_by_city_request=address_streets_by_city_request)
        print("The response of AddressesApi->streets_by_city_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->streets_by_city_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **address_streets_by_city_request** | [**AddressStreetsByCityRequest**](AddressStreetsByCityRequest.md)|  | [optional] 

### Return type

[**AddressStreetsResponse**](AddressStreetsResponse.md)

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

# **streets_by_id_post**
> AddressStreetsByIdResponse streets_by_id_post(timeout=timeout, address_streets_by_id_request=address_streets_by_id_request)

Streets by id or by classifierId.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.address_streets_by_id_request import AddressStreetsByIdRequest
from iikocloud_client.models.address_streets_by_id_response import AddressStreetsByIdResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    address_streets_by_id_request = iikocloud_client.AddressStreetsByIdRequest() # AddressStreetsByIdRequest |  (optional)

    try:
        # Streets by id or by classifierId.
        api_response = await api_instance.streets_by_id_post(timeout=timeout, address_streets_by_id_request=address_streets_by_id_request)
        print("The response of AddressesApi->streets_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->streets_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **address_streets_by_id_request** | [**AddressStreetsByIdRequest**](AddressStreetsByIdRequest.md)|  | [optional] 

### Return type

[**AddressStreetsByIdResponse**](AddressStreetsByIdResponse.md)

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

