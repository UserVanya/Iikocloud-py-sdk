# iikocloud_client.NomenclatureAssemblyChartApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#create_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/create | Create an assembly chart
[**create_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#create_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/create | Create an assembly chart (v2)
[**delete_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#delete_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/delete | Delete an assembly chart
[**delete_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#delete_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/delete | Delete an assembly chart (v2)
[**get_nomenclature_assembled_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembled_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/assembled | Get an assembled chart
[**get_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/get | Get an assembly chart by ID
[**get_nomenclature_assembly_chart_tree_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart_tree_v2) | **POST** /api/nomenclature/v2/assembly-chart/tree | Get an assembly chart tree
[**get_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/get | Get an assembly chart by ID (v2)
[**get_nomenclature_prepared_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_prepared_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/prepared | Get a prepared chart (breakdown to store items)
[**list_nomenclature_assembly_charts**](NomenclatureAssemblyChartApi.md#list_nomenclature_assembly_charts) | **POST** /api/nomenclature/v1/assembly-chart/list | Get a list of assembly charts by product
[**list_nomenclature_assembly_charts_v2**](NomenclatureAssemblyChartApi.md#list_nomenclature_assembly_charts_v2) | **POST** /api/nomenclature/v2/assembly-chart/list | Get a list of assembly charts by product (v2)
[**update_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#update_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/update | Update an assembly chart
[**update_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#update_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/update | Update an assembly chart (v2)


# **create_nomenclature_assembly_chart**
> AssemblyChartCommonResponse create_nomenclature_assembly_chart(create_request, timeout=timeout)

Create an assembly chart

Saves a new assembly chart for a product.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.create_request import CreateRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    create_request = iikocloud_client.CreateRequest() # CreateRequest | Request body for creating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create an assembly chart
        api_response = await api_instance.create_nomenclature_assembly_chart(create_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**CreateRequest**](CreateRequest.md)| Request body for creating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assembly chart created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse create_nomenclature_assembly_chart_v2(create_request, timeout=timeout)

Create an assembly chart (v2)

Saves a new assembly chart for a product.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.create_request import CreateRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    create_request = iikocloud_client.CreateRequest() # CreateRequest | Request body for creating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create an assembly chart (v2)
        api_response = await api_instance.create_nomenclature_assembly_chart_v2(create_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**CreateRequest**](CreateRequest.md)| Request body for creating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assembly chart created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_assembly_chart**
> AssemblyChartCommonResponse delete_nomenclature_assembly_chart(delete_request, timeout=timeout)

Delete an assembly chart

Deletes an assembly chart by UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.delete_request import DeleteRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    delete_request = iikocloud_client.DeleteRequest() # DeleteRequest | Request body for deleting an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete an assembly chart
        api_response = await api_instance.delete_nomenclature_assembly_chart(delete_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request** | [**DeleteRequest**](DeleteRequest.md)| Request body for deleting an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse delete_nomenclature_assembly_chart_v2(delete_request, timeout=timeout)

Delete an assembly chart (v2)

Deletes an assembly chart by UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.delete_request import DeleteRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    delete_request = iikocloud_client.DeleteRequest() # DeleteRequest | Request body for deleting an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete an assembly chart (v2)
        api_response = await api_instance.delete_nomenclature_assembly_chart_v2(delete_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request** | [**DeleteRequest**](DeleteRequest.md)| Request body for deleting an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembled_chart_v2**
> AssemblyChartResponse get_nomenclature_assembled_chart_v2(assembled_request, timeout=timeout)

Get an assembled chart

Returns the top-level assembly chart (without resolving nested ingredient charts) effective for
the product on the given date. If no chart is found, returns 200 with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembled_request import AssembledRequest
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembled_request = iikocloud_client.AssembledRequest() # AssembledRequest | Request body for getting an assembled chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembled chart
        api_response = await api_instance.get_nomenclature_assembled_chart_v2(assembled_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembled_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembled_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembled_request** | [**AssembledRequest**](AssembledRequest.md)| Request body for getting an assembled chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembled assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart**
> AssemblyChartResponse get_nomenclature_assembly_chart(get_request, timeout=timeout)

Get an assembly chart by ID

Returns a single assembly chart by its UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
from iikocloud_client.models.get_request import GetRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    get_request = iikocloud_client.GetRequest() # GetRequest | Request body for getting an assembly chart by ID
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart by ID
        api_response = await api_instance.get_nomenclature_assembly_chart(get_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_request** | [**GetRequest**](GetRequest.md)| Request body for getting an assembly chart by ID | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart_tree_v2**
> ChartTreeNodeDto get_nomenclature_assembly_chart_tree_v2(tree_request, timeout=timeout)

Get an assembly chart tree

Returns the assembly chart tree of the product for the given date: for every ingredient that has
its own assembly chart, its composition is recursively resolved. If no chart is found, returns 200
with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.chart_tree_node_dto import ChartTreeNodeDto
from iikocloud_client.models.tree_request import TreeRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    tree_request = iikocloud_client.TreeRequest() # TreeRequest | Request body for getting an assembly chart tree
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart tree
        api_response = await api_instance.get_nomenclature_assembly_chart_tree_v2(tree_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_tree_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_tree_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_request** | [**TreeRequest**](TreeRequest.md)| Request body for getting an assembly chart tree | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ChartTreeNodeDto**](ChartTreeNodeDto.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart tree |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart_v2**
> AssemblyChartResponse get_nomenclature_assembly_chart_v2(get_request, timeout=timeout)

Get an assembly chart by ID (v2)

Returns a single assembly chart by its UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
from iikocloud_client.models.get_request import GetRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    get_request = iikocloud_client.GetRequest() # GetRequest | Request body for getting an assembly chart by ID
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart by ID (v2)
        api_response = await api_instance.get_nomenclature_assembly_chart_v2(get_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_request** | [**GetRequest**](GetRequest.md)| Request body for getting an assembly chart by ID | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_prepared_chart_v2**
> PreparedChartDto get_nomenclature_prepared_chart_v2(prepared_request, timeout=timeout)

Get a prepared chart (breakdown to store items)

Returns the recipe breakdown of the product down to elementary store items (ingredients written
off from stock) for the given date. If no chart is found, returns 200 with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.prepared_chart_dto import PreparedChartDto
from iikocloud_client.models.prepared_request import PreparedRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    prepared_request = iikocloud_client.PreparedRequest() # PreparedRequest | Request body for getting a prepared chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a prepared chart (breakdown to store items)
        api_response = await api_instance.get_nomenclature_prepared_chart_v2(prepared_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_prepared_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_prepared_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepared_request** | [**PreparedRequest**](PreparedRequest.md)| Request body for getting a prepared chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**PreparedChartDto**](PreparedChartDto.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prepared chart (breakdown to store items) |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_assembly_charts**
> ListResponse list_nomenclature_assembly_charts(list_request, timeout=timeout)

Get a list of assembly charts by product

Returns the history of assembly charts for a product.
The filter `product eq` is required. The optional `department eq` filter restricts results to a specific department.
Pagination (limit / offset) is applied client-side.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.list_response import ListResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Parameters for the assembly chart list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of assembly charts by product
        api_response = await api_instance.list_nomenclature_assembly_charts(list_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Parameters for the assembly chart list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assembly charts |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_assembly_charts_v2**
> AssemblyChartListResponse list_nomenclature_assembly_charts_v2(assembly_chart_list_request, timeout=timeout)

Get a list of assembly charts by product (v2)

Returns the history of assembly charts for a product.
The filter `product eq` is required. The optional `department eq` filter restricts results to a specific department.
Pagination (limit / offset) is applied client-side.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_list_request import AssemblyChartListRequest
from iikocloud_client.models.assembly_chart_list_response import AssemblyChartListResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_list_request = iikocloud_client.AssemblyChartListRequest() # AssemblyChartListRequest | Parameters for the assembly chart list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of assembly charts by product (v2)
        api_response = await api_instance.list_nomenclature_assembly_charts_v2(assembly_chart_list_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_list_request** | [**AssemblyChartListRequest**](AssemblyChartListRequest.md)| Parameters for the assembly chart list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartListResponse**](AssemblyChartListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assembly charts |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_assembly_chart**
> AssemblyChartCommonResponse update_nomenclature_assembly_chart(assembly_chart_v1_save_request, timeout=timeout)

Update an assembly chart

Updates an existing assembly chart.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.assembly_chart_v1_save_request import AssemblyChartV1SaveRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_v1_save_request = iikocloud_client.AssemblyChartV1SaveRequest() # AssemblyChartV1SaveRequest | Request body for updating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update an assembly chart
        api_response = await api_instance.update_nomenclature_assembly_chart(assembly_chart_v1_save_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_v1_save_request** | [**AssemblyChartV1SaveRequest**](AssemblyChartV1SaveRequest.md)| Request body for updating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse update_nomenclature_assembly_chart_v2(assembly_chart_v2_save_request, timeout=timeout)

Update an assembly chart (v2)

Updates an existing assembly chart.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.assembly_chart_v2_save_request import AssemblyChartV2SaveRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_v2_save_request = iikocloud_client.AssemblyChartV2SaveRequest() # AssemblyChartV2SaveRequest | Request body for updating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update an assembly chart (v2)
        api_response = await api_instance.update_nomenclature_assembly_chart_v2(assembly_chart_v2_save_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_v2_save_request** | [**AssemblyChartV2SaveRequest**](AssemblyChartV2SaveRequest.md)| Request body for updating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

