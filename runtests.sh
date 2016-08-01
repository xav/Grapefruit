#! /bin/sh

nosetests-3.3 --verbosity=2 --with-doctest --with-coverage --cover-tests \
    --cover-package grapefruit \
    --cover-package grapefruit_test \
    $@
