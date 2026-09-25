# iikocloud_client.NomenclatureDirectoriesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_nomenclature_allergen_groups**](NomenclatureDirectoriesApi.md#list_nomenclature_allergen_groups) | **POST** /api/nomenclature/v1/allergen-group/list | Get a list of allergen groups
[**list_nomenclature_amount_units**](NomenclatureDirectoriesApi.md#list_nomenclature_amount_units) | **POST** /api/nomenclature/v1/amount-unit/list | Get a list of amount units
[**list_nomenclature_containers**](NomenclatureDirectoriesApi.md#list_nomenclature_containers) | **POST** /api/nomenclature/v1/container/list | Get a list of containers
[**list_nomenclature_custom_categories**](NomenclatureDirectoriesApi.md#list_nomenclature_custom_categories) | **POST** /api/nomenclature/v1/custom-category/list | Get a list of custom categories
[**list_nomenclature_menu_sections**](NomenclatureDirectoriesApi.md#list_nomenclature_menu_sections) | **POST** /api/nomenclature/v1/menu/list | Get a list of menu sections
[**list_nomenclature_modifier_schemas**](NomenclatureDirectoriesApi.md#list_nomenclature_modifier_schemas) | **POST** /api/nomenclature/v1/modifier-schema/list | Get a list of modifier schemas
[**list_nomenclature_place_types**](NomenclatureDirectoriesApi.md#list_nomenclature_place_types) | **POST** /api/nomenclature/v1/place-type/list | Get a list of preparation place types
[**list_nomenclature_producers**](NomenclatureDirectoriesApi.md#list_nomenclature_producers) | **POST** /api/nomenclature/v1/producer/list | Get a list of producers
[**list_nomenclature_product_sizes**](NomenclatureDirectoriesApi.md#list_nomenclature_product_sizes) | **POST** /api/nomenclature/v1/product-size/list | Get a list of product sizes
[**list_nomenclature_product_tags**](NomenclatureDirectoriesApi.md#list_nomenclature_product_tags) | **POST** /api/nomenclature/v1/product-tag/list | Get a list of product tags


# **list_nomenclature_allergen_groups**
> AllergenGroupListResponse list_nomenclature_allergen_groups(allergen_group_list_request, timeout=timeout)

Get a list of allergen groups

Returns a list of allergen groups with filtering and pagination support.
Filter fields: `id`, `name`, `code`, `isDeleted`.
Allowed operators: `id` — eq, in; `name`, `code` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.allergen_group_list_request import AllergenGroupListRequest
from iikocloud_client.models.allergen_group_list_response import AllergenGroupListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    allergen_group_list_request = iikocloud_client.AllergenGroupListRequest() # AllergenGroupListRequest | Parameters for the allergen group list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of allergen groups
        api_response = await api_instance.list_nomenclature_allergen_groups(allergen_group_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_allergen_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_allergen_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allergen_group_list_request** | [**AllergenGroupListRequest**](AllergenGroupListRequest.md)| Parameters for the allergen group list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AllergenGroupListResponse**](AllergenGroupListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of allergen groups |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_amount_units**
> AmountUnitListResponse list_nomenclature_amount_units(amount_unit_list_request, timeout=timeout)

Get a list of amount units

Returns a list of amount units with filtering and pagination support.
Filter fields: `id`, `name`, `code`, `isDeleted`.
Allowed operators: `id` — eq, in; `name`, `code` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.amount_unit_list_request import AmountUnitListRequest
from iikocloud_client.models.amount_unit_list_response import AmountUnitListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    amount_unit_list_request = iikocloud_client.AmountUnitListRequest() # AmountUnitListRequest | Parameters for the amount unit list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of amount units
        api_response = await api_instance.list_nomenclature_amount_units(amount_unit_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_amount_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_amount_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount_unit_list_request** | [**AmountUnitListRequest**](AmountUnitListRequest.md)| Parameters for the amount unit list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AmountUnitListResponse**](AmountUnitListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of amount units |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_containers**
> ContainerListResponse list_nomenclature_containers(container_list_request, timeout=timeout)

Get a list of containers

Returns a list of containers with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.container_list_request import ContainerListRequest
from iikocloud_client.models.container_list_response import ContainerListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    container_list_request = iikocloud_client.ContainerListRequest() # ContainerListRequest | Parameters for the container list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of containers
        api_response = await api_instance.list_nomenclature_containers(container_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_containers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_containers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_list_request** | [**ContainerListRequest**](ContainerListRequest.md)| Parameters for the container list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ContainerListResponse**](ContainerListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of containers |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_custom_categories**
> CustomCategoryListResponse list_nomenclature_custom_categories(custom_category_list_request, timeout=timeout)

Get a list of custom categories

Returns a list of custom categories with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.custom_category_list_request import CustomCategoryListRequest
from iikocloud_client.models.custom_category_list_response import CustomCategoryListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    custom_category_list_request = iikocloud_client.CustomCategoryListRequest() # CustomCategoryListRequest | Parameters for the custom category list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of custom categories
        api_response = await api_instance.list_nomenclature_custom_categories(custom_category_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_custom_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_custom_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_category_list_request** | [**CustomCategoryListRequest**](CustomCategoryListRequest.md)| Parameters for the custom category list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CustomCategoryListResponse**](CustomCategoryListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of custom categories |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_menu_sections**
> MenuSectionListResponse list_nomenclature_menu_sections(menu_section_list_request, timeout=timeout)

Get a list of menu sections

Returns a list of menu sections with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.menu_section_list_request import MenuSectionListRequest
from iikocloud_client.models.menu_section_list_response import MenuSectionListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    menu_section_list_request = iikocloud_client.MenuSectionListRequest() # MenuSectionListRequest | Parameters for the menu section list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of menu sections
        api_response = await api_instance.list_nomenclature_menu_sections(menu_section_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_menu_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_menu_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **menu_section_list_request** | [**MenuSectionListRequest**](MenuSectionListRequest.md)| Parameters for the menu section list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**MenuSectionListResponse**](MenuSectionListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of menu sections |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_modifier_schemas**
> ModifierSchemaListResponse list_nomenclature_modifier_schemas(modifier_schema_list_request, timeout=timeout)

Get a list of modifier schemas

Returns a list of modifier schemas with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.modifier_schema_list_request import ModifierSchemaListRequest
from iikocloud_client.models.modifier_schema_list_response import ModifierSchemaListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    modifier_schema_list_request = iikocloud_client.ModifierSchemaListRequest() # ModifierSchemaListRequest | Parameters for the modifier schema list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of modifier schemas
        api_response = await api_instance.list_nomenclature_modifier_schemas(modifier_schema_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_modifier_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_modifier_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modifier_schema_list_request** | [**ModifierSchemaListRequest**](ModifierSchemaListRequest.md)| Parameters for the modifier schema list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ModifierSchemaListResponse**](ModifierSchemaListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of modifier schemas |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_place_types**
> PlaceTypeListResponse list_nomenclature_place_types(place_type_list_request, timeout=timeout)

Get a list of preparation place types

Returns a list of preparation place types with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.place_type_list_request import PlaceTypeListRequest
from iikocloud_client.models.place_type_list_response import PlaceTypeListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    place_type_list_request = iikocloud_client.PlaceTypeListRequest() # PlaceTypeListRequest | Parameters for the preparation place type list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of preparation place types
        api_response = await api_instance.list_nomenclature_place_types(place_type_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_place_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_place_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_type_list_request** | [**PlaceTypeListRequest**](PlaceTypeListRequest.md)| Parameters for the preparation place type list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**PlaceTypeListResponse**](PlaceTypeListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of preparation place types |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_producers**
> ProducerListResponse list_nomenclature_producers(producer_list_request, timeout=timeout)

Get a list of producers

Returns a list of producers with filtering and pagination support.
Filter fields: `id`, `name`, `code`, `isDeleted`.
Allowed operators: `id` — eq, in; `name`, `code` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.producer_list_request import ProducerListRequest
from iikocloud_client.models.producer_list_response import ProducerListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    producer_list_request = iikocloud_client.ProducerListRequest() # ProducerListRequest | Parameters for the producer list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of producers
        api_response = await api_instance.list_nomenclature_producers(producer_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_producers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_producers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **producer_list_request** | [**ProducerListRequest**](ProducerListRequest.md)| Parameters for the producer list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProducerListResponse**](ProducerListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of producers |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_product_sizes**
> ProductSizeListResponse list_nomenclature_product_sizes(product_size_list_request, timeout=timeout)

Get a list of product sizes

Returns a list of product sizes with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_size_list_request import ProductSizeListRequest
from iikocloud_client.models.product_size_list_response import ProductSizeListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    product_size_list_request = iikocloud_client.ProductSizeListRequest() # ProductSizeListRequest | Parameters for the product size list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of product sizes
        api_response = await api_instance.list_nomenclature_product_sizes(product_size_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_product_sizes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_product_sizes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_list_request** | [**ProductSizeListRequest**](ProductSizeListRequest.md)| Parameters for the product size list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductSizeListResponse**](ProductSizeListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product sizes |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_product_tags**
> ProductTagListResponse list_nomenclature_product_tags(product_tag_list_request, timeout=timeout)

Get a list of product tags

Returns a list of product tags with filtering and pagination support.
Filter fields: `id`, `name`, `isDeleted`.
Allowed operators: `id` — eq, in; `name` — eq, ne, in, nin, like, blank, notblank; `isDeleted` — eq (boolean).
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_tag_list_request import ProductTagListRequest
from iikocloud_client.models.product_tag_list_response import ProductTagListResponse
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
    api_instance = iikocloud_client.NomenclatureDirectoriesApi(api_client)
    product_tag_list_request = iikocloud_client.ProductTagListRequest() # ProductTagListRequest | Parameters for the product tag list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of product tags
        api_response = await api_instance.list_nomenclature_product_tags(product_tag_list_request, timeout=timeout)
        print("The response of NomenclatureDirectoriesApi->list_nomenclature_product_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureDirectoriesApi->list_nomenclature_product_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_tag_list_request** | [**ProductTagListRequest**](ProductTagListRequest.md)| Parameters for the product tag list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductTagListResponse**](ProductTagListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product tags |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

