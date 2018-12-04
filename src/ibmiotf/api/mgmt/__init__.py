# *****************************************************************************
# Copyright (c) 2018 IBM Corporation and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
# *****************************************************************************

from ibmiotf.api.common import ApiClient 
from ibmiotf.api.registry.devices import Devices 
from ibmiotf.api.registry.types import DeviceTypes
from ibmiotf.api.mgmt.extensions import MgmtExtensions
from ibmiotf.api.mgmt.requests import MgmtRequests

class Mgmt():

    def __init__(self, apiClient):
        self._apiClient = apiClient
    
        self.requests = MgmtRequests(self._apiClient)
        self.extensions = MgmtExtensions(self._apiClient)
    
    
