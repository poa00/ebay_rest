# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FormDataContentDisposition(object):
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
        'creation_date': 'str',
        'file_name': 'str',
        'modification_date': 'str',
        'name': 'str',
        'parameters': 'dict(str, str)',
        'read_date': 'str',
        'size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'file_name': 'fileName',
        'modification_date': 'modificationDate',
        'name': 'name',
        'parameters': 'parameters',
        'read_date': 'readDate',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, creation_date=None, file_name=None, modification_date=None, name=None, parameters=None, read_date=None, size=None, type=None):  # noqa: E501
        """FormDataContentDisposition - a model defined in Swagger"""  # noqa: E501
        self._creation_date = None
        self._file_name = None
        self._modification_date = None
        self._name = None
        self._parameters = None
        self._read_date = None
        self._size = None
        self._type = None
        self.discriminator = None
        if creation_date is not None:
            self.creation_date = creation_date
        if file_name is not None:
            self.file_name = file_name
        if modification_date is not None:
            self.modification_date = modification_date
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if read_date is not None:
            self.read_date = read_date
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def creation_date(self):
        """Gets the creation_date of this FormDataContentDisposition.  # noqa: E501

        The file creation date. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 8, 2019 2019-09-08T00:00:00.000Z  # noqa: E501

        :return: The creation_date of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FormDataContentDisposition.

        The file creation date. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 8, 2019 2019-09-08T00:00:00.000Z  # noqa: E501

        :param creation_date: The creation_date of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def file_name(self):
        """Gets the file_name of this FormDataContentDisposition.  # noqa: E501

        The name of the file including its extension (for example, xml or csv) to be uploaded.  # noqa: E501

        :return: The file_name of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FormDataContentDisposition.

        The name of the file including its extension (for example, xml or csv) to be uploaded.  # noqa: E501

        :param file_name: The file_name of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def modification_date(self):
        """Gets the modification_date of this FormDataContentDisposition.  # noqa: E501

        The file modified date. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 9, 2019 2019-09-09T00:00:00.000Z  # noqa: E501

        :return: The modification_date of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this FormDataContentDisposition.

        The file modified date. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 9, 2019 2019-09-09T00:00:00.000Z  # noqa: E501

        :param modification_date: The modification_date of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._modification_date = modification_date

    @property
    def name(self):
        """Gets the name of this FormDataContentDisposition.  # noqa: E501

        A content identifier. The only presently supported name is file.  # noqa: E501

        :return: The name of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormDataContentDisposition.

        A content identifier. The only presently supported name is file.  # noqa: E501

        :param name: The name of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this FormDataContentDisposition.  # noqa: E501

        The parameters you want associated with the file.  # noqa: E501

        :return: The parameters of this FormDataContentDisposition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this FormDataContentDisposition.

        The parameters you want associated with the file.  # noqa: E501

        :param parameters: The parameters of this FormDataContentDisposition.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def read_date(self):
        """Gets the read_date of this FormDataContentDisposition.  # noqa: E501

        The date you read the file. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 10, 2019 2019-09-10T00:00:00.000Z  # noqa: E501

        :return: The read_date of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._read_date

    @read_date.setter
    def read_date(self, read_date):
        """Sets the read_date of this FormDataContentDisposition.

        The date you read the file. Format: UTC yyyy-MM-ddThh:mm:ss.SSSZ For example: Created on September 10, 2019 2019-09-10T00:00:00.000Z  # noqa: E501

        :param read_date: The read_date of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._read_date = read_date

    @property
    def size(self):
        """Gets the size of this FormDataContentDisposition.  # noqa: E501

        The size of the file.  # noqa: E501

        :return: The size of this FormDataContentDisposition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FormDataContentDisposition.

        The size of the file.  # noqa: E501

        :param size: The size of this FormDataContentDisposition.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this FormDataContentDisposition.  # noqa: E501

        The file type. The only presently supported type is form-data.  # noqa: E501

        :return: The type of this FormDataContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormDataContentDisposition.

        The file type. The only presently supported type is form-data.  # noqa: E501

        :param type: The type of this FormDataContentDisposition.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(FormDataContentDisposition, dict):
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
        if not isinstance(other, FormDataContentDisposition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
