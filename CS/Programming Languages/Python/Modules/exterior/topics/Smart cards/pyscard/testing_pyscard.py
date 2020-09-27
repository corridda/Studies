"""pyscard user’s guide.

https://pyscard.sourceforge.io/user-guide.html#pyscard-user-guide
"""
from __future__ import print_function

from smartcard.sw.SWExceptions import CheckingErrorException, WarningProcessingException

import admstorage

__auther__ = 'Igor Vasilev'


"""The reader-centric approach"""
# from smartcard.System import readers
# from smartcard.util import toHexString, hl2bs
#
# r = readers()
# print(r)
#
# connection = r[0].createConnection()
# connection.connect()
#
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# SPN = [0x6F, 0x46]
# data, sw1, sw2 = connection.transmit( SELECT + SPN )
# print(f"{sw1} {sw2}")
# print(toHexString([sw1, sw2]))



"""The Answer To Reset (ATR)"""
# from smartcard.ATR import ATR
# from smartcard.util import toHexString, toBytes
#
# # atr = ATR([0x3B, 0x9E, 0x95, 0x80, 0x1F, 0xC3, 0x80, 0x31, 0xA0, 0x73,
# #            0xBE, 0x21, 0x13, 0x67, 0x29, 0x02, 0x01, 0x01, 0x81,
# #            0xCD, 0xB9])
#
# # atr = toBytes('3B9F96801FC78031E073FE211367980702040238017A')
# # atr = ATR(atr)
#
# atr = toBytes('3B9F96801FC68031E073FE211367933501020141013D')
# atr = ATR(atr)
#
# print(atr)
# print('historical bytes: ', toHexString(atr.getHistoricalBytes()))
# print('checksum: ', "0x%X" % atr.getChecksum())
# print('checksum OK: ', atr.checksumOK)
# print('T0  supported: ', atr.isT0Supported())
# print('T1  supported: ', atr.isT1Supported())
# print('T15 supported: ', atr.isT15Supported())



"""The card-centric approach"""

"""Requesting a card by ATR"""
# from smartcard.CardType import ATRCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString, toBytes
# from smartcard.Exceptions import CardRequestTimeoutException
#
# cardtypes = [ATRCardType(toBytes(atr)) for atr in admstorage._adm_apdu.keys()]
# print(cardtypes)
#
# for cardtype in cardtypes:
#     try:
#         cardrequest = CardRequest(timeout=1, cardType=cardtype)
#         cardservice = cardrequest.waitforcard()
#         cardservice.connection.connect()
#         print(toHexString(cardservice.connection.getATR()))
#         SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#         DF_TELECOM = [0x7F, 0x10]
#         data, sw1, sw2 = cardservice.connection.transmit(SELECT + DF_TELECOM)
#         print(f"{sw1} {sw2}")
#         print(toHexString([sw1, sw2]))
#     except CardRequestTimeoutException:
#         continue


"""Requesting any card"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# cardservice.connection.connect()
# print(toHexString(cardservice.connection.getATR(), format=1))   # 3B9F96801FC78031E073FE211367980702040238017A
# print(cardservice.connection.getReader())   # Athena ASEDrive IIIe USB 0


"""Custom CardTypes"""
# from smartcard.CardType import CardType
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString
# from smartcard.Exceptions import CardRequestTimeoutException
#
#
# class DCCardType(CardType):
#     def matches( self, atr, reader=None ):
#         return atr[0]==0x3B
#         # return atr[0]==0x3A
#
# try:
#     cardtype = DCCardType()
#     cardrequest = CardRequest( timeout=1, cardType=cardtype )
#     cardservice = cardrequest.waitforcard()
#     cardservice.connection.connect()
#     print(toHexString(cardservice.connection.getATR()))
#     print(cardservice.connection.getReader())
# except CardRequestTimeoutException:
#     print("Card wasn't found.")


"""Selecting the card communication protocol"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardConnection import CardConnection
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString
# from smartcard.Exceptions import CardConnectionException
#
# cardtype = AnyCardType()
# cardrequest = CardRequest(timeout=1, cardType=cardtype)
# cardservice = cardrequest.waitforcard()
#
# protocols = [CardConnection.T0_protocol, CardConnection.T1_protocol, CardConnection.T15_protocol]
#
# for protocol in protocols:
#     try:
#         cardservice.connection.connect(protocol)
#         print(toHexString(cardservice.connection.getATR()))
#         print(f'{cardservice.connection.getReader()}\n')
#     except CardConnectionException as e:
#         print(e.args[0])


