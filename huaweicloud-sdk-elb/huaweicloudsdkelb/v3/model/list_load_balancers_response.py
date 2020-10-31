# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListLoadBalancersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'loadbalancers': 'list[LoadBalancer]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'loadbalancers': 'loadbalancers',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, loadbalancers=None, page_info=None, request_id=None):
        """ListLoadBalancersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._loadbalancers = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if loadbalancers is not None:
            self.loadbalancers = loadbalancers
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this ListLoadBalancersResponse.

        Loadbalancer的列表。

        :return: The loadbalancers of this ListLoadBalancersResponse.
        :rtype: list[LoadBalancer]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this ListLoadBalancersResponse.

        Loadbalancer的列表。

        :param loadbalancers: The loadbalancers of this ListLoadBalancersResponse.
        :type: list[LoadBalancer]
        """
        self._loadbalancers = loadbalancers

    @property
    def page_info(self):
        """Gets the page_info of this ListLoadBalancersResponse.


        :return: The page_info of this ListLoadBalancersResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListLoadBalancersResponse.


        :param page_info: The page_info of this ListLoadBalancersResponse.
        :type: PageInfo
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListLoadBalancersResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListLoadBalancersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListLoadBalancersResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListLoadBalancersResponse.
        :type: str
        """
        self._request_id = request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListLoadBalancersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
