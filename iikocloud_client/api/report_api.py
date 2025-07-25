# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from iikocloud_client.models.net_report_get_transactions_report_by_period_request import NetReportGetTransactionsReportByPeriodRequest
from iikocloud_client.models.net_report_get_transactions_report_by_period_response import NetReportGetTransactionsReportByPeriodResponse
from iikocloud_client.models.net_report_get_transactions_report_by_revision_request import NetReportGetTransactionsReportByRevisionRequest
from iikocloud_client.models.net_report_get_transactions_report_by_revision_response import NetReportGetTransactionsReportByRevisionResponse

from iikocloud_client.api_client import ApiClient, RequestSerialized
from iikocloud_client.api_response import ApiResponse
from iikocloud_client.rest import RESTResponseType


class ReportApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_date_post(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_period_request: Optional[NetReportGetTransactionsReportByPeriodRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> NetReportGetTransactionsReportByPeriodResponse:
        """Get transaction report by period.

        Get transaction report for specified customer by provided date range.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_period_request:
        :type net_report_get_transactions_report_by_period_request: NetReportGetTransactionsReportByPeriodRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_date_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByPeriodResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_date_post_with_http_info(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_period_request: Optional[NetReportGetTransactionsReportByPeriodRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[NetReportGetTransactionsReportByPeriodResponse]:
        """Get transaction report by period.

        Get transaction report for specified customer by provided date range.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_period_request:
        :type net_report_get_transactions_report_by_period_request: NetReportGetTransactionsReportByPeriodRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_date_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByPeriodResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_date_post_without_preload_content(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_period_request: Optional[NetReportGetTransactionsReportByPeriodRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get transaction report by period.

        Get transaction report for specified customer by provided date range.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_period_request:
        :type net_report_get_transactions_report_by_period_request: NetReportGetTransactionsReportByPeriodRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_date_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_period_request=net_report_get_transactions_report_by_period_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByPeriodResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api1_loyalty_iiko_customer_transactions_by_date_post_serialize(
        self,
        authorization,
        timeout,
        net_report_get_transactions_report_by_period_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if authorization is not None:
            _header_params['Authorization'] = authorization
        if timeout is not None:
            _header_params['Timeout'] = timeout
        # process the form parameters
        # process the body parameter
        if net_report_get_transactions_report_by_period_request is not None:
            _body_params = net_report_get_transactions_report_by_period_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/1/loyalty/iiko/customer/transactions/by_date',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_revision_post(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_revision_request: Optional[NetReportGetTransactionsReportByRevisionRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> NetReportGetTransactionsReportByRevisionResponse:
        """Get transaction report by revision.

        Get transaction report for specified customer by provided revision.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_revision_request:
        :type net_report_get_transactions_report_by_revision_request: NetReportGetTransactionsReportByRevisionRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_revision_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByRevisionResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_revision_post_with_http_info(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_revision_request: Optional[NetReportGetTransactionsReportByRevisionRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[NetReportGetTransactionsReportByRevisionResponse]:
        """Get transaction report by revision.

        Get transaction report for specified customer by provided revision.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_revision_request:
        :type net_report_get_transactions_report_by_revision_request: NetReportGetTransactionsReportByRevisionRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_revision_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByRevisionResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def api1_loyalty_iiko_customer_transactions_by_revision_post_without_preload_content(
        self,
        authorization: Annotated[StrictStr, Field(description="Authorization token.")],
        timeout: Annotated[Optional[StrictInt], Field(description="Timeout in seconds.")] = None,
        net_report_get_transactions_report_by_revision_request: Optional[NetReportGetTransactionsReportByRevisionRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get transaction report by revision.

        Get transaction report for specified customer by provided revision.   > Restriction group: `Guests: info`.

        :param authorization: Authorization token. (required)
        :type authorization: str
        :param timeout: Timeout in seconds.
        :type timeout: int
        :param net_report_get_transactions_report_by_revision_request:
        :type net_report_get_transactions_report_by_revision_request: NetReportGetTransactionsReportByRevisionRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api1_loyalty_iiko_customer_transactions_by_revision_post_serialize(
            authorization=authorization,
            timeout=timeout,
            net_report_get_transactions_report_by_revision_request=net_report_get_transactions_report_by_revision_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "NetReportGetTransactionsReportByRevisionResponse",
            '400': "TransportErrorsErrorResponse",
            '401': "TransportErrorsErrorResponse",
            '500': "TransportErrorsErrorResponse",
            '408': "TransportErrorsErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api1_loyalty_iiko_customer_transactions_by_revision_post_serialize(
        self,
        authorization,
        timeout,
        net_report_get_transactions_report_by_revision_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if authorization is not None:
            _header_params['Authorization'] = authorization
        if timeout is not None:
            _header_params['Timeout'] = timeout
        # process the form parameters
        # process the body parameter
        if net_report_get_transactions_report_by_revision_request is not None:
            _body_params = net_report_get_transactions_report_by_revision_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/1/loyalty/iiko/customer/transactions/by_revision',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


