#!/usr/bin/python
# coding: utf-8
# vim: ts=4: expandtab
import select
import pybonjour

# airPlay tcp host
regtype = "_airplay._tcp"

timeout = 3 
resolved = []
queried = []
resolvedHosts = []

# data model for airplay
class AirPlayDevice:
    def __init__(self, interfaceIndex, fullname, hosttarget, port):
        self.interfaceIndex = interfaceIndex
        self.fullname = fullname
        self.hosttarget = hosttarget
        self.port = port;
        self.displayname = hosttarget.replace(".local.", "")
        self.ip = 0


# It found a device
def resolve_callback(sdRef, flags, interfaceIndex, errorCode, fullname, hosttarget, port, txtRecord):
    for appleTv in resolvedHosts:
        # skip if there has two same address apple tv device.
        if appleTv.hosttarget == hosttarget:
            return
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        resolvedHosts.append(AirPlayDevice(interfaceIndex, fullname, hosttarget, port))
        resolved.append(True)


# Looking for devices
def browse_callback(sdRef, flags, interfaceIndex, errorCode, serviceName, regtype, replyDomain):
    if errorCode != pybonjour.kDNSServiceErr_NoError:
        return

    if not (flags & pybonjour.kDNSServiceFlagsAdd):
        return

    resolve_sdRef = pybonjour.DNSServiceResolve(0, interfaceIndex, serviceName, regtype, replyDomain, resolve_callback)

    try:
        while not resolved:
            ready = select.select([resolve_sdRef], [], [], timeout)
            if resolve_sdRef not in ready[0]:
                # print 'Resolve timed out'
                break

            pybonjour.DNSServiceProcessResult(resolve_sdRef)
        else:
            resolved.pop()

    finally:
        resolve_sdRef.close()

## starting workflow
browse_sdRef = pybonjour.DNSServiceBrowse(regtype=regtype, callBack=browse_callback)

try:
    try:
        ready = select.select([browse_sdRef], [], [])
        if browse_sdRef in ready[0]:
            pybonjour.DNSServiceProcessResult(browse_sdRef)
    except KeyboardInterrupt:
        pass
finally:
    browse_sdRef.close()

if len(resolvedHosts) > 1:
    for host in resolvedHosts:
        if host.displayname != "none":
            print host.displayname

quit()


