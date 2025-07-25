# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iikocloud_client.api.drafts_api import DraftsApi


class TestDraftsApi(unittest.IsolatedAsyncioTestCase):
    """DraftsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = DraftsApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_api1_deliveries_drafts_by_filter_post(self) -> None:
        """Test case for api1_deliveries_drafts_by_filter_post

        Retrieve order drafts list by parameters.
        """
        pass

    async def test_api1_deliveries_drafts_by_id_post(self) -> None:
        """Test case for api1_deliveries_drafts_by_id_post

        Retrieve order draft by ID.
        """
        pass

    async def test_api1_deliveries_drafts_commit_post(self) -> None:
        """Test case for api1_deliveries_drafts_commit_post

        Admit order draft changes and send them to Front.
        """
        pass

    async def test_api1_deliveries_drafts_create_post(self) -> None:
        """Test case for api1_deliveries_drafts_create_post

        Create delivery order draft.
        """
        pass

    async def test_api1_deliveries_drafts_delete_post(self) -> None:
        """Test case for api1_deliveries_drafts_delete_post

        Delete order draft.
        """
        pass

    async def test_api1_deliveries_drafts_lock_post(self) -> None:
        """Test case for api1_deliveries_drafts_lock_post

        Lock order draft.
        """
        pass

    async def test_api1_deliveries_drafts_save_post(self) -> None:
        """Test case for api1_deliveries_drafts_save_post

        Update existing delivery order draft.
        """
        pass

    async def test_api1_deliveries_drafts_unlock_post(self) -> None:
        """Test case for api1_deliveries_drafts_unlock_post

        Unlock order draft.
        """
        pass


if __name__ == '__main__':
    unittest.main()
