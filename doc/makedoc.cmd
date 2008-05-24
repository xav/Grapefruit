@echo off
set builder=%1
if [%builder%]==[] set builder=html
set target=_build\%builder%
if not exist %target%\* md %target%
sphinx-build -b %builder% . _build\%builder%\
set target=
set builder=
