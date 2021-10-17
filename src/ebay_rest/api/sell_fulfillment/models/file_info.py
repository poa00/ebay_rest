# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileInfo(object):
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
        'file_id': 'str',
        'file_type': 'str',
        'name': 'str',
        'uploaded_date': 'str'
    }

    attribute_map = {
        'file_id': 'fileId',
        'file_type': 'fileType',
        'name': 'name',
        'uploaded_date': 'uploadedDate'
    }

    def __init__(self, file_id=None, file_type=None, name=None, uploaded_date=None):  # noqa: E501
        """FileInfo - a model defined in Swagger"""  # noqa: E501
        self._file_id = None
        self._file_type = None
        self._name = None
        self._uploaded_date = None
        self.discriminator = None
        if file_id is not None:
            self.file_id = file_id
        if file_type is not None:
            self.file_type = file_type
        if name is not None:
            self.name = name
        if uploaded_date is not None:
            self.uploaded_date = uploaded_date

    @property
    def file_id(self):
        """Gets the file_id of this FileInfo.  # noqa: E501

        The unique identifier of the evidence file.  # noqa: E501

        :return: The file_id of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileInfo.

        The unique identifier of the evidence file.  # noqa: E501

        :param file_id: The file_id of this FileInfo.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_type(self):
        """Gets the file_type of this FileInfo.  # noqa: E501

        The type of file uploaded. Supported file extensions are .JPEG, .JPG, and .PNG., and maximum file size allowed is 1.5 MB.  # noqa: E501

        :return: The file_type of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileInfo.

        The type of file uploaded. Supported file extensions are .JPEG, .JPG, and .PNG., and maximum file size allowed is 1.5 MB.  # noqa: E501

        :param file_type: The file_type of this FileInfo.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def name(self):
        """Gets the name of this FileInfo.  # noqa: E501

        The seller-provided name of the evidence file.  # noqa: E501

        :return: The name of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileInfo.

        The seller-provided name of the evidence file.  # noqa: E501

        :param name: The name of this FileInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uploaded_date(self):
        """Gets the uploaded_date of this FileInfo.  # noqa: E501

        The timestamp in this field shows the date/time when the seller uploaded the evidential document to eBay. <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The uploaded_date of this FileInfo.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_date

    @uploaded_date.setter
    def uploaded_date(self, uploaded_date):
        """Sets the uploaded_date of this FileInfo.

        The timestamp in this field shows the date/time when the seller uploaded the evidential document to eBay. <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param uploaded_date: The uploaded_date of this FileInfo.  # noqa: E501
        :type: str
        """

        self._uploaded_date = uploaded_date

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
        if issubclass(FileInfo, dict):
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
        if not isinstance(other, FileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
