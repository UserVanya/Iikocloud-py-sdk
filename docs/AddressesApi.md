# iikocloud_client.AddressesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_cities_post**](AddressesApi.md#api1_cities_post) | **POST** /api/1/cities | Cities.
[**api1_regions_post**](AddressesApi.md#api1_regions_post) | **POST** /api/1/regions | Regions.
[**api1_streets_by_city_post**](AddressesApi.md#api1_streets_by_city_post) | **POST** /api/1/streets/by_city | Streets by city.
[**api1_streets_by_id_post**](AddressesApi.md#api1_streets_by_id_post) | **POST** /api/1/streets/by_id | Streets by id or by classifierId.


# **api1_cities_post**
> TransportAddressCitiesResponse api1_cities_post(timeout=timeout, transport_address_cities_request=transport_address_cities_request)

Cities.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_address_cities_request import TransportAddressCitiesRequest
from iikocloud_client.models.transport_address_cities_response import TransportAddressCitiesResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_address_cities_request = iikocloud_client.TransportAddressCitiesRequest() # TransportAddressCitiesRequest |  (optional)

    try:
        # Cities.
        api_response = await api_instance.api1_cities_post(timeout=timeout, transport_address_cities_request=transport_address_cities_request)
        print("The response of AddressesApi->api1_cities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->api1_cities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_address_cities_request** | [**TransportAddressCitiesRequest**](TransportAddressCitiesRequest.md)|  | [optional] 

### Return type

[**TransportAddressCitiesResponse**](TransportAddressCitiesResponse.md)

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

# **api1_regions_post**
> TransportAddressRegionsResponse api1_regions_post(timeout=timeout, transport_address_regions_request=transport_address_regions_request)

Regions.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_address_regions_request import TransportAddressRegionsRequest
from iikocloud_client.models.transport_address_regions_response import TransportAddressRegionsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_address_regions_request = iikocloud_client.TransportAddressRegionsRequest() # TransportAddressRegionsRequest |  (optional)

    try:
        # Regions.
        api_response = await api_instance.api1_regions_post(timeout=timeout, transport_address_regions_request=transport_address_regions_request)
        print("The response of AddressesApi->api1_regions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->api1_regions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_address_regions_request** | [**TransportAddressRegionsRequest**](TransportAddressRegionsRequest.md)|  | [optional] 

### Return type

[**TransportAddressRegionsResponse**](TransportAddressRegionsResponse.md)

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

# **api1_streets_by_city_post**
> TransportAddressStreetsResponse api1_streets_by_city_post(timeout=timeout, transport_address_streets_by_city_request=transport_address_streets_by_city_request)

Streets by city.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_address_streets_by_city_request import TransportAddressStreetsByCityRequest
from iikocloud_client.models.transport_address_streets_response import TransportAddressStreetsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_address_streets_by_city_request = iikocloud_client.TransportAddressStreetsByCityRequest() # TransportAddressStreetsByCityRequest |  (optional)

    try:
        # Streets by city.
        api_response = await api_instance.api1_streets_by_city_post(timeout=timeout, transport_address_streets_by_city_request=transport_address_streets_by_city_request)
        print("The response of AddressesApi->api1_streets_by_city_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->api1_streets_by_city_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_address_streets_by_city_request** | [**TransportAddressStreetsByCityRequest**](TransportAddressStreetsByCityRequest.md)|  | [optional] 

### Return type

[**TransportAddressStreetsResponse**](TransportAddressStreetsResponse.md)

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

# **api1_streets_by_id_post**
> TransportAddressStreetsByIdResponse api1_streets_by_id_post(timeout=timeout, transport_address_streets_by_id_request=transport_address_streets_by_id_request)

Streets by id or by classifierId.



 > Restriction group: `Data: geo`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_address_streets_by_id_request import TransportAddressStreetsByIdRequest
from iikocloud_client.models.transport_address_streets_by_id_response import TransportAddressStreetsByIdResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_address_streets_by_id_request = iikocloud_client.TransportAddressStreetsByIdRequest() # TransportAddressStreetsByIdRequest |  (optional)

    try:
        # Streets by id or by classifierId.
        api_response = await api_instance.api1_streets_by_id_post(timeout=timeout, transport_address_streets_by_id_request=transport_address_streets_by_id_request)
        print("The response of AddressesApi->api1_streets_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->api1_streets_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_address_streets_by_id_request** | [**TransportAddressStreetsByIdRequest**](TransportAddressStreetsByIdRequest.md)|  | [optional] 

### Return type

[**TransportAddressStreetsByIdResponse**](TransportAddressStreetsByIdResponse.md)

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

