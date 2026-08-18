import numpy as np
import os
import csv
from pathlib import Path

curpath = os.path.dirname(os.path.abspath(__file__))
row_count = 9
col_count = 7
spring_count = (row_count-1)*col_count + row_count*(col_count-1)

def writeks(spring_count):
  write_to_stiffness_file_text = list()
  write_to_stiffness_file_text.append("echo $Input1$>$stiffness_file.txt$")
  for i in range(1,spring_count):
    write_to_stiffness_file_text.append("echo $Input{}$>>$stiffness_file.txt$".format(i+1))

  with open("utilFiles/write_to_stiffness_file.txt", "w") as fo:
    for line in write_to_stiffness_file_text:
      fo.writelines(line+"\n")

def writeds(spring_count):
  write_to_distances_file_text = list()
  write_to_distances_file_text.append("echo $Input111$>$dist_file.txt$")
  for i in range(111,spring_count*2):
    write_to_distances_file_text.append("echo $Input{}$>>$dist_file.txt$".format(i+1))

  with open("utilFiles/write_to_distances_file.txt", "w") as fo:
    for line in write_to_distances_file_text:
      fo.writelines(line+"\n")

def write_stretch_pos(islandID, row_count, col_count):
  pos_list = list()
  count = 1
  for i in range(row_count):
    for j in range(col_count):
      pos_list.append(("x_island_{}".format(count),",",str(islandID[i,j]["str_mm"][0]), ",","y_island_{}".format(count),",", str(-islandID[i,j]["str_mm"][1]),"\n"))
      count += 1
  
  # with open('parameterFiles/stretchedpos.csv', "w") as fo: #The output is like (x_island, 0, y_island, 0\n, x_island...). Useful for CSV format.
  #   for line in pos_list:
  #     fo.writelines(line)

  # with open('parameterFiles/stretchedpos_oneline_x.txt', "w") as fo: #The output is like (0, 32, 44). Useful if we'd like to define vector in Matlab
  #   for line in pos_list:
  #     fo.write(line[2]+ ", ")
  
  # with open('parameterFiles/stretchedpos_oneline_y.txt', "w") as fo: #The output is like (0, 32, 44). Useful if we'd like to define vector in Matlab
  #   for line in pos_list:
  #     fo.write(line[6]+ ", ")
  
  with open('parameterFiles/stretchedpos_onecolumn_x.txt', "w") as fo: #The output is like (0\n, 32\n, ...). Useful if we'd like to define a vector as file in Optimus.
    for line in pos_list:
      fo.writelines(line[2]+"\n")

  with open('parameterFiles/stretchedpos_onecolumn_y.txt', "w") as fo: #The output is like (0\n, 32\n, ...). Useful if we'd like to define a vector as file in Optimus.
    for line in pos_list:
      fo.writelines(line[6]+"\n")

def write_stretch_pos_optimus(axis, islandID, row_count, col_count):
  pos_list = list()
  count = 1
  for i in range(row_count):
    for j in range(col_count):
      pos_list.append(("x_island_{}".format(count),",",str(islandID[i,j]["str_mm"][0]), ",","y_island_{}".format(count),",", str(-islandID[i,j]["str_mm"][1]),"\n"))
      count += 1
  
  if axis == 'x':
    with open('stretchedpos_onecolumn_x.txt', "w") as fo: #The output is like (0\n, 32\n, ...). Useful if we'd like to define a vector as file in Optimus.
      for line in pos_list:
        fo.writelines(line[2]+"\n")
  elif axis == 'y':
    with open('stretchedpos_onecolumn_y.txt', "w") as fo: #The output is like (0\n, 32\n, ...). Useful if we'd like to define a vector as file in Optimus.
      for line in pos_list:
        fo.writelines(line[6]+"\n")

def write_interconnectStretchs_lines(row_count, col_count, node_edge_size, hor_island_dist, ver_island_dist):
  with open('parameterFiles/interconnectStretchsLines.txt', "w") as fo:
    count = 0
    for i in range(row_count):
      for j in range(col_count-1):
        left_node = count
        right_node = count+1
        fo.writelines("sqrt((YatX($x_coords_end$,{}) - YatX($x_coords_end$,{})-{})^2 + (YatX($y_coords_end$,{}) - YatX($y_coords_end$,{}))^2) - {}\n".format(right_node, left_node, hor_island_dist[i,j], right_node, left_node, node_edge_size))
        if j == col_count-2:
          count += 2
        else:
          count += 1
    count = 0
    for i in range(col_count):
      for j in range(row_count-1):
        up_node = count
        down_node = count+col_count
        fo.writelines("sqrt((YatX($x_coords_end$,{}) - YatX($x_coords_end$,{}))^2 + (YatX($y_coords_end$,{}) - YatX($y_coords_end$,{})-{})^2) - {}\n".format(up_node, down_node, up_node, down_node, ver_island_dist[j,i], node_edge_size))
        if j == row_count-2: #Last iteration
          count -= (row_count-1)*(col_count-1)
        else:
          count += col_count

def write_unique_deviations(row_count, col_count):
  with open('parameterFiles/unique_deviations_name.txt', "w") as fo:
    for i in range(row_count):
      for j in range(col_count):
        fo.writelines("xdev{},{}\n".format(i, j))
        fo.writelines("ydev{},{}\n".format(i, j))

  with open('parameterFiles/unique_deviations_formula.txt', "w") as fo:
    count = 0
    for i in range(row_count):
      for j in range(col_count):
        fo.writelines("abs(YatX($obj_x_corrected$,{})-YatX($x_coords_end$,{}))\n".format(count, count))
        fo.writelines("abs(YatX($obj_y_corrected$,{})-YatX($y_coords_end$,{}))\n".format(count, count))
        count += 1

  with open('parameterFiles/unique_total_deviations_name.txt', "w") as fo:
    for i in range(row_count):
      for j in range(col_count):
        fo.writelines("dev{},{}\n".format(i, j))

  with open('parameterFiles/unique_total_deviations_formula.txt', "w") as fo:
    count = 0
    for i in range(row_count):
      for j in range(col_count):
        fo.writelines("sqrt (abs(YatX($obj_x_corrected$,{})-YatX($x_coords_end$,{}))^2 + abs(YatX($obj_y_corrected$,{})-YatX($y_coords_end$,{}))^2 )\n".format(count, count, count, count))
        count += 1

def read_optimus_RSM(filename):
  nonlin_model_params = list()
  folder = Path(curpath).parents[0]
  folder = os.path.join(folder, "nonlinearStiffness", "summary&model_files")
  file = os.path.join(folder, filename)
  with open (file, "r") as fo:
    record = False
    counter = 0
    for line in fo:
      if record and counter % 10 != 0:
        nonlin_model_params.append(float(line.split(":")[1]))
        counter += 1
      elif record and counter % 10 == 0:
        nonlin_model_params.append (float(line.split (":")[1]))
        record = False
      if line == "  Model terms:\n":
        record = True
        counter += 1


    nonlin_model_params = np.asarray(nonlin_model_params).reshape((10,10))
    return nonlin_model_params
