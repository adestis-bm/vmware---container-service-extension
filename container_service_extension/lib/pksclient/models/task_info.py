# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TaskInfo(object):
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
        'uuid': 'str',
        'type': 'str',
        'status': 'str',
        'clusters': 'list[ClusterUpgradeInfo]',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'type': 'type',
        'status': 'status',
        'clusters': 'clusters',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, uuid=None, type=None, status=None, clusters=None, start_time=None, end_time=None):  # noqa: E501
        """TaskInfo - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._type = None
        self._status = None
        self._clusters = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if clusters is not None:
            self.clusters = clusters
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def uuid(self):
        """Gets the uuid of this TaskInfo.  # noqa: E501

        The uuid of a task  # noqa: E501

        :return: The uuid of this TaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TaskInfo.

        The uuid of a task  # noqa: E501

        :param uuid: The uuid of this TaskInfo.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this TaskInfo.  # noqa: E501

        The type of a task  # noqa: E501

        :return: The type of this TaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskInfo.

        The type of a task  # noqa: E501

        :param type: The type of this TaskInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UPGRADE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this TaskInfo.  # noqa: E501


        :return: The status of this TaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskInfo.


        :param status: The status of this TaskInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["not started", "in progress", "canceled", "done"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def clusters(self):
        """Gets the clusters of this TaskInfo.  # noqa: E501


        :return: The clusters of this TaskInfo.  # noqa: E501
        :rtype: list[ClusterUpgradeInfo]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this TaskInfo.


        :param clusters: The clusters of this TaskInfo.  # noqa: E501
        :type: list[ClusterUpgradeInfo]
        """

        self._clusters = clusters

    @property
    def start_time(self):
        """Gets the start_time of this TaskInfo.  # noqa: E501


        :return: The start_time of this TaskInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskInfo.


        :param start_time: The start_time of this TaskInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskInfo.  # noqa: E501


        :return: The end_time of this TaskInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskInfo.


        :param end_time: The end_time of this TaskInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

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
        if issubclass(TaskInfo, dict):
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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other