# # Alternatively, you can specify the required protocol in the CardConnection transmit() method:
# from smartcard.CardType import AnyCardType
# from smartcard.CardConnection import CardConnection
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString, toBytes, HexListToBinString
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
# cardservice.connection.connect()
#
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# apdu = SELECT+DF_TELECOM
# print('sending ' + toHexString(apdu))
# response, sw1, sw2 = cardservice.connection.transmit( apdu, CardConnection.T0_protocol )
# print('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))
#
# if sw1 == 0x9F:
#     GET_RESPONSE = [0XA0, 0XC0, 00, 00]
#     apdu = GET_RESPONSE + [sw2]
#     print('sending ' + toHexString(apdu))
#     response, sw1, sw2 = cardservice.connection.transmit( apdu )
#     print('response: ', toHexString(response), ' status words: ', "%x %x" % (sw1, sw2))
#
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_GSM = [0x7F, 0x20]
# EF_SPN = [0x6F, 0x46]
#
# apdu = SELECT + DF_GSM
# print('sending ' + toHexString(apdu))
# response, sw1, sw2 = cardservice.connection.transmit(apdu, CardConnection.T0_protocol)
# print('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))
#
# if sw1 == 0x9F:
#     apdu = SELECT + EF_SPN
#     print('sending ' + toHexString(apdu))
#     response, sw1, sw2 = cardservice.connection.transmit(apdu, CardConnection.T0_protocol)
#     print(f'response: {response}, status words: {sw1:#x}, {sw2:#x}\n')
#
#     if sw1 == 0x9F:
#         READ_BINARY = [0xA0, 0xB0, 0x00, 0x00]
#         apdu = READ_BINARY + [sw2]
#         print('sending ' + toHexString(apdu))
#         response, sw1, sw2 = cardservice.connection.transmit(apdu, CardConnection.T0_protocol)
#         print(f'response: {response}, status words: {sw1:#0x}, {sw2:#0x}\n')
#         print(bytearray(response[1:]))



"""Tracing APDUs"""

"""The brute force"""
# from smartcard.CardType import ATRCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString, toBytes
# from smartcard.Exceptions import CardRequestTimeoutException
#
# cardtypes = [ATRCardType(toBytes(atr)) for atr in admstorage._adm_apdu.keys()]
# print(cardtypes)
#
# for cardtype in cardtypes:
#     try:
#         cardrequest = CardRequest(timeout=1, cardType=cardtype)
#         cardservice = cardrequest.waitforcard()
#         cardservice.connection.connect()
#
#         SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#         DF_TELECOM = [0x7F, 0x10]
#         apdu = SELECT + DF_TELECOM
#         print('sending ' + toHexString(apdu))
#         response, sw1, sw2 = cardservice.connection.transmit(apdu)
#         print(f'response: {response}, status words: {sw1:#0x}, {sw2:#0x}\n')
#
#         if sw1 == 0x9F:
#             GET_RESPONSE = [0XA0, 0XC0, 00, 00]
#             apdu = GET_RESPONSE + [sw2]
#             print('sending ' + toHexString(apdu))
#             response, sw1, sw2 = cardservice.connection.transmit(apdu)
#             print(f'response: {response}, status words: {sw1:#0x}, {sw2:#0x}\n')
#     except CardRequestTimeoutException:
#         continue

# # A small improvement in visibility would be to replace the print instructions by functions, e.g.:
# def trace_command(apdu):
#     print('sending ' + toHexString(apdu))
#
# def trace_response( response, sw1, sw2 ):
#     if response is None:
#         response=[]
#     print(f'response: {response}, status words: {sw1:#0x}, {sw2:#0x}\n')
#
# for cardtype in cardtypes:
#     try:
#         cardrequest = CardRequest(timeout=1, cardType=cardtype)
#         cardservice = cardrequest.waitforcard()
#         cardservice.connection.connect()
#
#         SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#         DF_TELECOM = [0x7F, 0x10]
#
#         apdu = SELECT + DF_TELECOM
#         print('sending ' + toHexString(apdu))
#         response, sw1, sw2 = cardservice.connection.transmit(apdu)
#         print(f'response: {response}, status words: {sw1:#0x}, {sw2:#0x}\n')
#
#         if sw1 == 0x9F:
#             GET_RESPONSE = [0XA0, 0XC0, 00, 00]
#             apdu = GET_RESPONSE + [sw2]
#             trace_command(apdu)
#             response, sw1, sw2 = cardservice.connection.transmit(apdu)
#             trace_response(response, sw1, sw2)
#     except CardRequestTimeoutException:
#         continue


