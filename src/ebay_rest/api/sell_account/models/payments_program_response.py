# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (the Fulfillment Policy, Payment Policy, and Return Policy), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentsProgramResponse(object):
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
        'marketplace_id': 'str',
        'payments_program_type': 'str',
        'status': 'str',
        'was_previously_opted_in': 'bool'
    }

    attribute_map = {
        'marketplace_id': 'marketplaceId',
        'payments_program_type': 'paymentsProgramType',
        'status': 'status',
        'was_previously_opted_in': 'wasPreviouslyOptedIn'
    }

    def __init__(self, marketplace_id=None, payments_program_type=None, status=None, was_previously_opted_in=None):  # noqa: E501
        """PaymentsProgramResponse - a model defined in Swagger"""  # noqa: E501
        self._marketplace_id = None
        self._payments_program_type = None
        self._status = None
        self._was_previously_opted_in = None
        self.discriminator = None
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if payments_program_type is not None:
            self.payments_program_type = payments_program_type
        if status is not None:
            self.status = status
        if was_previously_opted_in is not None:
            self.was_previously_opted_in = was_previously_opted_in

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this PaymentsProgramResponse.  # noqa: E501

        The ID of the eBay marketplace to which the payment policy applies. If this value is not specified in the request, the value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this PaymentsProgramResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this PaymentsProgramResponse.

        The ID of the eBay marketplace to which the payment policy applies. If this value is not specified in the request, the value defaults to the seller's eBay registration site. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this PaymentsProgramResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def payments_program_type(self):
        """Gets the payments_program_type of this PaymentsProgramResponse.  # noqa: E501

        This path parameter specifies the payment program whose status is returned by the call.  <br><br>Currently the only supported payments program is <code>EBAY_PAYMENTS</code>. For details on the program, see <a href=\"https://pages.ebay.com/payment/2.0/terms.html\" target=\"_blank\">Payments Terms of Use</a>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramType'>eBay API documentation</a>  # noqa: E501

        :return: The payments_program_type of this PaymentsProgramResponse.  # noqa: E501
        :rtype: str
        """
        return self._payments_program_type

    @payments_program_type.setter
    def payments_program_type(self, payments_program_type):
        """Sets the payments_program_type of this PaymentsProgramResponse.

        This path parameter specifies the payment program whose status is returned by the call.  <br><br>Currently the only supported payments program is <code>EBAY_PAYMENTS</code>. For details on the program, see <a href=\"https://pages.ebay.com/payment/2.0/terms.html\" target=\"_blank\">Payments Terms of Use</a>. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramType'>eBay API documentation</a>  # noqa: E501

        :param payments_program_type: The payments_program_type of this PaymentsProgramResponse.  # noqa: E501
        :type: str
        """

        self._payments_program_type = payments_program_type

    @property
    def status(self):
        """Gets the status of this PaymentsProgramResponse.  # noqa: E501

         For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramStatus'>eBay API documentation</a>  # noqa: E501

        :return: The status of this PaymentsProgramResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentsProgramResponse.

         For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramStatus'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this PaymentsProgramResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def was_previously_opted_in(self):
        """Gets the was_previously_opted_in of this PaymentsProgramResponse.  # noqa: E501

        If set to <code>true</code>, the seller was at one point opted-in to the associated payment program, but they later opted out of the program. A value of <code>false</code> indicates the seller never opted-in to the program or if they did opt-in to the program, they never opted-out of it.  <br><br>It's important to note that the setting of this field does not indicate the seller's current status regarding the payment program. It is possible for this field to return <code>true</code> while the <b>status</b> field returns <code>OPTED_IN</code>.  # noqa: E501

        :return: The was_previously_opted_in of this PaymentsProgramResponse.  # noqa: E501
        :rtype: bool
        """
        return self._was_previously_opted_in

    @was_previously_opted_in.setter
    def was_previously_opted_in(self, was_previously_opted_in):
        """Sets the was_previously_opted_in of this PaymentsProgramResponse.

        If set to <code>true</code>, the seller was at one point opted-in to the associated payment program, but they later opted out of the program. A value of <code>false</code> indicates the seller never opted-in to the program or if they did opt-in to the program, they never opted-out of it.  <br><br>It's important to note that the setting of this field does not indicate the seller's current status regarding the payment program. It is possible for this field to return <code>true</code> while the <b>status</b> field returns <code>OPTED_IN</code>.  # noqa: E501

        :param was_previously_opted_in: The was_previously_opted_in of this PaymentsProgramResponse.  # noqa: E501
        :type: bool
        """

        self._was_previously_opted_in = was_previously_opted_in

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
        if issubclass(PaymentsProgramResponse, dict):
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
        if not isinstance(other, PaymentsProgramResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
