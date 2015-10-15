# Ansible role for Celery

[![Build Status](https://travis-ci.org/torian/ansible-role-celery.svg)](https://travis-ci.org/torian/ansible-role-celery)

This role will install [celery](http://www.celeryproject.org/), a distributed
task queue. You can also install [Flower](http://flower.readthedocs.org/en/latest/),
a web based monitoring dashboard for celery clusters.

In order to daemonize Celery and/or Flower, `supervisor` is used.

## Tested On

  * Ubuntu 14.04

## Defaults

The `defaults/main.yml` should be pretty clear on the usage and values. The 
version used by defaults are:

  * `celery_version`: 3.1.18
  * `celery_flower_version`: 0.8.0
  * `celery_user`: nobody
  * `celery_group`: nogroup

## Usage

The tests in the respository should be pretty straight forward, but here are
some examples:

### Celery

This following will generate a supervisor configuration file in
`/etc/supervisor/conf.d` named `worker1`. The attributes of the
key `worker1` represent configuration params to supervisor, so 
you are free to specify the ones you need

```
- name: Install and run Celery
  hosts: localhost
  sudo: True

  vars:
    - supervisor_services: 
        worker1: 
          directory:    /path/to/celery/task
          process_name: celery_worker1
          num_procs:    1
          user:         "{{celery_user}}"
          command: |
            "celery -A tasks worker --loglevel=debug -f /tmp/worker1.log"
  
  roles:
    - { role: ansible-role-celery }

```

### Flower 

Running Flower is very similar:

```
- name: Install and run Celery
  hosts: localhost
  sudo: True

  vars:
    - celery_flower_service: 
        flower: 
          directory:    /path/to/celery/task
          process_name: celery_flower
          num_procs:    1
          user:         "{{celery_user}}"
          command: |
            "celery -A tasks --loglevel=debug -f /tmp/flower.log --broker=redis://localhost"
  
  roles:
    - { role: ansible-role-celery }

```

## TODO

  * Extract supervisor to it's own role
  * Extend to other distros

