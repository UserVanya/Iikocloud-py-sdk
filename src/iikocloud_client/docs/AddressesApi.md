# iikocloud_client.AddressesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cities**](AddressesApi.md#get_cities) | **POST** /api/1/cities | Cities.
[**get_regions**](AddressesApi.md#get_regions) | **POST** /api/1/regions | Regions.
[**get_streets_by_city**](AddressesApi.md#get_streets_by_city) | **POST** /api/1/streets/by_city | Streets by city.
[**get_streets_by_id**](AddressesApi.md#get_streets_by_id) | **POST** /api/1/streets/by_id | Streets by id or by classifierId.


# **get_cities**
> CitiesResponse get_cities(timeout=timeout, cities_request=cities_request)

Cities.



 > Restriction group: `Data: geo`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cities_request import CitiesRequest
from iikocloud_client.models.cities_response import CitiesResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cities_request = iikocloud_client.CitiesRequest() # CitiesRequest |  (optional)

    try:
        # Cities.
        api_response = await api_instance.get_cities(timeout=timeout, cities_request=cities_request)
        print("The response of AddressesApi->get_cities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->get_cities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cities_request** | [**CitiesRequest**](CitiesRequest.md)|  | [optional] 

### Return type

[**CitiesResponse**](CitiesResponse.md)

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

# **get_regions**
> RegionsResponse get_regions(timeout=timeout, regions_request=regions_request)

Regions.



 > Restriction group: `Data: geo`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.regions_request import RegionsRequest
from iikocloud_client.models.regions_response import RegionsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    regions_request = iikocloud_client.RegionsRequest() # RegionsRequest |  (optional)

    try:
        # Regions.
        api_response = await api_instance.get_regions(timeout=timeout, regions_request=regions_request)
        print("The response of AddressesApi->get_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->get_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **regions_request** | [**RegionsRequest**](RegionsRequest.md)|  | [optional] 

### Return type

[**RegionsResponse**](RegionsResponse.md)

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

# **get_streets_by_city**
> StreetsResponse get_streets_by_city(timeout=timeout, streets_by_city_request=streets_by_city_request)

Streets by city.



 > Restriction group: `Data: geo`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.streets_by_city_request import StreetsByCityRequest
from iikocloud_client.models.streets_response import StreetsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    streets_by_city_request = iikocloud_client.StreetsByCityRequest() # StreetsByCityRequest |  (optional)

    try:
        # Streets by city.
        api_response = await api_instance.get_streets_by_city(timeout=timeout, streets_by_city_request=streets_by_city_request)
        print("The response of AddressesApi->get_streets_by_city:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->get_streets_by_city: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **streets_by_city_request** | [**StreetsByCityRequest**](StreetsByCityRequest.md)|  | [optional] 

### Return type

[**StreetsResponse**](StreetsResponse.md)

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

# **get_streets_by_id**
> StreetsByIdResponse get_streets_by_id(timeout=timeout, streets_by_id_request=streets_by_id_request)

Streets by id or by classifierId.



 > Restriction group: `Data: geo`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.streets_by_id_request import StreetsByIdRequest
from iikocloud_client.models.streets_by_id_response import StreetsByIdResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    streets_by_id_request = iikocloud_client.StreetsByIdRequest() # StreetsByIdRequest |  (optional)

    try:
        # Streets by id or by classifierId.
        api_response = await api_instance.get_streets_by_id(timeout=timeout, streets_by_id_request=streets_by_id_request)
        print("The response of AddressesApi->get_streets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->get_streets_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **streets_by_id_request** | [**StreetsByIdRequest**](StreetsByIdRequest.md)|  | [optional] 

### Return type

[**StreetsByIdResponse**](StreetsByIdResponse.md)

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

