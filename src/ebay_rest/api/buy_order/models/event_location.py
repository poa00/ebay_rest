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

class EventLocation(object):
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
        'city': 'str',
        'country': 'str',
        'county': 'str',
        'postal_code': 'str',
        'state_or_province': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country',
        'county': 'county',
        'postal_code': 'postalCode',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, city=None, country=None, county=None, postal_code=None, state_or_province=None):  # noqa: E501
        """EventLocation - a model defined in Swagger"""  # noqa: E501
        self._city = None
        self._country = None
        self._county = None
        self._postal_code = None
        self._state_or_province = None
        self.discriminator = None
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if county is not None:
            self.county = county
        if postal_code is not None:
            self.postal_code = postal_code
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def city(self):
        """Gets the city of this EventLocation.  # noqa: E501

        The city where the tracking event occurred.  # noqa: E501

        :return: The city of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EventLocation.

        The city where the tracking event occurred.  # noqa: E501

        :param city: The city of this EventLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this EventLocation.  # noqa: E501

        The two letter code representing the country of the address where the tracking event occurred. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this EventLocation.

        The two letter code representing the country of the address where the tracking event occurred. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country: The country of this EventLocation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this EventLocation.  # noqa: E501

        The county where the tracking event occurred.  # noqa: E501

        :return: The county of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this EventLocation.

        The county where the tracking event occurred.  # noqa: E501

        :param county: The county of this EventLocation.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def postal_code(self):
        """Gets the postal_code of this EventLocation.  # noqa: E501

        The postal code where the tracking event occurred.  # noqa: E501

        :return: The postal_code of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EventLocation.

        The postal code where the tracking event occurred.  # noqa: E501

        :param postal_code: The postal_code of this EventLocation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state_or_province(self):
        """Gets the state_or_province of this EventLocation.  # noqa: E501

        The state where the tracking event occurred.  # noqa: E501

        :return: The state_or_province of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this EventLocation.

        The state where the tracking event occurred.  # noqa: E501

        :param state_or_province: The state_or_province of this EventLocation.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

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
        if issubclass(EventLocation, dict):
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
        if not isinstance(other, EventLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other