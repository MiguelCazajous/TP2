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
libName="libConverter.so"
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
        return responses


def loadLibrary():
    """
        Loads a 32 bits library in C language.
    """
    path=os.path.join(libPath, libName)
    libConverter = ctypes.CDLL(path)
    return libConverter


def processData(request, lib):
    requestStr = json.dumps(request)
    lib.parser.restype = ctypes.c_bool
    lib.parser.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
    ret = lib.parser(requestStr.encode(), len(requestStr))
    print(f'Return value: {ret}')


def main():
    """
        Main function.
    """
    jsonRequest = []
    jsonResponse = asyncio.run(apiRequestsList(getApiKey()))
    for item in jsonResponse:
        jsonItem = {}
        jsonItem["symbol"] = item[0]["symbol"]
        jsonItem["name"] = item[0]["name"]
        jsonItem["price"] = item[0]["price"]
        jsonRequest.append(jsonItem)
    processData(jsonRequest, loadLibrary())


if __name__ == "__main__":
    main()

