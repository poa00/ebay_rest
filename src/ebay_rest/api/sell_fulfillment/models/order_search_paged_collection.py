# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrderSearchPagedCollection(object):
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
        'orders': 'list[Order]',
        'prev': 'str',
        'total': 'int',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'orders': 'orders',
        'prev': 'prev',
        'total': 'total',
        'warnings': 'warnings'
    }

    def __init__(self, href=None, limit=None, next=None, offset=None, orders=None, prev=None, total=None, warnings=None):  # noqa: E501
        """OrderSearchPagedCollection - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._orders = None
        self._prev = None
        self._total = None
        self._warnings = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if orders is not None:
            self.orders = orders
        if prev is not None:
            self.prev = prev
        if total is not None:
            self.total = total
        if warnings is not None:
            self.warnings = warnings

    @property
    def href(self):
        """Gets the href of this OrderSearchPagedCollection.  # noqa: E501

        The URI of the <b>getOrders</b> call request that produced the current page of the result set.  # noqa: E501

        :return: The href of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this OrderSearchPagedCollection.

        The URI of the <b>getOrders</b> call request that produced the current page of the result set.  # noqa: E501

        :param href: The href of this OrderSearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this OrderSearchPagedCollection.  # noqa: E501

        The maximum number of orders returned per page of the result set. The <strong>limit</strong> value can be passed in as a query parameter, or if omitted, its value defaults to <code>50</code>. <br><br><span class=\"tablenote\"><strong>Note:</strong> If this is the last or only page of the result set, the page may contain fewer orders than the <strong>limit</strong> value.  To determine the number of pages in a result set, divide the <b>total</b> value (total number of orders matching input criteria) by this <strong>limit</strong> value, and then round up to the next integer. For example, if the <b>total</b> value was <code>120</code> (120 total orders) and the <strong>limit</strong> value was <code>50</code> (show 50 orders per page), the total number of pages in the result set is three, so the seller would have to make three separate <strong>getOrders</strong> calls to view all orders matching the input criteria. </span><b>Default:</b> <code>50</code>  # noqa: E501

        :return: The limit of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this OrderSearchPagedCollection.

        The maximum number of orders returned per page of the result set. The <strong>limit</strong> value can be passed in as a query parameter, or if omitted, its value defaults to <code>50</code>. <br><br><span class=\"tablenote\"><strong>Note:</strong> If this is the last or only page of the result set, the page may contain fewer orders than the <strong>limit</strong> value.  To determine the number of pages in a result set, divide the <b>total</b> value (total number of orders matching input criteria) by this <strong>limit</strong> value, and then round up to the next integer. For example, if the <b>total</b> value was <code>120</code> (120 total orders) and the <strong>limit</strong> value was <code>50</code> (show 50 orders per page), the total number of pages in the result set is three, so the seller would have to make three separate <strong>getOrders</strong> calls to view all orders matching the input criteria. </span><b>Default:</b> <code>50</code>  # noqa: E501

        :param limit: The limit of this OrderSearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this OrderSearchPagedCollection.  # noqa: E501

        The <b>getOrders</b> call URI to use if you wish to view the  next page of the result set. For example, the following URI returns records 41 thru 50 from the collection of orders: <br><br><code><i>path</i>/order?limit=10&offset=40 </code><br><br>This field is only returned if there is a next page of results to view based on the current input criteria.<br>  # noqa: E501

        :return: The next of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this OrderSearchPagedCollection.

        The <b>getOrders</b> call URI to use if you wish to view the  next page of the result set. For example, the following URI returns records 41 thru 50 from the collection of orders: <br><br><code><i>path</i>/order?limit=10&offset=40 </code><br><br>This field is only returned if there is a next page of results to view based on the current input criteria.<br>  # noqa: E501

        :param next: The next of this OrderSearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this OrderSearchPagedCollection.  # noqa: E501

        The number of results skipped in the result set before listing the first returned result. This value can be set in the request with the <b>offset</b> query parameter. <p class=\"tablenote\"><strong>Note: </strong>The items in a paginated result set use a zero-based list where the first item in the list has an offset of <code>0</code>.</p>  # noqa: E501

        :return: The offset of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this OrderSearchPagedCollection.

        The number of results skipped in the result set before listing the first returned result. This value can be set in the request with the <b>offset</b> query parameter. <p class=\"tablenote\"><strong>Note: </strong>The items in a paginated result set use a zero-based list where the first item in the list has an offset of <code>0</code>.</p>  # noqa: E501

        :param offset: The offset of this OrderSearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def orders(self):
        """Gets the orders of this OrderSearchPagedCollection.  # noqa: E501

        This array contains one or more orders that are part of the current result set, that is controlled by the input criteria. The details of each order include information about the buyer, order history, shipping fulfillments, line items, costs, payments, and order fulfillment status. <br><br>By default, orders are returned according to creation date (oldest to newest), but the order will vary according to any filter that is set in request.  # noqa: E501

        :return: The orders of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this OrderSearchPagedCollection.

        This array contains one or more orders that are part of the current result set, that is controlled by the input criteria. The details of each order include information about the buyer, order history, shipping fulfillments, line items, costs, payments, and order fulfillment status. <br><br>By default, orders are returned according to creation date (oldest to newest), but the order will vary according to any filter that is set in request.  # noqa: E501

        :param orders: The orders of this OrderSearchPagedCollection.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

    @property
    def prev(self):
        """Gets the prev of this OrderSearchPagedCollection.  # noqa: E501

        The <b>getOrders</b> call URI for the previous result set. For example, the following URI returns orders 21 thru 30 from the collection of orders: <br><br><code><i>path</i>/order?limit=10&offset=20</code><br><br>This field is only returned if there is a previous page of results to view based on the current input criteria.  # noqa: E501

        :return: The prev of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this OrderSearchPagedCollection.

        The <b>getOrders</b> call URI for the previous result set. For example, the following URI returns orders 21 thru 30 from the collection of orders: <br><br><code><i>path</i>/order?limit=10&offset=20</code><br><br>This field is only returned if there is a previous page of results to view based on the current input criteria.  # noqa: E501

        :param prev: The prev of this OrderSearchPagedCollection.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def total(self):
        """Gets the total of this OrderSearchPagedCollection.  # noqa: E501

        The total number of orders in the results set based on the current input criteria.<br><br><span class=\"tablenote\"><strong>Note:</strong> If no orders are found, this field is returned with a value of <code>0</code>.</span>  # noqa: E501

        :return: The total of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OrderSearchPagedCollection.

        The total number of orders in the results set based on the current input criteria.<br><br><span class=\"tablenote\"><strong>Note:</strong> If no orders are found, this field is returned with a value of <code>0</code>.</span>  # noqa: E501

        :param total: The total of this OrderSearchPagedCollection.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def warnings(self):
        """Gets the warnings of this OrderSearchPagedCollection.  # noqa: E501

        This array is returned if one or more errors or warnings occur with the call request.  # noqa: E501

        :return: The warnings of this OrderSearchPagedCollection.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this OrderSearchPagedCollection.

        This array is returned if one or more errors or warnings occur with the call request.  # noqa: E501

        :param warnings: The warnings of this OrderSearchPagedCollection.  # noqa: E501
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
        if issubclass(OrderSearchPagedCollection, dict):
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
        if not isinstance(other, OrderSearchPagedCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
