import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation=mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean(2*-std_deviation)=mean(2*+std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(2*std_deviation)=mean+(3*std_deviation)

fig=ff.create_distplot([data] 