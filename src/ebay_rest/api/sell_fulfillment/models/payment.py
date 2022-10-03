# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Payment(object):
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
        'amount': 'Amount',
        'payment_date': 'str',
        'payment_holds': 'list[PaymentHold]',
        'payment_method': 'str',
        'payment_reference_id': 'str',
        'payment_status': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'payment_date': 'paymentDate',
        'payment_holds': 'paymentHolds',
        'payment_method': 'paymentMethod',
        'payment_reference_id': 'paymentReferenceId',
        'payment_status': 'paymentStatus'
    }

    def __init__(self, amount=None, payment_date=None, payment_holds=None, payment_method=None, payment_reference_id=None, payment_status=None):  # noqa: E501
        """Payment - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._payment_date = None
        self._payment_holds = None
        self._payment_method = None
        self._payment_reference_id = None
        self._payment_status = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if payment_date is not None:
            self.payment_date = payment_date
        if payment_holds is not None:
            self.payment_holds = payment_holds
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_reference_id is not None:
            self.payment_reference_id = payment_reference_id
        if payment_status is not None:
            self.payment_status = payment_status

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501


        :return: The amount of this Payment.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def payment_date(self):
        """Gets the payment_date of this Payment.  # noqa: E501

        The date and time that the payment was received by the seller. This field will not be returned if buyer has yet to pay for the order. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The payment_date of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this Payment.

        The date and time that the payment was received by the seller. This field will not be returned if buyer has yet to pay for the order. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param payment_date: The payment_date of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_date = payment_date

    @property
    def payment_holds(self):
        """Gets the payment_holds of this Payment.  # noqa: E501

        This container is only returned if eBay is temporarily holding the seller's funds for the order. If a payment hold has been placed on the order, this container includes the reason for the payment hold, the expected release date of the funds into the seller's account, the current state of the hold, and as soon as the payment hold has been released, the actual release date.  # noqa: E501

        :return: The payment_holds of this Payment.  # noqa: E501
        :rtype: list[PaymentHold]
        """
        return self._payment_holds

    @payment_holds.setter
    def payment_holds(self, payment_holds):
        """Sets the payment_holds of this Payment.

        This container is only returned if eBay is temporarily holding the seller's funds for the order. If a payment hold has been placed on the order, this container includes the reason for the payment hold, the expected release date of the funds into the seller's account, the current state of the hold, and as soon as the payment hold has been released, the actual release date.  # noqa: E501

        :param payment_holds: The payment_holds of this Payment.  # noqa: E501
        :type: list[PaymentHold]
        """

        self._payment_holds = payment_holds

    @property
    def payment_method(self):
        """Gets the payment_method of this Payment.  # noqa: E501

        The payment method used to pay for the order. See the <strong>PaymentMethodTypeEnum</strong> type for more information on the payment methods. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_method of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Payment.

        The payment method used to pay for the order. See the <strong>PaymentMethodTypeEnum</strong> type for more information on the payment methods. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_method: The payment_method of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def payment_reference_id(self):
        """Gets the payment_reference_id of this Payment.  # noqa: E501

        This field is only returned if payment has been made by the buyer, and the <strong>paymentMethod</strong> is <code>ESCROW</code>. This field contains a special ID for ESCROW.  # noqa: E501

        :return: The payment_reference_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_reference_id

    @payment_reference_id.setter
    def payment_reference_id(self, payment_reference_id):
        """Sets the payment_reference_id of this Payment.

        This field is only returned if payment has been made by the buyer, and the <strong>paymentMethod</strong> is <code>ESCROW</code>. This field contains a special ID for ESCROW.  # noqa: E501

        :param payment_reference_id: The payment_reference_id of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_reference_id = payment_reference_id

    @property
    def payment_status(self):
        """Gets the payment_status of this Payment.  # noqa: E501

        The enumeration value returned in this field indicates the status of the payment for the order. See the <strong>PaymentStatusEnum</strong> type definition for more information on the possible payment states. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:PaymentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_status of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this Payment.

        The enumeration value returned in this field indicates the status of the payment for the order. See the <strong>PaymentStatusEnum</strong> type definition for more information on the possible payment states. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:PaymentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_status: The payment_status of this Payment.  # noqa: E501
        :type: str
        """

        self._payment_status = payment_status

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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
