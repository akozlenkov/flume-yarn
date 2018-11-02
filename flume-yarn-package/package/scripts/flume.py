#!/usr/bin/env python

import os
import shutil

from resource_management import *


class Flume(Script):
    def __init__(self):
        pass

    def install(self, env):
        self.install_packages(env)
        pass

    def configure(self, env):
        import params
        env.set_params(params)

        if (os.path.exists(params.app_conf_dir)):
            shutil.rmtree(params.app_conf_dir)

        Directory(params.app_conf_dir, owner=params.flume_user, group=params.flume_user_group, recursive=True)
        TemplateConfig(os.path.join(params.app_conf_dir, 'flume-env.sh'), owner=params.flume_user, group=params.flume_user_group, template_tag=None)

    def start(self, env):
        import params
        self.configure(env)

        cmd = '%s/bin/flume-ng agent --zkConnString %s --zkBasePath %s --name %s --conf %s --plugins-path %s -Dflume.root.logger=INFO,console >> %s 2>&1' % (os.path.join(params.app_root, params.app_name), params.flume_zookeeper_quorum, params.flume_zookeeper_znode, params.flume_agent, params.app_conf_dir, os.path.join(params.app_root, '../definition/package/plugins'), os.path.join(params.app_log_dir, 'flume.log'))

        Execute(cmd, user=params.flume_user, logoutput=True, wait_for_finish=False, pid_file=params.pid_file, poll_after=3)


    def stop(self, env):
        pass

    def status(self, env):
        import params
        env.set_params(params)

        check_process_status(params.pid_file)


if __name__ == "__main__":
    Flume().execute()
