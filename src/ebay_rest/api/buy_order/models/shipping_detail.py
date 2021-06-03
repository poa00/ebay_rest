# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> This version of the Order API (v2) currently only supports the guest payment flow for eBay managed payments. To view the v1_beta version of the Order API, which includes both member and guest checkout payment flows, refer to the <a href=\"/api-docs/buy/order_v1/resources/methods\">Order_v1 API</a> documentation.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingDetail(object):
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
        'max_estimated_delivery_date': 'str',
        'min_estimated_delivery_date': 'str',
        'shipping_carrier_code': 'str',
        'shipping_service_code': 'str'
    }

    attribute_map = {
        'max_estimated_delivery_date': 'maxEstimatedDeliveryDate',
        'min_estimated_delivery_date': 'minEstimatedDeliveryDate',
        'shipping_carrier_code': 'shippingCarrierCode',
        'shipping_service_code': 'shippingServiceCode'
    }

    def __init__(self, max_estimated_delivery_date=None, min_estimated_delivery_date=None, shipping_carrier_code=None, shipping_service_code=None):  # noqa: E501
        """ShippingDetail - a model defined in Swagger"""  # noqa: E501
        self._max_estimated_delivery_date = None
        self._min_estimated_delivery_date = None
        self._shipping_carrier_code = None
        self._shipping_service_code = None
        self.discriminator = None
        if max_estimated_delivery_date is not None:
            self.max_estimated_delivery_date = max_estimated_delivery_date
        if min_estimated_delivery_date is not None:
            self.min_estimated_delivery_date = min_estimated_delivery_date
        if shipping_carrier_code is not None:
            self.shipping_carrier_code = shipping_carrier_code
        if shipping_service_code is not None:
            self.shipping_service_code = shipping_service_code

    @property
    def max_estimated_delivery_date(self):
        """Gets the max_estimated_delivery_date of this ShippingDetail.  # noqa: E501

        The end of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).  # noqa: E501

        :return: The max_estimated_delivery_date of this ShippingDetail.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_delivery_date

    @max_estimated_delivery_date.setter
    def max_estimated_delivery_date(self, max_estimated_delivery_date):
        """Sets the max_estimated_delivery_date of this ShippingDetail.

        The end of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).  # noqa: E501

        :param max_estimated_delivery_date: The max_estimated_delivery_date of this ShippingDetail.  # noqa: E501
        :type: str
        """

        self._max_estimated_delivery_date = max_estimated_delivery_date

    @property
    def min_estimated_delivery_date(self):
        """Gets the min_estimated_delivery_date of this ShippingDetail.  # noqa: E501

        The beginning of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).  # noqa: E501

        :return: The min_estimated_delivery_date of this ShippingDetail.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_delivery_date

    @min_estimated_delivery_date.setter
    def min_estimated_delivery_date(self, min_estimated_delivery_date):
        """Sets the min_estimated_delivery_date of this ShippingDetail.

        The beginning of the date range in which the purchase order is expected to be delivered to the shipping address (final destination).  # noqa: E501

        :param min_estimated_delivery_date: The min_estimated_delivery_date of this ShippingDetail.  # noqa: E501
        :type: str
        """

        self._min_estimated_delivery_date = min_estimated_delivery_date

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this ShippingDetail.  # noqa: E501

        The shipping provider for the line item, such as FedEx or USPS.  # noqa: E501

        :return: The shipping_carrier_code of this ShippingDetail.  # noqa: E501
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this ShippingDetail.

        The shipping provider for the line item, such as FedEx or USPS.  # noqa: E501

        :param shipping_carrier_code: The shipping_carrier_code of this ShippingDetail.  # noqa: E501
        :type: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def shipping_service_code(self):
        """Gets the shipping_service_code of this ShippingDetail.  # noqa: E501

        The name of the shipping service option. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).  # noqa: E501

        :return: The shipping_service_code of this ShippingDetail.  # noqa: E501
        :rtype: str
        """
        return self._shipping_service_code

    @shipping_service_code.setter
    def shipping_service_code(self, shipping_service_code):
        """Sets the shipping_service_code of this ShippingDetail.

        The name of the shipping service option. For example, Priority Mail Express (provided by USPS) or FedEx International Priority (Provided by FedEx).  # noqa: E501

        :param shipping_service_code: The shipping_service_code of this ShippingDetail.  # noqa: E501
        :type: str
        """

        self._shipping_service_code = shipping_service_code

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
        if issubclass(ShippingDetail, dict):
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
        if not isinstance(other, ShippingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
