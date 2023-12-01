#excel_file_path1 <- "G:BDE_VU/GreenLab/data/Batterymanager/WebGL/GL_Aggregated_Results_Batterymanager.csv"
#excel_file_path2 <- "G:BDE_VU/GreenLab/data/Batterymanager/WebGPU/GPU_Aggregated_Results_Batterymanager.csv"

#excel_file_path1 <- "G:BDE_VU/GreenLab/data/BatteryManager_Babylon/2023.10.16_WebGL_Babylon/GL_Aggregated_Results_Batterymanager.csv"
#excel_file_path2 <- "G:BDE_VU/GreenLab/data/BatteryManager_Babylon/2023.10.17_WebGPU_Babylon/GPU_Aggregated_Results_Batterymanager.csv"
#excel_file_path1 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GL2/memory.csv"
#excel_file_path2 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GPU2/memory.csv"

excel_file_path1 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GL2/frame_time.csv"
excel_file_path2 <- "G:BDE_VU/GreenLab/data/performance_final/babylon/GPU2/frame_time.csv"

#column_name <- "Energy_trapz"
column_name <- "delayed_rate"
#column_name <- "avg_memory"


data1 <- read.csv(excel_file_path1)
data2 <- read.csv(excel_file_path2)

column_data1 <- data1[[column_name]]
column_data2 <- data2[[column_name]]

# merge into one list
data <- list(Group1 = column_data1, Group2 = column_data2)

# plot
boxplot(data, 
        ylim = c(0.1, 0.35),
        main = "Boxplot:Energy Consumption Values",
        xlab = "Api Groups",
        ylab = "Energy Consumption(KJ)",
        col = c("lightblue", "lightgreen"),
        names = c("WebGL", "WebGPU"))

# max value
max_value <- max(column_data1)

# min value
min_value <- min(column_data1)

# mean
average <- mean(column_data1)

# median value
median_value <- median(column_data1)

# 1st Qu.
q1 <- quantile(column_data1, 0.25)

# 3rd Qu.
q3 <- quantile(column_data1, 0.75)

# standard deviation
std_dev <- sd(column_data1)


# 输出结果
cat("max value:", max_value, "\n")
cat("min value:", min_value, "\n")
cat("mean:", average, "\n")
cat("median:", median_value, "\n")
cat("1st:", q1, "\n")
cat("3rd:", q3, "\n")
cat("standard deviation:", std_dev, "\n")
