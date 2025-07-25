# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iikocloud_client.models.transport_table_orders_request_create_table_order_request import TransportTableOrdersRequestCreateTableOrderRequest

class TestTransportTableOrdersRequestCreateTableOrderRequest(unittest.TestCase):
    """TransportTableOrdersRequestCreateTableOrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransportTableOrdersRequestCreateTableOrderRequest:
        """Test TransportTableOrdersRequestCreateTableOrderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransportTableOrdersRequestCreateTableOrderRequest`
        """
        model = TransportTableOrdersRequestCreateTableOrderRequest()
        if include_optional:
            return TransportTableOrdersRequestCreateTableOrderRequest(
                organization_id = '',
                terminal_group_id = '',
                order = iikocloud_client.models.request_table_order_schema.RequestTableOrderSchema(
                    id = '', 
                    external_number = '', 
                    table_ids = [
                        ''
                        ], 
                    customer = null, 
                    phone = '', 
                    guest_count = 56, 
                    guests = null, 
                    tab_name = '', 
                    menu_id = '', 
                    items = [
                        iikocloud_client.models.create_order_order_item_schema.CreateOrderOrderItemSchema(
                            type = '', 
                            amount = 0, 
                            product_size_id = '', 
                            combo_information = null, 
                            comment = '', )
                        ], 
                    combos = [
                        iikocloud_client.models.create_order_combo_schema.CreateOrderComboSchema(
                            id = '', 
                            name = '', 
                            amount = 56, 
                            price = 1.337, 
                            source_id = '', 
                            program_id = '', 
                            size_id = '', )
                        ], 
                    payments = [
                        iikocloud_client.models.create_order_payment_schema.CreateOrderPaymentSchema(
                            payment_type_kind = '', 
                            sum = 0, 
                            payment_type_id = '', 
                            is_processed_externally = True, 
                            payment_additional_data = null, 
                            is_fiscalized_externally = True, 
                            is_prepay = True, )
                        ], 
                    tips = [
                        iikocloud_client.models.create_order_tips_payment_schema.CreateOrderTipsPaymentSchema(
                            payment_type_kind = '', 
                            tips_type_id = '', 
                            sum = 0, 
                            payment_type_id = '', 
                            is_processed_externally = True, 
                            payment_additional_data = null, 
                            is_fiscalized_externally = True, 
                            is_prepay = True, )
                        ], 
                    source_key = '', 
                    discounts_info = null, 
                    loyalty_info = null, 
                    order_type_id = '', 
                    cheque_additional_info = null, 
                    external_data = [
                        iikocloud_client.models.create_order_external_data_schema.CreateOrderExternalDataSchema(
                            key = '', 
                            value = '', 
                            is_public = True, )
                        ], ),
                create_order_settings = iikocloud_client.models.request_create_table_order_settings_schema.RequestCreateTableOrderSettingsSchema(
                    service_print = False, 
                    transport_to_front_timeout = 56, 
                    check_stop_list = False, )
            )
        else:
            return TransportTableOrdersRequestCreateTableOrderRequest(
                organization_id = '',
                terminal_group_id = '',
        )
        """

    def testTransportTableOrdersRequestCreateTableOrderRequest(self):
        """Test TransportTableOrdersRequestCreateTableOrderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
