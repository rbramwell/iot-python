# *****************************************************************************
# Copyright (c) 2017 IBM Corporation and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Initial Contribution:
#   Ian Craggs
# *****************************************************************************


from __future__ import print_function
import time, ibmiotf.api, json, base64, traceback, sys, logging, importlib

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print("Property file name needed")
      sys.exit()

  property_file_name = sys.argv[1]

  logger.info("Getting properties from %s" % property_file_name)
  properties = importlib.import_module(property_file_name)
  property_names = dir(properties)

  verify = None
  params = {"auth-key": properties.key, "auth-token": properties.token}
  if "domain" in property_names:
    params["domain"] = properties.domain

  if "verify" in property_names:
    verify = properties.verify

  if "host" in property_names:
    params["host"] = properties.host

  api = ibmiotf.api.ApiClient(params)
  api.verify = verify

  while True:
    try:
      result = api.getLastEvents(properties.devicetype, properties.deviceid)
      """for event in result:
        if event["format"] == "json":
          event["payload"] = base64.decodestring(event["payload"])"""
      print("result", result)
    except Exception as exc:
      traceback.print_exc()
      print(exc)
    time.sleep(1)
