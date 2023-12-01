library(effsize)

excel_file_path1 <- "G:BDE_VU/GreenLab/resit/data/GL_combined_averaged_data.csv"
excel_file_path2 <- "G:BDE_VU/GreenLab/resit/data/GPU_combined_averaged_data.csv"

column_name <- "GPU_mem"

data1 <- read.csv(excel_file_path1)
data2 <- read.csv(excel_file_path2)

column_data1 <- data1[[column_name]]
column_data2 <- data2[[column_name]]


group1 <- column_data1
group2 <- column_data2


cliffs_delta_result <- cliff.delta(group1, group2)


print(cliffs_delta_result)