"""Using card connection observers to trace apdu transmission"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# GET_RESPONSE = [0XA0, 0XC0, 00, 00 ]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=10, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# observer = ConsoleCardConnectionObserver()
# cardservice.connection.addObserver(observer)
#
# cardservice.connection.connect()
#
# apdu = SELECT + DF_TELECOM
# response, sw1, sw2 = cardservice.connection.transmit(apdu)
#
# if sw1 == 0x9F:
#     apdu = GET_RESPONSE + [sw2]
#     response, sw1, sw2 = cardservice.connection.transmit(apdu)
# else:
#     print('no DF_TELECOM')


"""Testing for APDU transmission errors"""
"""The brute force for testing APDU transmission errors"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# GET_RESPONSE = [0XA0, 0XC0, 00, 00 ]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# observer=ConsoleCardConnectionObserver()
# cardservice.connection.addObserver( observer )
#
# cardservice.connection.connect()
#
# apdu = SELECT + DF_TELECOM
# response, sw1, sw2 = cardservice.connection.transmit( apdu )
#
# if sw1 in range(0x61, 0x6f):
#     print(f"Error: sw1: {sw1:#0x} sw2: {sw2:#0x}")
#
# if sw1 == 0x9F:
#     apdu = GET_RESPONSE + [sw2]
#     response, sw1, sw2 = cardservice.connection.transmit( apdu )
#
# cardservice.connection.disconnect()


# # An improvement in visibility is to wrap the transmit instruction inside a function mytransmit, e.g.:
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# def mytransmit( connection, apdu ):
#     response, sw1, sw2 = connection.transmit( apdu )
#     if sw1 in range(0x61, 0x6f):
#         print(f"Error: sw1: {sw1:#0x} sw2: {sw2:#0x}")
#     return response, sw1, sw2
#
# GET_RESPONSE = [0XA0, 0XC0, 00, 00 ]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# observer=ConsoleCardConnectionObserver()
# cardservice.connection.addObserver( observer )
#
# cardservice.connection.connect()
#
# apdu = SELECT + DF_TELECOM
# response, sw1, sw2 = cardservice.connection.transmit( apdu )
#
#
# if sw1 == 0x9F:
#     apdu = GET_RESPONSE + [sw2]
#     response, sw1, sw2 = cardservice.connection.transmit( apdu )
#
# cardservice.connection.disconnect()


"""Checking APDU transmission errors with error checkers"""
"""Error checkers"""
# from smartcard.sw.ISO7816_4ErrorChecker import ISO7816_4ErrorChecker
#
# errorchecker=ISO7816_4ErrorChecker()
# errorchecker( [], 0x90, 0x00 )
# errorchecker( [], 0x6A, 0x80 )

# # Error checking chains
# from smartcard.sw.ISO7816_4ErrorChecker import ISO7816_4ErrorChecker
# from smartcard.sw.ISO7816_8ErrorChecker import ISO7816_8ErrorChecker
# from smartcard.sw.ISO7816_9ErrorChecker import ISO7816_9ErrorChecker
#
# from smartcard.sw.ErrorCheckingChain import ErrorCheckingChain
#
# errorchain = []
# errorchain = [
#     ErrorCheckingChain( errorchain, ISO7816_9ErrorChecker() ),
#     ErrorCheckingChain( errorchain, ISO7816_8ErrorChecker() ),
#     ErrorCheckingChain( errorchain, ISO7816_4ErrorChecker() ),
# ]
#
# for erch in errorchain:
#     print(erch)
# print()
#
# try:
#     errorchain[0]([], 0x90, 0x00)
#     errorchain[0]([], 0x6A, 0x8a)
# except CheckingErrorException as e:
#     print(repr(e))
#     print(tb.print_tb(e.__traceback__))


"""Filtering exceptions"""
# from smartcard.sw.ISO7816_4ErrorChecker import ISO7816_4ErrorChecker
# from smartcard.sw.ISO7816_8ErrorChecker import ISO7816_8ErrorChecker
# from smartcard.sw.ISO7816_9ErrorChecker import ISO7816_9ErrorChecker
#
# from smartcard.sw.ErrorCheckingChain import ErrorCheckingChain
#
# errorchain = []
# errorchain = [
#     ErrorCheckingChain( errorchain, ISO7816_9ErrorChecker() ),
#     ErrorCheckingChain( errorchain, ISO7816_8ErrorChecker() ),
#     ErrorCheckingChain( errorchain, ISO7816_4ErrorChecker() ),
# ]
#
# try:
#     errorchain[0]([], 0x90, 0x00)
#     errorchain[0]([], 0x62, 0x00)
# except WarningProcessingException as e:
#     print(f'{repr(e)}\n')
#
# errorchain[0].addFilterException( WarningProcessingException )
#
# try:
#     errorchain[0]([], 0x62, 0x00)
#     print('No exceptions occured.')
# except Exception:
#     print('Exception occured!')


