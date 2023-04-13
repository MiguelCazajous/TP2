"""
Cryptocurrency conversor frontend.
"""
import ctypes
import os
import asyncio
import aiohttp
import json
import sys


libPath="lib"
libName="libHelloWorld.so"
apiUrlBase="https://financialmodelingprep.com/api/v3/quote/"
symbols = [
            "BTCUSD",
            "ETHUSD",
            "USDARS",
            "USDEUR"
          ]


def getApiKey():
    """
        Gets API key from a file.
    """
    try:
        with open("api_key", "r") as file:
            return file.read().replace('\n','')
    except IOError:
        print("Could not get API key")
        sys.exit(1)


async def getResponse(session, apiUrl, apiKey):
    """
        Performs the http request to the API.
    """
    params = {'apikey': apiKey}
    async with session.get(apiUrl, params=params) as response:
        response = await response.json()
        return response


async def apiRequestsList(apiKey):
    """
        Stores in a list all the required requests.
    """
    async with aiohttp.ClientSession() as session:
        requests=[]
        for symbol in symbols:
            apiUrl = apiUrlBase + symbol
            requests.append(asyncio.ensure_future(getResponse(session, apiUrl, apiKey)))

        responses = await asyncio.gather(*requests)
        print(responses)


def loadLibrary():
    """
        Loads a 32 bits library in C language.
    """
    path=os.path.join(libPath, libName)
    libHelloWorld = ctypes.CDLL(path)
    #libHelloWorld.helloWorld.argtypes = (ctypes.c_int,)
    #libHelloWorld.factorial.restype = ctypes.c_ulonglong
    libHelloWorld.hello_world()


def main():
    """
        Main function.
    """
    loadLibrary()
    asyncio.run(apiRequestsList(getApiKey()))


if __name__ == "__main__":
    main()

