import sys
sys.path.append('\\synthetics\\modules\\behave-1.2.5')
#sys.path.append('\\synthetics\\modules\\behave')
sys.path.append('\\synthetics\\modules\\parse-1.8.4')
sys.path.append('\\synthetics\\modules\\selenium-3.13.0')
sys.path.append('\\synthetics\\modules\\parse_type-0.4.2')
sys.path.append('\\synthetics\\modules\\traceback2-1.4.0')
sys.path.append('\\synthetics\\modules\\linecache2-1.0.0')
sys.path.append('\\synthetics\\modules\\nose-1.3.7')
sys.path.append('\\synthetics\\modules\\six-1.11.0')
sys.path.append('\\synthetics\\modules\\enum-0.4.6')
sys.path.append('\\synthetics\\modules\\influxdb-5.1.0')

sys.path.append('\\synthetics\\modules\\requests-2.19.1')
sys.path.append('\\synthetics\\modules\\urllib3-1.23')
sys.path.append('\\synthetics\\modules\\chardet-3.0.4')
sys.path.append('\\synthetics\\modules\\certifi-2018.4.16')
sys.path.append('\\synthetics\\modules\\idna-2.7')
sys.path.append('\\synthetics\\modules\\pytz-2013.7')
sys.path.append('\\synthetics\\modules\\py-dateutil-2.2')





print sys.path

from behave.__main__ import main as behave_main

behave_main(["\\synthetics\\features", "-n NEAT"])
#behave_main(["\\synthetics\\features"])
#behave_main(["-n NEAT"])
