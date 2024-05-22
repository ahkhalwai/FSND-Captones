#!/bin/bash
export AUTH0_DOMAIN = 'dev-aiehfurehuh6sbmf.us.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = '127.0.0.1:5000'
export DATABASE_URL="postgresql://postgres:8089@localhost:5432/fsnd"
export TEST_DATABASE_URL="postgresql://postgres@localhost:5432/fsndtest"
export TEST_TOKEN="Bearer "
export EXCITED="true"
echo "setup.sh script executed successfully!"
echo $DATABASE_URL
echo $TEST_DATABASE_URL
echo $EXCITED
export FLASK_APP=test_app.py
export FLASK_ENV=development
