# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentDisputeSummary(object):
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
        'amount': 'SimpleAmount',
        'buyer_username': 'str',
        'closed_date': 'str',
        'open_date': 'str',
        'order_id': 'str',
        'payment_dispute_id': 'str',
        'payment_dispute_status': 'str',
        'reason': 'str',
        'respond_by_date': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'buyer_username': 'buyerUsername',
        'closed_date': 'closedDate',
        'open_date': 'openDate',
        'order_id': 'orderId',
        'payment_dispute_id': 'paymentDisputeId',
        'payment_dispute_status': 'paymentDisputeStatus',
        'reason': 'reason',
        'respond_by_date': 'respondByDate'
    }

    def __init__(self, amount=None, buyer_username=None, closed_date=None, open_date=None, order_id=None, payment_dispute_id=None, payment_dispute_status=None, reason=None, respond_by_date=None):  # noqa: E501
        """PaymentDisputeSummary - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._buyer_username = None
        self._closed_date = None
        self._open_date = None
        self._order_id = None
        self._payment_dispute_id = None
        self._payment_dispute_status = None
        self._reason = None
        self._respond_by_date = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if buyer_username is not None:
            self.buyer_username = buyer_username
        if closed_date is not None:
            self.closed_date = closed_date
        if open_date is not None:
            self.open_date = open_date
        if order_id is not None:
            self.order_id = order_id
        if payment_dispute_id is not None:
            self.payment_dispute_id = payment_dispute_id
        if payment_dispute_status is not None:
            self.payment_dispute_status = payment_dispute_status
        if reason is not None:
            self.reason = reason
        if respond_by_date is not None:
            self.respond_by_date = respond_by_date

    @property
    def amount(self):
        """Gets the amount of this PaymentDisputeSummary.  # noqa: E501


        :return: The amount of this PaymentDisputeSummary.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentDisputeSummary.


        :param amount: The amount of this PaymentDisputeSummary.  # noqa: E501
        :type: SimpleAmount
        """

        self._amount = amount

    @property
    def buyer_username(self):
        """Gets the buyer_username of this PaymentDisputeSummary.  # noqa: E501

        This is the buyer's eBay user ID. This field is returned for all payment disputes returned in the response.  # noqa: E501

        :return: The buyer_username of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._buyer_username

    @buyer_username.setter
    def buyer_username(self, buyer_username):
        """Sets the buyer_username of this PaymentDisputeSummary.

        This is the buyer's eBay user ID. This field is returned for all payment disputes returned in the response.  # noqa: E501

        :param buyer_username: The buyer_username of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._buyer_username = buyer_username

    @property
    def closed_date(self):
        """Gets the closed_date of this PaymentDisputeSummary.  # noqa: E501

        The timestamp in this field shows the date/time when the payment dispute was closed, so this field is only returned for payment disputes in the <code>CLOSED</code> state.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The closed_date of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._closed_date

    @closed_date.setter
    def closed_date(self, closed_date):
        """Sets the closed_date of this PaymentDisputeSummary.

        The timestamp in this field shows the date/time when the payment dispute was closed, so this field is only returned for payment disputes in the <code>CLOSED</code> state.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param closed_date: The closed_date of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._closed_date = closed_date

    @property
    def open_date(self):
        """Gets the open_date of this PaymentDisputeSummary.  # noqa: E501

        The timestamp in this field shows the date/time when the payment dispute was opened. This field is returned for payment disputes in all states.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The open_date of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this PaymentDisputeSummary.

        The timestamp in this field shows the date/time when the payment dispute was opened. This field is returned for payment disputes in all states.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param open_date: The open_date of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._open_date = open_date

    @property
    def order_id(self):
        """Gets the order_id of this PaymentDisputeSummary.  # noqa: E501

        This is the unique identifier of the order involved in the payment dispute.  # noqa: E501

        :return: The order_id of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentDisputeSummary.

        This is the unique identifier of the order involved in the payment dispute.  # noqa: E501

        :param order_id: The order_id of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_dispute_id(self):
        """Gets the payment_dispute_id of this PaymentDisputeSummary.  # noqa: E501

        This is the unique identifier of the payment dispute. This identifier is automatically created by eBay once the payment dispute comes into the eBay system. This identifier is passed in at the end of the <strong>getPaymentDispute</strong> call URI to retrieve a specific payment dispute. The <strong>getPaymentDispute</strong> method returns more details about a payment dispute than the <strong>getPaymentDisputeSummaries</strong> method.  # noqa: E501

        :return: The payment_dispute_id of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._payment_dispute_id

    @payment_dispute_id.setter
    def payment_dispute_id(self, payment_dispute_id):
        """Sets the payment_dispute_id of this PaymentDisputeSummary.

        This is the unique identifier of the payment dispute. This identifier is automatically created by eBay once the payment dispute comes into the eBay system. This identifier is passed in at the end of the <strong>getPaymentDispute</strong> call URI to retrieve a specific payment dispute. The <strong>getPaymentDispute</strong> method returns more details about a payment dispute than the <strong>getPaymentDisputeSummaries</strong> method.  # noqa: E501

        :param payment_dispute_id: The payment_dispute_id of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._payment_dispute_id = payment_dispute_id

    @property
    def payment_dispute_status(self):
        """Gets the payment_dispute_status of this PaymentDisputeSummary.  # noqa: E501

        The enumeration value in this field gives the current status of the payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeStateEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_dispute_status of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._payment_dispute_status

    @payment_dispute_status.setter
    def payment_dispute_status(self, payment_dispute_status):
        """Sets the payment_dispute_status of this PaymentDisputeSummary.

        The enumeration value in this field gives the current status of the payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeStateEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_dispute_status: The payment_dispute_status of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._payment_dispute_status = payment_dispute_status

    @property
    def reason(self):
        """Gets the reason of this PaymentDisputeSummary.  # noqa: E501

        The enumeration value in this field gives the reason why the buyer initiated the payment dispute. See <strong>DisputeReasonEnum</strong> type for a description of the supported reasons that buyers can give for initiating a payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reason of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PaymentDisputeSummary.

        The enumeration value in this field gives the reason why the buyer initiated the payment dispute. See <strong>DisputeReasonEnum</strong> type for a description of the supported reasons that buyers can give for initiating a payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param reason: The reason of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def respond_by_date(self):
        """Gets the respond_by_date of this PaymentDisputeSummary.  # noqa: E501

        The timestamp in this field shows the date/time when the seller must response to a payment dispute, so this field is only returned for payment disputes in the <code>ACTION_NEEDED</code> state. For payment disputes that require action by the seller, that same seller must call <strong>getPaymentDispute</strong> to see the next action(s) that they can take against the payment dispute.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The respond_by_date of this PaymentDisputeSummary.  # noqa: E501
        :rtype: str
        """
        return self._respond_by_date

    @respond_by_date.setter
    def respond_by_date(self, respond_by_date):
        """Sets the respond_by_date of this PaymentDisputeSummary.

        The timestamp in this field shows the date/time when the seller must response to a payment dispute, so this field is only returned for payment disputes in the <code>ACTION_NEEDED</code> state. For payment disputes that require action by the seller, that same seller must call <strong>getPaymentDispute</strong> to see the next action(s) that they can take against the payment dispute.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param respond_by_date: The respond_by_date of this PaymentDisputeSummary.  # noqa: E501
        :type: str
        """

        self._respond_by_date = respond_by_date

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
        if issubclass(PaymentDisputeSummary, dict):
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
        if not isinstance(other, PaymentDisputeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
