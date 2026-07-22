#!/bin/bash
echo "instaling ..."
cd apps 
npm create vite@latest
npm install orval -D
npm install @tanstack/react-query axios