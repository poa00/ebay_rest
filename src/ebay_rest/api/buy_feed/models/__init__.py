# coding: utf-8

# flake8: noqa
"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span><br><br>The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK \" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ...buy_feed.models.error import Error
from ...buy_feed.models.error_parameter import ErrorParameter
from ...buy_feed.models.item import Item
from ...buy_feed.models.item_group import ItemGroup
from ...buy_feed.models.item_group_response import ItemGroupResponse
from ...buy_feed.models.item_priority import ItemPriority
from ...buy_feed.models.item_priority_response import ItemPriorityResponse
from ...buy_feed.models.item_response import ItemResponse
from ...buy_feed.models.item_snapshot import ItemSnapshot
from ...buy_feed.models.item_snapshot_response import ItemSnapshotResponse
