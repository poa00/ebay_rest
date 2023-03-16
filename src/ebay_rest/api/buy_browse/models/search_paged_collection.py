# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Resource\" title=\"Experimental Resource\" />&nbsp;(Experimental Resource)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.18.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SearchPagedCollection(object):
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
        'auto_corrections': 'AutoCorrections',
        'href': 'str',
        'item_summaries': 'list[ItemSummary]',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'refinement': 'Refinement',
        'total': 'int',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'auto_corrections': 'autoCorrections',
        'href': 'href',
        'item_summaries': 'itemSummaries',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'refinement': 'refinement',
        'total': 'total',
        'warnings': 'warnings'
    }

    def __init__(self, auto_corrections=None, href=None, item_summaries=None, limit=None, next=None, offset=None, prev=None, refinement=None, total=None, warnings=None):  # noqa: E501
        """SearchPagedCollection - a model defined in Swagger"""  # noqa: E501
        self._auto_corrections = None
        self._href = None
        self._item_summaries = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._refinement = None
        self._total = None
        self._warnings = None
        self.discriminator = None
        if auto_corrections is not None:
            self.auto_corrections = auto_corrections
        if href is not None:
            self.href = href
        if item_summaries is not None:
            self.item_summaries = item_summaries
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if refinement is not None:
            self.refinement = refinement
        if total is not None:
            self.total = total
        if warnings is not None:
            self.warnings = warnings

    @property
    def auto_corrections(self):
        """Gets the auto_corrections of this SearchPagedCollection.  # noqa: E501


        :return: The auto_corrections of this SearchPagedCollection.  # noqa: E501
        :rtype: AutoCorrections
        """
        return self._auto_corrections

    @auto_corrections.setter
    def auto_corrections(self, auto_corrections):
        """Sets the auto_corrections of this SearchPagedCollection.


        :param auto_corrections: The auto_corrections of this SearchPagedCollection.  # noqa: E501
        :type: AutoCorrections
        """

        self._auto_corrections = auto_corrections

    @property
    def href(self):
        """Gets the href of this SearchPagedCollection.  # noqa: E501

        The URI of the current page of results. <br><br>The following example of the <b> search</b> method returns items 1 thru 5 from the list of items found. <br><br><code>https://api.ebay.com/buy/v1/item_summary/search?q=shirt&limit=5&offset=0</code>.  # noqa: E501

        :return: The href of this SearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SearchPagedCollection.

        The URI of the current page of results. <br><br>The following example of the <b> search</b> method returns items 1 thru 5 from the list of items found. <br><br><code>https://api.ebay.com/buy/v1/item_summary/search?q=shirt&limit=5&offset=0</code>.  # noqa: E501

        :param href: The href of this SearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def item_summaries(self):
        """Gets the item_summaries of this SearchPagedCollection.  # noqa: E501

        An array of the items on this page. The items are sorted according to the sorting method specified in the request.  # noqa: E501

        :return: The item_summaries of this SearchPagedCollection.  # noqa: E501
        :rtype: list[ItemSummary]
        """
        return self._item_summaries

    @item_summaries.setter
    def item_summaries(self, item_summaries):
        """Sets the item_summaries of this SearchPagedCollection.

        An array of the items on this page. The items are sorted according to the sorting method specified in the request.  # noqa: E501

        :param item_summaries: The item_summaries of this SearchPagedCollection.  # noqa: E501
        :type: list[ItemSummary]
        """

        self._item_summaries = item_summaries

    @property
    def limit(self):
        """Gets the limit of this SearchPagedCollection.  # noqa: E501

        The value of the <b>limit</b> parameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method.  # noqa: E501

        :return: The limit of this SearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchPagedCollection.

        The value of the <b>limit</b> parameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method.  # noqa: E501

        :param limit: The limit of this SearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this SearchPagedCollection.  # noqa: E501

        The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set. <br><br>The following example of the <b> search</b> method returns items 5 thru 10 from the list of items found.<br> <br><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=10 </code>  # noqa: E501

        :return: The next of this SearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this SearchPagedCollection.

        The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set. <br><br>The following example of the <b> search</b> method returns items 5 thru 10 from the list of items found.<br> <br><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=10 </code>  # noqa: E501

        :param next: The next of this SearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this SearchPagedCollection.  # noqa: E501

        This value indicates the <b>offset</b> used for current page of items being returned. Assume the initial request used an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>3</code>. Then in the first page of results, this value would be <code>0</code>, and items 1-3 are returned. For the second page, this value is <code>3</code> and so on.  # noqa: E501

        :return: The offset of this SearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchPagedCollection.

        This value indicates the <b>offset</b> used for current page of items being returned. Assume the initial request used an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>3</code>. Then in the first page of results, this value would be <code>0</code>, and items 1-3 are returned. For the second page, this value is <code>3</code> and so on.  # noqa: E501

        :param offset: The offset of this SearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this SearchPagedCollection.  # noqa: E501

        The URI for the previous page of results. This is returned if there is a previous page of results from the result set. <br><br>The following example of the <b> search</b> method returns items 1 thru 5 from the list of items found, which would be the first set of items returned.<br> <br><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=0</code>  # noqa: E501

        :return: The prev of this SearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this SearchPagedCollection.

        The URI for the previous page of results. This is returned if there is a previous page of results from the result set. <br><br>The following example of the <b> search</b> method returns items 1 thru 5 from the list of items found, which would be the first set of items returned.<br> <br><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=0</code>  # noqa: E501

        :param prev: The prev of this SearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def refinement(self):
        """Gets the refinement of this SearchPagedCollection.  # noqa: E501


        :return: The refinement of this SearchPagedCollection.  # noqa: E501
        :rtype: Refinement
        """
        return self._refinement

    @refinement.setter
    def refinement(self, refinement):
        """Sets the refinement of this SearchPagedCollection.


        :param refinement: The refinement of this SearchPagedCollection.  # noqa: E501
        :type: Refinement
        """

        self._refinement = refinement

    @property
    def total(self):
        """Gets the total of this SearchPagedCollection.  # noqa: E501

        The total number of items that match the input criteria.  # noqa: E501

        :return: The total of this SearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchPagedCollection.

        The total number of items that match the input criteria.  # noqa: E501

        :param total: The total of this SearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def warnings(self):
        """Gets the warnings of this SearchPagedCollection.  # noqa: E501

        The container with all the warnings for the request.  # noqa: E501

        :return: The warnings of this SearchPagedCollection.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this SearchPagedCollection.

        The container with all the warnings for the request.  # noqa: E501

        :param warnings: The warnings of this SearchPagedCollection.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(SearchPagedCollection, dict):
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
        if not isinstance(other, SearchPagedCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
