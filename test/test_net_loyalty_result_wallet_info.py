# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iikocloud_client.models.net_loyalty_result_wallet_info import NetLoyaltyResultWalletInfo

class TestNetLoyaltyResultWalletInfo(unittest.TestCase):
    """NetLoyaltyResultWalletInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetLoyaltyResultWalletInfo:
        """Test NetLoyaltyResultWalletInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetLoyaltyResultWalletInfo`
        """
        model = NetLoyaltyResultWalletInfo()
        if include_optional:
            return NetLoyaltyResultWalletInfo(
                id = '',
                max_sum = 1.337,
                can_hold_money = True
            )
        else:
            return NetLoyaltyResultWalletInfo(
        )
        """

    def testNetLoyaltyResultWalletInfo(self):
        """Test NetLoyaltyResultWalletInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
