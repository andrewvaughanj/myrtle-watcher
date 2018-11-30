#!/bin/bash

openssl aes-256-cbc -md md5 -a -salt -in config.yml -out config.yml.enc

