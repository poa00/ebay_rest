# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AcceptPaymentDisputeRequest(object):
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
        'return_address': 'ReturnAddress',
        'revision': 'int'
    }

    attribute_map = {
        'return_address': 'returnAddress',
        'revision': 'revision'
    }

    def __init__(self, return_address=None, revision=None):  # noqa: E501
        """AcceptPaymentDisputeRequest - a model defined in Swagger"""  # noqa: E501
        self._return_address = None
        self._revision = None
        self.discriminator = None
        if return_address is not None:
            self.return_address = return_address
        if revision is not None:
            self.revision = revision

    @property
    def return_address(self):
        """Gets the return_address of this AcceptPaymentDisputeRequest.  # noqa: E501


        :return: The return_address of this AcceptPaymentDisputeRequest.  # noqa: E501
        :rtype: ReturnAddress
        """
        return self._return_address

    @return_address.setter
    def return_address(self, return_address):
        """Sets the return_address of this AcceptPaymentDisputeRequest.


        :param return_address: The return_address of this AcceptPaymentDisputeRequest.  # noqa: E501
        :type: ReturnAddress
        """

        self._return_address = return_address

    @property
    def revision(self):
        """Gets the revision of this AcceptPaymentDisputeRequest.  # noqa: E501

        This integer value indicates the revision number of the payment dispute. This field is required. The current revision number for a payment dispute can be retrieved with the getPaymentDispute method. Each time an action is taken against a payment dispute, this integer value increases by 1.  # noqa: E501

        :return: The revision of this AcceptPaymentDisputeRequest.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this AcceptPaymentDisputeRequest.

        This integer value indicates the revision number of the payment dispute. This field is required. The current revision number for a payment dispute can be retrieved with the getPaymentDispute method. Each time an action is taken against a payment dispute, this integer value increases by 1.  # noqa: E501

        :param revision: The revision of this AcceptPaymentDisputeRequest.  # noqa: E501
        :type: int
        """

        self._revision = revision

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
        if issubclass(AcceptPaymentDisputeRequest, dict):
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
        if not isinstance(other, AcceptPaymentDisputeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
