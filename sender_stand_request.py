import configuration
import requests
import data


def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)


def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))
