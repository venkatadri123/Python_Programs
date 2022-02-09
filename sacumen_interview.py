# Write a program to calculate the total time taken by build process to complete.

# datetime [level] message
# 2020-11-30T09:43:49Z [error] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s
# '2020-11-30T09:41:34Z [info] Deploying the new build named as Connector as a service for the antivirus service with Instance Deployment complete.'

from datetime import datetime

log_list = [
  '2020-11-30T09:41:10Z [info] Success in plugin: success getting disk io info: open /proc/diskstats: no such file or CASS: directory',
  '2020-11-30T09:41:34Z [info] Deploying the new build named as Connector as a service for the antivirus service with Instance Deployment complete.',
  '2020-11-30T09:42:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:43:49Z [info] CASS: Instance Deployment started.',
  '2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s.',
  '2020-11-30T09:44:09Z [error] When writing to [http://localhost:8086]: Post "http://localhost:8086": dial tcp 127.0.0.1:8086: connect: connection refused',
  '2020-11-30T09:44:10Z [warning] Error in plugin: warning getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:44:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:45:10Z [info] CASS: Instance Deployment configured.',
  '2020-11-30T09:45:10Z [warning] Warning in plugin: error getting disk io info: open /proc/diskstats: no such file or directory.',
  '2020-11-30T09:45:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:47:10Z [info] Info in plugin: error getting disk io info: open /proc/diskstats: no such file or directory in Instance Deployment complete in progress',
  '2020-11-30T09:49:10Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:51:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:54:10Z [info] CASS: Instance Deployment complete.',
  '2020-11-30T09:54:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:55:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
  '2020-11-30T09:57:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory'
]

start_time = None
end_time = None

for val in log_list:
  if "CASS: Instance Deployment" in val:
    loop += 1
    d = val.split(' ')[0]
    if loop == 1:
      start_time = datetime.strptime(d, "%Y-%m-%dT%H:%M:%Sz")
      print("CASS: Instance Deployment started: ", start_time)
    else: 
      end_time = datetime.strptime(d, "%Y-%m-%dT%H:%M:%Sz")
      print(end_time - start_time)
 
