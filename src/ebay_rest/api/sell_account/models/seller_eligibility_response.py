# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellerEligibilityResponse(object):
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
        'program_type': 'str',
        'reason': 'str',
        'status': 'str'
    }

    attribute_map = {
        'program_type': 'programType',
        'reason': 'reason',
        'status': 'status'
    }

    def __init__(self, program_type=None, reason=None, status=None):  # noqa: E501
        """SellerEligibilityResponse - a model defined in Swagger"""  # noqa: E501
        self._program_type = None
        self._reason = None
        self._status = None
        self.discriminator = None
        if program_type is not None:
            self.program_type = program_type
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status

    @property
    def program_type(self):
        """Gets the program_type of this SellerEligibilityResponse.  # noqa: E501

        The eBay advertising program for which a seller may be eligible. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/plser:AdvertisingProgramEnum'>eBay API documentation</a>  # noqa: E501

        :return: The program_type of this SellerEligibilityResponse.  # noqa: E501
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """Sets the program_type of this SellerEligibilityResponse.

        The eBay advertising program for which a seller may be eligible. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/plser:AdvertisingProgramEnum'>eBay API documentation</a>  # noqa: E501

        :param program_type: The program_type of this SellerEligibilityResponse.  # noqa: E501
        :type: str
        """

        self._program_type = program_type

    @property
    def reason(self):
        """Gets the reason of this SellerEligibilityResponse.  # noqa: E501

        The reason why a seller is ineligible for the specified eBay advertising program.<br /><br />This field is only returned if the seller is ineligible for the eBay advertising program. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/plser:SellerIneligibleReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reason of this SellerEligibilityResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SellerEligibilityResponse.

        The reason why a seller is ineligible for the specified eBay advertising program.<br /><br />This field is only returned if the seller is ineligible for the eBay advertising program. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/plser:SellerIneligibleReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param reason: The reason of this SellerEligibilityResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this SellerEligibilityResponse.  # noqa: E501

        The seller elibibilty status for the specified eBay advertising program. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/cmlib:SellerEligibilityEnum'>eBay API documentation</a>  # noqa: E501

        :return: The status of this SellerEligibilityResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SellerEligibilityResponse.

        The seller elibibilty status for the specified eBay advertising program. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/cmlib:SellerEligibilityEnum'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this SellerEligibilityResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(SellerEligibilityResponse, dict):
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
        if not isinstance(other, SellerEligibilityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
