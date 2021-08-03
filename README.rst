XKCD SimpleBot plugin
=====================

.. image:: https://img.shields.io/pypi/v/simplebot_xkcd.svg
   :target: https://pypi.org/project/simplebot_xkcd

.. image:: https://img.shields.io/pypi/pyversions/simplebot_xkcd.svg
   :target: https://pypi.org/project/simplebot_xkcd

.. image:: https://pepy.tech/badge/simplebot_xkcd
   :target: https://pepy.tech/project/simplebot_xkcd

.. image:: https://img.shields.io/pypi/l/simplebot_xkcd.svg
   :target: https://pypi.org/project/simplebot_xkcd

.. image:: https://github.com/simplebot-org/simplebot_xkcd/actions/workflows/python-ci.yml/badge.svg
   :target: https://github.com/simplebot-org/simplebot_xkcd/actions/workflows/python-ci.yml

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

A `SimpleBot`_ plugin that allows to request `XKCD <https://xkcd.com>`_ comics.

If this plugin has collisions with commands from other plugins in your bot, you can set a command prefix like ``/xkcd_`` for all commands::

  simplebot -a bot@example.com db simplebot_xkcd/command_prefix xkcd_

Install
-------

To install run::

  pip install simplebot-xkcd


.. _SimpleBot: https://github.com/simplebot-org/simplebot
