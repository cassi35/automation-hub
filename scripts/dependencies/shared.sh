#!/bin/bash
echo "Installing scraping dependencies..."
cd /packages/shared
uv add scrapy
uv add ipython
uv add  scrapy-rotating-proxies 
uv add scrapeops-scrapy-proxy-sdk
echo "Creating scraping project..."
scrapy startproject bookscraper
echo "instaling automation"
uv add selenium 