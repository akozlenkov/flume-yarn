#!/usr/bin/env python

from resource_management import *

config = Script.get_config()

java_home = config['hostLevelParams']['java_home']

app_root = config['configurations']['global']['app_root']
app_name = config['configurations']['global']['app_name']
app_log_dir = config['configurations']['global']['app_log_dir']
app_conf_dir = config['configurations']['global']['app_conf_dir']
pid_file = config['configurations']['global']['pid_file']

flume_user = default('/configurations/global/flume_user', 'flume')
flume_user_group = default('/configurations/global/flume_user_group', 'flume')
flume_agent = default('/configurations/global/flume_agent', 'a1')
flume_zookeeper_quorum = default('/configurations/global/flume_zookeeper_quorum', 'localhost:2181')
flume_zookeeper_znode = default('/configurations/global/flume_zookeeper_znode', '/flume')
flume_java_opts = default('/configurations/global/flume_java_opts', '-Xms100m -Xmx2000m -Dcom.sun.management.jmxremote')
