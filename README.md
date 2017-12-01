[![Build Status](https://travis-ci.org/mplachter/yahoo-kafka-manager.svg?branch=master)](https://travis-ci.org/mplachter/yahoo-kafka-manager)

Yahoo-Kafka-Manager
=========

Ansible Role for building, deploying and configuring Yahoo Kafka Manager

* Build Yahoo Kafka Manager
  * Builds Yahoo Kafka Manager Locally
* Deploys Yahoo Kafka Manager
* Configures Yahoo Kafka Manager
* Creates `kafka-manager` service


* This is a ansible role to install and configure yahoo kafka manager
  * [Yahoo Kafka Manager](https://github.com/yahoo/kafka-manager)

Requirements
------------

* Running
  * Ansible 2.3
  * Java 1.8 JDK
  * Unzip
* Testing
  * Docker
  * Molecule 1.25.0

Role Variables
--------------

* Java `vars`
  ```
  java_heap_xms: 125
  java_heap_xmx: 250
  ```
* Kafka Manager `vars`
  ```
  kafka_manager_ver: '1.3.3.14'
  kafka_manager_mirror: https://github.com/yahoo/kafka-manager/archive
  ```
* Linux folder/path install `vars`
  ```
  download_path: /tmp
  installation_path: /usr/local
  owner: root
  group: root
  ```
* Kafka Manager configuration `vars`
  * Please consult Yahoo Kafka Manager [github](https://github.com/yahoo/kafka-manager) Page
  * Currently configuration will allow setting
    * Kafka Manager Features
    * Simple Auth
    * Changing Play Secret
    * Zookeeper Hosts
* Example variables

  ```
  ---
  # defaults file for kafka-manager

  # Kafka Manager Remote Download
  kafka_manager_ver: '1.3.3.14'
  kafka_manager_mirror: https://github.com/yahoo/kafka-manager/archive
  download_path: /tmp

  # Kafka Manager Install Defualt Settings
  installation_path: /usr/local
  listen_port: 8080

  # Linux Directory Permissions
  owner: root
  group: root

  kafka_manager_features:
    - KMClusterManagerFeature
    - KMTopicManagerFeature
    - KMPreferredReplicaElectionFeature
    - KMReassignPartitionsFeature

  kafka_manager_auth_enabled: false
  kafka_manager_auth_username: admin
  kafka_manager_auth_password: password
  kafka_manager_play_crypto_secret: /HeV^GoZV00N=ov8`IRL3:iTDX3[WNgS1hMMPl/3Y0[qfKCncDspHaNSYNyoB3XA
  kafka_manager_zookeeper_host:
    - name: 127.0.0.1
      port: 2181
  ```

Dependencies
------------

* role: andrewrothstein.java-oracle-jdk
  * version: v2.0.0

Example Playbook
----------------

    - hosts: all
      roles:
        - role: mplachter.kafka-manager

License
-------

MIT

Author Information
------------------

Matthew Plachter
