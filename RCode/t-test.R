excel_file_path1 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GL2/frame_time.csv"
excel_file_path2 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GPU2/frame_time.csv"

column_name <- "delayed_rate"

data1 <- read.csv(excel_file_path1)
data2 <- read.csv(excel_file_path2)

column_data1 <- data1[[column_name]]
column_data2 <- data2[[column_name]]

t_test_result <- t.test(column_data1, column_data2)

print(t_test_result)