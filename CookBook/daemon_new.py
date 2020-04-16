#!/usr/bin/python

#================================================================
#   Copyright (C) 2020 Sangfor Ltd. All rights reserved.
#   
#   FileName: daemon_new.py
#   Author: Vassago
#   CreateTime: 2020-04-08
#   Email: vassago.von@gmail.com
#
#================================================================
import time
import sys
import os
import signal


def do_something():
    ...

class DaemonContext():
    def __init__(
            self,
            pidfile,
            stdin='/dev/null',
            stdout='/dev/null',
            stderr='/dev/null',
            chdir='/'
            ):
        self.pidfile = pidfile
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.chdir = chdir

    def open(self):
        if os.path.exists(self.pidfile):
            raise RuntimeError('Already running')
        # First fork (detaches from parent)
        try:
            if os.fork() > 0:
                raise SystemExit(0) # Parent exit
        except OSError as e:
            raise RuntimeError('fork #1 failed.')
        os.chdir(self.chdir)
        os.umask(self.umask)
        os.setsid()
        # Second fork (relinquish session leadership)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            raise RuntimeError('fork #2 failed.')
        # Flush I/O buffers
        sys.stdout.flush()
        sys.stderr.flush()
        self._replace_file_descriptors()
        # Arrange to have the PID file removed on exit/signal
        atexit.register(lambda: os.remove(pidfile))
        # Write the PID file
        with open(pidfile,'w') as f:
            print(os.getpid(),file=f)

        signal.signal(signal.SIGTERM, self._sigterm_handler)

    def close(self):
        if os.path.exists(self.pidfile):
            with open(self.pidfile) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            raise SystemExit(1)


    def _sigterm_handler(self, signo, frame):
        raise SystemExit(1)


    def _replace_file_descriptors(self):
        with open(stdin, 'rb', 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open(stdout, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open(stderr, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stderr.fileno())


    def __enter__(self):
        try:
            self.open()
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)
        return self

    def __exit__(self):
        self.close()


if __name__ == '__main__':
    ...
