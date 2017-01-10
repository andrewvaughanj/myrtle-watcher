#!/bin/bash

openssl aes-256-cbc -d -a -in config.yml.enc -out config.yml

