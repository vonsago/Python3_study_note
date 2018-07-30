#!/usr/bin/env python
# coding=utf-8
'''
> File Name: setup_broker.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  7/30 19:35:25 2018
'''
def setup_servicebroker(zone_id, broker_address):
    from app.broker.broker import add_broker, sync_broker, ServiceBroker
    from app.broker.adapter import init_adapter
    init_adapter()
    service_existed = False
    with sqlalchemy_session() as session:
        services = session.query(Service).filter().all()
        if services:
            service_existed = True
    LOG.info("init ServiceBroker start.")
    wait_broker_adapter_available('service_broker')

    with sqlalchemy_session() as session:
        brokers = broker_address.split(";")
        for i in range(len(brokers)):
            broker = add_broker(brokers[i], zone_id)
            wait_broker_available(broker)
            # only init first time
            if not service_existed:
                sync_broker(broker)
            LOG.info("init broker %s finish.", brokers[i])
