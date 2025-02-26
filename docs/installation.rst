============
Installation
============

Navground, CoppeliaSim, and navground_coppeliasim supports Linux, macOS and Windows.

Navground
=========

Follow the `documentation <https://idsia-robotics.github.io/navground/installation/index.html>`_ to install navground. This plugin does only depends on the navground_core and navground_sim C++ shared libraries.

You can install navground from source or install pre-build binaries.

Once installed, will need to source the environment to find navground

.. tabs::

   .. tab:: macOS

      .. code-block:: console

         $ . <navground_install>/setup.zsh

   .. tab:: Linux

      .. code-block:: console
         
         $ . <navground_install>install/setup.bash


   .. tab:: Windows

      .. code-block:: console
        
         $ <navground_install>install\setup.bat

where ``<navground_install>`` is the directory where you installed navground (e.g., ``/opt/navground/`` on Linux and macOS and ``C:\Program Files\navground`` in Windows).

CoppeliaSim
===========

Download and install `coppeliaSim <https://www.coppeliarobotics.com>`_ (versions 4.3--4.9 [latest]).

You then need to set ``COPPELIASIM_ROOT_DIR`` to the ``<path>`` of the directory containing the ``programming`` CoppeliaSim sub-directory.

.. tabs::

   .. tab:: macOS and Linux

      .. code-block:: console

         $ export COPPELIASIM_ROOT_DIR=<path>

   .. tab:: Windows

      .. code-block:: console
        
         $ set COPPELIASIM_ROOT_DIR=<path>

Navground-CoppeliaSim plugin
=============================

Using colcon
------------

Clone this repository in your workspace and run

.. code-block:: console

   colcon build --merge-install --cmake-args -DCMAKE_BUILD_TYPE=Release --packages-select navground_coppeliasim

Using cmake
------------

Clone this repository anywhere you like

.. tabs::

   .. tab:: macOS and Linux

      .. code-block:: console

         $ cmake -DCMAKE_BUILD_TYPE=Release <path to navground_coppeliasim>
         $ cmake --install .

   .. tab:: Windows

      .. code-block:: console
        
         $ cmake.exe <path to navground_coppeliasim>
         $ cmake.exe --install . --config Release

