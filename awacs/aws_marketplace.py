# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Marketplace Metering Service'
prefix = 'aws-marketplace'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchMeterUsage = Action('BatchMeterUsage')
MeterUsage = Action('MeterUsage')
RegisterUsage = Action('RegisterUsage')
ResolveCustomer = Action('ResolveCustomer')
RegisterUsage = Action('RegisterUsage')
Subscribe = Action('Subscribe')
Unsubscribe = Action('Unsubscribe')
ViewSubscriptions = Action('ViewSubscriptions')