"""Full sample code"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# from smartcard.sw.ErrorCheckingChain import ErrorCheckingChain
# from smartcard.sw.ISO7816_4ErrorChecker import ISO7816_4ErrorChecker
# from smartcard.sw.ISO7816_8ErrorChecker import ISO7816_8ErrorChecker
# from smartcard.sw.ISO7816_9ErrorChecker import ISO7816_9ErrorChecker
# from smartcard.sw.SWExceptions import SWException, WarningProcessingException
#
#
# # define the apdus used in this script
# GET_RESPONSE = [0XA0, 0XC0, 00, 00]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
#
# if __name__ == '__main__':
#
#     print('Insert a card within 10 seconds')
#     print('Cards without a DF_TELECOM will except')
#
#     # request any card type
#     cardtype = AnyCardType()
#     cardrequest = CardRequest(timeout=10, cardType=cardtype)
#     cardservice = cardrequest.waitforcard()
#
#     # use ISO7816-4 and ISO7816-8 and ISO7816-9 error checking strategy
#     # first check iso7816_9, then iso7816_8 errors, then iso7816_4 errors
#     errorchain = []
#     errorchain = [ErrorCheckingChain(errorchain, ISO7816_9ErrorChecker())]
#     errorchain = [ErrorCheckingChain(errorchain, ISO7816_8ErrorChecker())]
#     errorchain = [ErrorCheckingChain(errorchain, ISO7816_4ErrorChecker())]
#     cardservice.connection.setErrorCheckingChain(errorchain)
#
#     # filter Warning Processing Exceptions (sw1 = 0x62 or 0x63)
#     cardservice.connection.addSWExceptionToFilter(WarningProcessingException)
#
#     # attach the console tracer
#     observer = ConsoleCardConnectionObserver()
#     cardservice.connection.addObserver(observer)
#
#     # connect to the card and perform a few transmits
#     cardservice.connection.connect()
#
#     try:
#         apdu = SELECT + DF_TELECOM
#         response, sw1, sw2 = cardservice.connection.transmit(apdu)
#
#         if sw1 == 0x9F:
#             apdu = GET_RESPONSE + [sw2]
#             response, sw1, sw2 = cardservice.connection.transmit(apdu)
#     except SWException as e:
#         print(repr(e))
#
#     cardservice.connection.disconnect()


"""Detecting response APDU errors for a card connection"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# from smartcard.sw.ErrorCheckingChain import ErrorCheckingChain
# from smartcard.sw.ISO7816_4ErrorChecker import ISO7816_4ErrorChecker
# from smartcard.sw.ISO7816_8ErrorChecker import ISO7816_8ErrorChecker
# from smartcard.sw.SWExceptions import SWException, WarningProcessingException
#
# # request any card
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=10, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# # our error checking chain
# errorchain=[]
# errorchain=[
#     ErrorCheckingChain( errorchain, ISO7816_8ErrorChecker() ),
#     ErrorCheckingChain( errorchain, ISO7816_4ErrorChecker() ),
# ]
# cardservice.connection.setErrorCheckingChain( errorchain )
#
# # a console tracer
# observer=ConsoleCardConnectionObserver()
# cardservice.connection.addObserver( observer )
#
# # send a few apdus; exceptions will occur upon errors
# cardservice.connection.connect()
#
# try:
#     SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#     DF_TELECOM = [0x7F, 0x10]
#     apdu = SELECT+DF_TELECOM
#     response, sw1, sw2 = cardservice.connection.transmit( apdu )
#     if sw1 == 0x9F:
#         GET_RESPONSE = [0XA0, 0XC0, 00, 00 ]
#         apdu = GET_RESPONSE + [sw2]
#         response, sw1, sw2 = cardservice.connection.transmit( apdu )
# except SWException as e:
#     print(repr(e))


