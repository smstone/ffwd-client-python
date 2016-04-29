from ffwd import FFWD, Metric

f = FFWD()

disk_used_percentage = f.metric('system', what='disk-used-percentage')
disk_used_percentage.send(0.01)
