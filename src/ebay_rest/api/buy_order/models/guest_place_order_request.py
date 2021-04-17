# coding: utf-8

"""
    Order API

    The Order API provides interfaces that let shoppers pay for items (for both eBay guest and eBay member buyers). It also returns payment and shipping status of the order. It enables eBay partners to use accept payment without being <a href=\"https://www.pcisecuritystandards.org/\">PCI compliant</a> and use the <a href=\"/api-docs/buy/static/api-order.html#Post\">Post Order API</a> for returns and cancellations for eBay member buyers.   <p>The Order API has the following resources:  </p>  <ul>  <li><b>checkout_session:</b> Lets eBay members purchase items using PayPal or a credit card.</li>  <li><b>guest_checkout_session:</b> Lets eBay guests purchase items using a credit card or the <a href=\"/api-docs/buy/static/api-order.html#spb-checkout\">PayPal Smart Button</a>.</li>   <li><b>proxy_guest_checkout_session:</b> Lets eBay guests purchase items through a <a href=\"/api-docs/buy/static/api-order.html#vsp-checkout\">vault service provider</a> (VSP). &nbsp;&nbsp;<b>*Note:* </b>Due to the requirement of having a VSP, this resource is not available in the eBay <a href=\"https://developer.ebay.com/my/api_test_tool?index=0\">API Explorer</a>.</li>  <li><b>guest_purchase_order</b> and <b>purchase_order:</b> Lets eBay partners track the payment status and show the buyers their purchase order. </li> </ul>  # noqa: E501

    OpenAPI spec version: v1_beta.29.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GuestPlaceOrderRequest(object):
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
        'marketing_terms': 'list[MarketingTerms]'
    }

    attribute_map = {
        'marketing_terms': 'marketingTerms'
    }

    def __init__(self, marketing_terms=None):  # noqa: E501
        """GuestPlaceOrderRequest - a model defined in Swagger"""  # noqa: E501
        self._marketing_terms = None
        self.discriminator = None
        if marketing_terms is not None:
            self.marketing_terms = marketing_terms

    @property
    def marketing_terms(self):
        """Gets the marketing_terms of this GuestPlaceOrderRequest.  # noqa: E501

        The container for the marketing channels, the types of messages the buyer can choose to receive and the field to indicate whether the buyer wants to receive marketing materials from eBay. These fields are required for all marketplaces. See Marketing Consent Notice for details.  # noqa: E501

        :return: The marketing_terms of this GuestPlaceOrderRequest.  # noqa: E501
        :rtype: list[MarketingTerms]
        """
        return self._marketing_terms

    @marketing_terms.setter
    def marketing_terms(self, marketing_terms):
        """Sets the marketing_terms of this GuestPlaceOrderRequest.

        The container for the marketing channels, the types of messages the buyer can choose to receive and the field to indicate whether the buyer wants to receive marketing materials from eBay. These fields are required for all marketplaces. See Marketing Consent Notice for details.  # noqa: E501

        :param marketing_terms: The marketing_terms of this GuestPlaceOrderRequest.  # noqa: E501
        :type: list[MarketingTerms]
        """

        self._marketing_terms = marketing_terms

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
        if issubclass(GuestPlaceOrderRequest, dict):
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
        if not isinstance(other, GuestPlaceOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
