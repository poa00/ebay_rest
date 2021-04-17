# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExtendedContact(object):
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
        'company_name': 'str',
        'contact_address': 'Address',
        'email': 'str',
        'full_name': 'str',
        'primary_phone': 'PhoneNumber'
    }

    attribute_map = {
        'company_name': 'companyName',
        'contact_address': 'contactAddress',
        'email': 'email',
        'full_name': 'fullName',
        'primary_phone': 'primaryPhone'
    }

    def __init__(self, company_name=None, contact_address=None, email=None, full_name=None, primary_phone=None):  # noqa: E501
        """ExtendedContact - a model defined in Swagger"""  # noqa: E501
        self._company_name = None
        self._contact_address = None
        self._email = None
        self._full_name = None
        self._primary_phone = None
        self.discriminator = None
        if company_name is not None:
            self.company_name = company_name
        if contact_address is not None:
            self.contact_address = contact_address
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if primary_phone is not None:
            self.primary_phone = primary_phone

    @property
    def company_name(self):
        """Gets the company_name of this ExtendedContact.  # noqa: E501

        The company name associated with the buyer or eBay shipping partner. This field is only returned if defined/applicable to the buyer or eBay shipping partner.  # noqa: E501

        :return: The company_name of this ExtendedContact.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ExtendedContact.

        The company name associated with the buyer or eBay shipping partner. This field is only returned if defined/applicable to the buyer or eBay shipping partner.  # noqa: E501

        :param company_name: The company_name of this ExtendedContact.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_address(self):
        """Gets the contact_address of this ExtendedContact.  # noqa: E501


        :return: The contact_address of this ExtendedContact.  # noqa: E501
        :rtype: Address
        """
        return self._contact_address

    @contact_address.setter
    def contact_address(self, contact_address):
        """Sets the contact_address of this ExtendedContact.


        :param contact_address: The contact_address of this ExtendedContact.  # noqa: E501
        :type: Address
        """

        self._contact_address = contact_address

    @property
    def email(self):
        """Gets the email of this ExtendedContact.  # noqa: E501

        This field shows the email address of the buyer. The email address of a buyer will be masked 14 days after order creation. This field will still be returned for the order, but it will not contain the buyer's email address, but instead, something like 'Invalid Request'. Note: This field always contains the email address of the buyer even with a Global Shipping Program shipment.  # noqa: E501

        :return: The email of this ExtendedContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ExtendedContact.

        This field shows the email address of the buyer. The email address of a buyer will be masked 14 days after order creation. This field will still be returned for the order, but it will not contain the buyer's email address, but instead, something like 'Invalid Request'. Note: This field always contains the email address of the buyer even with a Global Shipping Program shipment.  # noqa: E501

        :param email: The email of this ExtendedContact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this ExtendedContact.  # noqa: E501

        The full name of the buyer or eBay shipping partner.  # noqa: E501

        :return: The full_name of this ExtendedContact.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ExtendedContact.

        The full name of the buyer or eBay shipping partner.  # noqa: E501

        :param full_name: The full_name of this ExtendedContact.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def primary_phone(self):
        """Gets the primary_phone of this ExtendedContact.  # noqa: E501


        :return: The primary_phone of this ExtendedContact.  # noqa: E501
        :rtype: PhoneNumber
        """
        return self._primary_phone

    @primary_phone.setter
    def primary_phone(self, primary_phone):
        """Sets the primary_phone of this ExtendedContact.


        :param primary_phone: The primary_phone of this ExtendedContact.  # noqa: E501
        :type: PhoneNumber
        """

        self._primary_phone = primary_phone

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
        if issubclass(ExtendedContact, dict):
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
        if not isinstance(other, ExtendedContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
