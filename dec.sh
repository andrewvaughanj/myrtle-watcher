#!/bin/bash

openssl aes-256-cbc -d -a -md md5 -in config.yml.enc -out config.yml

