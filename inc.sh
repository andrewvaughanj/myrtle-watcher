#!/bin/bash

openssl aes-256-cbc -a -salt -in config.yml -out config.yml.enc