"""Writing a custom error checker"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#
# from smartcard.sw.ErrorCheckingChain import ErrorCheckingChain
# from smartcard.sw.ErrorChecker import ErrorChecker
# from smartcard.sw.SWExceptions import SWException
#
#
# class MyErrorChecker(ErrorChecker):
#     """Our custom error checker that will except if 0x61<sw1<0x70."""
#
#     def __call__(self, data, sw1, sw2):
#         print(sw1, sw2)
#         if 0x61 < sw1 and 0x70 > sw1:
#             raise SWException(data, sw1, sw2)
#
# # define the apdus used in this script
# GET_RESPONSE = [0XA0, 0XC0, 00, 00]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# if __name__ == '__main__':
#
#     print('Insert a card within 10 seconds')
#     print('Cards without a DF_TELECOM will except')
#
#     # request any card
#     cardtype = AnyCardType()
#     cardrequest = CardRequest(timeout=10, cardType=cardtype)
#     cardservice = cardrequest.waitforcard()
#
#     # our error checking chain
#     errorchain = [
#         ErrorCheckingChain([], MyErrorChecker()),
#     ]
#     cardservice.connection.setErrorCheckingChain(errorchain)
#
#     # attach the console tracer
#     observer = ConsoleCardConnectionObserver()
#     cardservice.connection.addObserver(observer)
#
#     # send a few apdus; exceptions will occur upon errors
#     cardservice.connection.connect()
#
#     try:
#         SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#         DF_TELECOM = [0x7F, 0x10]
#         apdu = SELECT + DF_TELECOM
#         response, sw1, sw2 = cardservice.connection.transmit(apdu)
#         if sw1 == 0x9F:
#             GET_RESPONSE = [0XA0, 0XC0, 00, 00]
#             apdu = GET_RESPONSE + [sw2]
#             response, sw1, sw2 = cardservice.connection.transmit(apdu)
#     except SWException as e:
#         print(e, "%x %x" % (e.sw1, e.sw2))
#
#     cardservice.connection.disconnect()



"""Smartcard readers"""

"""Listing Smartcard Readers"""
# import smartcard.System
# print(smartcard.System.readers())


# Organizing Smartcard Readers into reader groups
# import smartcard.System
# print(smartcard.System.readergroups())

# The readergroups() object has all the list attributes.
# from smartcard.System import readergroups
# g = readergroups()
# print(g)
# print(type(g))
#
# for i, readergroup in enumerate(g):
#     print(f'{i}: {readergroup}')
#
# g.append('Biometric$Readers')
# print(g)
#
# g.insert(1,'Pinpad$Readers')
# print(g)


"""Monitoring readers"""
# from time import sleep
#
# from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver
#
#
# class PrintObserver(ReaderObserver):
#     """A simple reader observer that is notified
#     when readers are added/removed from the system and
#     prints the list of readers
#     """
#
#     def update(self, observable, actions):
#         (addedreaders, removedreaders) = actions
#         print("Added readers", addedreaders)
#         print("Removed readers", removedreaders)
#
# if __name__ == '__main__':
#     print("Add or remove a smartcard reader to the system.")
#     print("This program will exit in 5 seconds")
#     print("")
#     readermonitor = ReaderMonitor()
#     readerobserver = PrintObserver()
#     readermonitor.addObserver(readerobserver)
#
#     sleep(5)
#
#     # don't forget to remove observer, or the
#     # monitor will poll forever...
#     readermonitor.deleteObserver(readerobserver)



"""Smart Cards"""

"""Monitoring Smart Cards"""
# from time import sleep
#
# from smartcard.CardMonitoring import CardMonitor, CardObserver
# from smartcard.util import toHexString
#
#
# # a simple card observer that prints inserted/removed cards
# class PrintObserver(CardObserver):
#     """A simple card observer that is notified
#     when cards are inserted/removed from the system and
#     prints the list of cards
#     """
#
#     def update(self, observable, actions):
#         (addedcards, removedcards) = actions
#         for card in addedcards:
#             print("+Inserted: ", toHexString(card.atr))
#         for card in removedcards:
#             print("-Removed: ", toHexString(card.atr))
#
# if __name__ == '__main__':
#     print("Insert or remove a smartcard in the system.")
#     print("This program will exit in 5 seconds")
#     print("")
#     cardmonitor = CardMonitor()
#     cardobserver = PrintObserver()
#     cardmonitor.addObserver(cardobserver)
#
#     sleep(5)
#
#     # don't forget to remove observer, or the
#     # monitor will poll forever...
#     cardmonitor.deleteObserver(cardobserver)



"""Connections"""

