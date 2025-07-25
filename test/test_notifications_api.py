# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iikocloud_client.api.notifications_api import NotificationsApi


class TestNotificationsApi(unittest.IsolatedAsyncioTestCase):
    """NotificationsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = NotificationsApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_api1_notifications_send_post(self) -> None:
        """Test case for api1_notifications_send_post

        Send notification to external systems (iikoFront and iikoWeb).
        """
        pass


if __name__ == '__main__':
    unittest.main()
