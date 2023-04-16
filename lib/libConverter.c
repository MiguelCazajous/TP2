#include "json/json_object.h"
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include"definitions.h"
#include"json/json.h"

#define NO_NEG(X) (X >= 0.0 ? (X) : (0.0))

char BTCUSD[] = "BTCUSD";
char ETHUSD[] = "ETHUSD";
char USDARS[] = "USDARS";
char USDEUR[] = "USDEUR";
char BTCARS[] = "BTCARS";
char BTCEUR[] = "BTCEUR";
char ETHARS[] = "ETHARS";
char ETHEUR[] = "ETHEUR";

const char* converter(char *json_str, size_t json_str_size)  {
    json_object* json_obj = json_tokener_parse(json_str);
    if (NULL != json_obj && json_str_size > 0 && json_str_size < MAX_LENGTH) {
        double btc_usd = 0.0;
        double eth_usd = 0.0;
        double usd_ars = 0.0;
        double usd_eur = 0.0;

        double btc_ars = 0.0;
        double eth_ars = 0.0;
        double btc_eur = 0.0;
        double eth_eur = 0.0;

        json_object* json_response = json_object_new_array();

        for (int i = 0; i < json_object_array_length(json_obj); ++i) {
            json_object* json_item = json_object_array_get_idx(json_obj, i);
            json_object* symbol_str = json_object_object_get(json_item, "symbol");
            json_object* price_str = json_object_object_get(json_item, "price");

            if (strncmp(json_object_get_string(symbol_str), BTCUSD, strlen(BTCUSD)) == 0) {
                btc_usd = json_object_get_double(price_str);
                json_object* btc_usd_obj = json_object_new_object();
                json_object_object_add(btc_usd_obj, "symbol", symbol_str);
                json_object_object_add(btc_usd_obj, "price", json_object_new_double(NO_NEG(btc_usd)));
                json_object_array_add(json_response, btc_usd_obj);
            } else if (strncmp(json_object_get_string(symbol_str), ETHUSD, strlen(ETHUSD)) == 0) {
                eth_usd = json_object_get_double(price_str);
                json_object* eth_usd_obj = json_object_new_object();
                json_object_object_add(eth_usd_obj, "symbol", symbol_str);
                json_object_object_add(eth_usd_obj, "price", json_object_new_double(NO_NEG(eth_usd)));
                json_object_array_add(json_response, eth_usd_obj);
            } else if (strncmp(json_object_get_string(symbol_str), USDARS, strlen(USDARS)) == 0) {
                usd_ars = json_object_get_double(price_str);
            } else if (strncmp(json_object_get_string(symbol_str), USDEUR, strlen(USDEUR)) == 0) {
                usd_eur = json_object_get_double(price_str);
            }
        }
        btc_ars = product(btc_usd, usd_ars);
        btc_eur = product(btc_usd, usd_eur);
        eth_ars = product(eth_usd, usd_ars);
        eth_eur = product(eth_usd, usd_eur);

        json_object* btc_ars_obj = json_object_new_object();
        json_object* eth_ars_obj = json_object_new_object();

        json_object_object_add(btc_ars_obj, "symbol", json_object_new_string(BTCARS));
        json_object_object_add(btc_ars_obj, "price", json_object_new_double(NO_NEG(btc_ars)));
        json_object_object_add(eth_ars_obj, "symbol", json_object_new_string(ETHARS));
        json_object_object_add(eth_ars_obj, "price", json_object_new_double(NO_NEG(eth_ars)));

        json_object* btc_eur_obj = json_object_new_object();
        json_object* eth_eur_obj = json_object_new_object();

        json_object_object_add(btc_eur_obj, "symbol", json_object_new_string(BTCEUR));
        json_object_object_add(btc_eur_obj, "price", json_object_new_double(NO_NEG(btc_eur)));
        json_object_object_add(eth_eur_obj, "symbol", json_object_new_string(ETHEUR));
        json_object_object_add(eth_eur_obj, "price", json_object_new_double(NO_NEG(eth_eur)));

        json_object_array_add(json_response, btc_ars_obj);
        json_object_array_add(json_response, eth_ars_obj);
        json_object_array_add(json_response, btc_eur_obj);
        json_object_array_add(json_response, eth_eur_obj);

        return json_object_to_json_string(json_response);
    } else {
        return NULL;
    }
}

