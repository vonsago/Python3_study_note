export LC_ALL=C.UTF-8
export LANG=C.UTF-8
apt-get -y update ;apt-get  install -y git
pip3 install pipenv ; pipenv --python 3.6 install  --dev 

mkdir -p /var/run/mysqld && chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
service mysql start
mysqladmin --silent --wait=30 ping || exit 1

export PYTHONPATH=`pwd`
pipenv run python3.6 app/unit_tests/mock_broker.py &
#wait for mock service start
sleep 30

pipenv run pytest
