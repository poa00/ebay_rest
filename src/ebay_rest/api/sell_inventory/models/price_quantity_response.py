# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PriceQuantityResponse(object):
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
        'errors': 'list[Error]',
        'offer_id': 'str',
        'sku': 'str',
        'status_code': 'int',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'errors': 'errors',
        'offer_id': 'offerId',
        'sku': 'sku',
        'status_code': 'statusCode',
        'warnings': 'warnings'
    }

    def __init__(self, errors=None, offer_id=None, sku=None, status_code=None, warnings=None):  # noqa: E501
        """PriceQuantityResponse - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._offer_id = None
        self._sku = None
        self._status_code = None
        self._warnings = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if offer_id is not None:
            self.offer_id = offer_id
        if sku is not None:
            self.sku = sku
        if status_code is not None:
            self.status_code = status_code
        if warnings is not None:
            self.warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this PriceQuantityResponse.  # noqa: E501

        This array will be returned if there were one or more errors associated with the update to the offer or inventory item record.  # noqa: E501

        :return: The errors of this PriceQuantityResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this PriceQuantityResponse.

        This array will be returned if there were one or more errors associated with the update to the offer or inventory item record.  # noqa: E501

        :param errors: The errors of this PriceQuantityResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def offer_id(self):
        """Gets the offer_id of this PriceQuantityResponse.  # noqa: E501

        The unique identifier of the offer that was updated. This field will not be returned in situations where the seller is only updating the total 'ship-to-home' quantity of an inventory item record.  # noqa: E501

        :return: The offer_id of this PriceQuantityResponse.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this PriceQuantityResponse.

        The unique identifier of the offer that was updated. This field will not be returned in situations where the seller is only updating the total 'ship-to-home' quantity of an inventory item record.  # noqa: E501

        :param offer_id: The offer_id of this PriceQuantityResponse.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def sku(self):
        """Gets the sku of this PriceQuantityResponse.  # noqa: E501

        This is the seller-defined SKU value of the product. This field is returned whether the seller attempted to update an offer with the SKU value or just attempted to update the total 'ship-to-home' quantity of an inventory item record.<br><br><strong>Max Length</strong>: 50<br>  # noqa: E501

        :return: The sku of this PriceQuantityResponse.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this PriceQuantityResponse.

        This is the seller-defined SKU value of the product. This field is returned whether the seller attempted to update an offer with the SKU value or just attempted to update the total 'ship-to-home' quantity of an inventory item record.<br><br><strong>Max Length</strong>: 50<br>  # noqa: E501

        :param sku: The sku of this PriceQuantityResponse.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def status_code(self):
        """Gets the status_code of this PriceQuantityResponse.  # noqa: E501

        The value returned in this container will indicate the status of the attempt to update the price and/or quantity of the offer (specified in the corresponding <strong>offerId</strong> field) or the attempt to update the total 'ship-to-home' quantity of an inventory item (specified in the corresponding <strong>sku</strong> field). For a completely successful update of an offer or inventory item record, a value of <code>200</code> will appear in this field.  A user can view the <strong>HTTP status codes</strong> section for information on other status codes that may be returned with the <strong>bulkUpdatePriceQuantity</strong> method.  # noqa: E501

        :return: The status_code of this PriceQuantityResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this PriceQuantityResponse.

        The value returned in this container will indicate the status of the attempt to update the price and/or quantity of the offer (specified in the corresponding <strong>offerId</strong> field) or the attempt to update the total 'ship-to-home' quantity of an inventory item (specified in the corresponding <strong>sku</strong> field). For a completely successful update of an offer or inventory item record, a value of <code>200</code> will appear in this field.  A user can view the <strong>HTTP status codes</strong> section for information on other status codes that may be returned with the <strong>bulkUpdatePriceQuantity</strong> method.  # noqa: E501

        :param status_code: The status_code of this PriceQuantityResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def warnings(self):
        """Gets the warnings of this PriceQuantityResponse.  # noqa: E501

        This array will be returned if there were one or more warnings associated with the update to the offer or inventory item record.  # noqa: E501

        :return: The warnings of this PriceQuantityResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this PriceQuantityResponse.

        This array will be returned if there were one or more warnings associated with the update to the offer or inventory item record.  # noqa: E501

        :param warnings: The warnings of this PriceQuantityResponse.  # noqa: E501
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
        if issubclass(PriceQuantityResponse, dict):
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
        if not isinstance(other, PriceQuantityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
