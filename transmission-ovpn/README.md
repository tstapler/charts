# transmission-ovpn

This helm chart is for running [haugene's dockerized transmission + openvpn setup](https://github.com/haugene/docker-transmission-openvpn).


# Usage

To use this chart you'll need to configure the volumes which have a host path of `/data`.


# Changelog

## 1.0.0

Initial release after split from media-master chart

## 1.0.1

Helm chart fixes

## 1.1.0

Add a post-download script to unrar torrents that are rar'd