"""Creating a Connection from a CardRequest"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.util import toHexString
#
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# cardservice.connection.connect()
# print(toHexString(cardservice.connection.getATR()))
# print(cardservice.connection.getReader())

"""Creating Connection from CardMonitoring"""
# from time import sleep
#
# from smartcard.CardMonitoring import CardMonitor, CardObserver
# from smartcard.util import *
#
# # replace by your favourite apdu
# SELECT_DF_TELECOM = [0xA0, 0xA4, 0x00, 0x00, 0x02, 0x7F, 0x10]
#
#
# class TransmitObserver(CardObserver):
#     """A card observer that is notified when cards are inserted/removed
#     from the system, connects to cards and SELECT DF_TELECOM """
#
#     def __init__(self):
#         super().__init__()
#         self.cards = []
#
#     def update(self, observable, actions):
#         (addedcards, removedcards) = actions
#         for card in addedcards:
#             if card not in self.cards:
#                 self.cards += [card]
#                 print("+Inserted: ", toHexString(card.atr))
#                 card.connection = card.createConnection()
#                 card.connection.connect()
#                 response, sw1, sw2 = card.connection.transmit(
#                     SELECT_DF_TELECOM)
#                 print("%.2x %.2x" % (sw1, sw2))
#
#         for card in removedcards:
#             print("-Removed: ", toHexString(card.atr))
#             if card in self.cards:
#                 self.cards.remove(card)
#
# if __name__ == '__main__':
#     print("Insert or remove a smartcard in the system.")
#     print("This program will exit in 5 seconds")
#     print("")
#     cardmonitor = CardMonitor()
#     cardobserver = TransmitObserver()
#     cardmonitor.addObserver(cardobserver)
#
#     sleep(5)



"""Card Connection Decorators"""
# from smartcard.CardConnectionDecorator import CardConnectionDecorator
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
# from smartcard.util import toHexString
#
# class FakeATRConnection( CardConnectionDecorator ):
#     '''This decorator changes the fist byte of the ATR.'''
#     def __init__( self, cardconnection ):
#         CardConnectionDecorator.__init__( self, cardconnection )
#
#     def getATR( self ):
#         """Replace first BYTE of ATR by 3F"""
#         atr = CardConnectionDecorator.getATR( self )
#         return [ 0x3f ] + atr [1:]
#
# # request any card type
# cardtype = AnyCardType()
# cardrequest = CardRequest( timeout=1.5, cardType=cardtype )
# cardservice = cardrequest.waitforcard()
#
# # attach the console tracer
# observer=ConsoleCardConnectionObserver()
# cardservice.connection.addObserver( observer )
#
# # attach our decorator
# cardservice.connection = FakeATRConnection( cardservice.connection )
#
# # connect to the card and perform a few transmits
# cardservice.connection.connect()
#
# print('ATR', toHexString( cardservice.connection.getATR()))


"""Exclusive Card Connection Decorator"""
# from smartcard.CardType import AnyCardType
# from smartcard.CardRequest import CardRequest
# from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
# from smartcard.util import toHexString
#
# from smartcard.ExclusiveConnectCardConnection import \
#     ExclusiveConnectCardConnection
# from smartcard.ExclusiveTransmitCardConnection import \
#     ExclusiveTransmitCardConnection
#
#
# # define the apdus used in this script
# GET_RESPONSE = [0XA0, 0XC0, 00, 00]
# SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
# DF_TELECOM = [0x7F, 0x10]
#
# # request any card type
# cardtype = AnyCardType()
# cardrequest = CardRequest(timeout=5, cardType=cardtype)
# cardservice = cardrequest.waitforcard()
#
# # attach the console tracer
# observer = ConsoleCardConnectionObserver()
# cardservice.connection.addObserver(observer)
#
# # attach our decorator
# cardservice.connection = ExclusiveTransmitCardConnection(
#     ExclusiveConnectCardConnection(cardservice.connection))
#
# # connect to the card and perform a few transmits
# cardservice.connection.connect()
#
# print('ATR', toHexString(cardservice.connection.getATR()))
#
# try:
#     # lock for initiating transaction
#     cardservice.connection.lock()
#
#     apdu = SELECT + DF_TELECOM
#     response, sw1, sw2 = cardservice.connection.transmit(apdu)
#
#     if sw1 == 0x9F:
#         apdu = GET_RESPONSE + [sw2]
#         response, sw1, sw2 = cardservice.connection.transmit(apdu)
# finally:
#     # unlock connection at the end of the transaction
#     cardservice.connection.unlock()