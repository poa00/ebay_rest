# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the <a href=\"/api-docs/sell/static/marketing/pl-landing.html\">Promoted Listings playbook</a>.</li><li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p><p><b>Store Email Campaign</b> allows sellers to create and send email campaigns to customers who have signed up to receive their newsletter. For more information on email campaigns, see <a href=\"/api-docs/sell/static/marketing/store-email-campaigns.html#email-campain-types\" target=\"_blank\">Store Email Campaigns</a>.<p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.21.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TargetedAdsPagedCollection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'suggested_items': 'list[TargetingItems]',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'suggested_items': 'suggestedItems',
        'total': 'total'
    }

    def __init__(self, href=None, limit=None, next=None, offset=None, prev=None, suggested_items=None, total=None):  # noqa: E501
        """TargetedAdsPagedCollection - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._suggested_items = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if suggested_items is not None:
            self.suggested_items = suggested_items
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this TargetedAdsPagedCollection.  # noqa: E501

        The URI of the current page of results from the result set.  # noqa: E501

        :return: The href of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TargetedAdsPagedCollection.

        The URI of the current page of results from the result set.  # noqa: E501

        :param href: The href of this TargetedAdsPagedCollection.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this TargetedAdsPagedCollection.  # noqa: E501

        The number of items returned on a single page from the result set. This value can be set in the request with the <b>limit</b> query parameter.  # noqa: E501

        :return: The limit of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TargetedAdsPagedCollection.

        The number of items returned on a single page from the result set. This value can be set in the request with the <b>limit</b> query parameter.  # noqa: E501

        :param limit: The limit of this TargetedAdsPagedCollection.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this TargetedAdsPagedCollection.  # noqa: E501

        The call URI that can be used to retrieve the next page in the result set. This value is returned only if there is an additional page of results to display from the result set.  # noqa: E501

        :return: The next of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this TargetedAdsPagedCollection.

        The call URI that can be used to retrieve the next page in the result set. This value is returned only if there is an additional page of results to display from the result set.  # noqa: E501

        :param next: The next of this TargetedAdsPagedCollection.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this TargetedAdsPagedCollection.  # noqa: E501

        The number of results skipped in the result set before listing the first returned result. This value can be set in the request with the <b>offset</b> query parameter. <p><b>Default:</b> 0</p><br><span class=\"tablenote\"><b>Note: </b>The items in a paginated result set use a zero-based list, where the first item in the list has an offset of <code>0</code>.</span>  # noqa: E501

        :return: The offset of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TargetedAdsPagedCollection.

        The number of results skipped in the result set before listing the first returned result. This value can be set in the request with the <b>offset</b> query parameter. <p><b>Default:</b> 0</p><br><span class=\"tablenote\"><b>Note: </b>The items in a paginated result set use a zero-based list, where the first item in the list has an offset of <code>0</code>.</span>  # noqa: E501

        :param offset: The offset of this TargetedAdsPagedCollection.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this TargetedAdsPagedCollection.  # noqa: E501

        The call URI that can be used to retrieve the previous page in the result set. Basically, all of the request parameters will remain the same except the offset value, which will be decreased to retrieve the previous page of results.  # noqa: E501

        :return: The prev of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this TargetedAdsPagedCollection.

        The call URI that can be used to retrieve the previous page in the result set. Basically, all of the request parameters will remain the same except the offset value, which will be decreased to retrieve the previous page of results.  # noqa: E501

        :param prev: The prev of this TargetedAdsPagedCollection.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def suggested_items(self):
        """Gets the suggested_items of this TargetedAdsPagedCollection.  # noqa: E501

        A list of suggested items in the paginated collection.  # noqa: E501

        :return: The suggested_items of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: list[TargetingItems]
        """
        return self._suggested_items

    @suggested_items.setter
    def suggested_items(self, suggested_items):
        """Sets the suggested_items of this TargetedAdsPagedCollection.

        A list of suggested items in the paginated collection.  # noqa: E501

        :param suggested_items: The suggested_items of this TargetedAdsPagedCollection.  # noqa: E501
        :type: list[TargetingItems]
        """

        self._suggested_items = suggested_items

    @property
    def total(self):
        """Gets the total of this TargetedAdsPagedCollection.  # noqa: E501

        The total number of items retrieved in the result set.<br /><br /><span class=\"tablenote\"><b>Note: </b>If no items are found, this field is returned with a value of <code>0</code>.</span>  # noqa: E501

        :return: The total of this TargetedAdsPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TargetedAdsPagedCollection.

        The total number of items retrieved in the result set.<br /><br /><span class=\"tablenote\"><b>Note: </b>If no items are found, this field is returned with a value of <code>0</code>.</span>  # noqa: E501

        :param total: The total of this TargetedAdsPagedCollection.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TargetedAdsPagedCollection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TargetedAdsPagedCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
