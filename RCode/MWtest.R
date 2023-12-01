#excel_file_path1 <- "G:BDE_VU/GreenLab/data/BatteryManager_Babylon/2023.10.16_WebGL_Babylon/GL_Aggregated_Results_Batterymanager.csv"
#excel_file_path2 <- "G:BDE_VU/GreenLab/data/BatteryManager_Babylon/2023.10.17_WebGPU_Babylon/GPU_Aggregated_Results_Batterymanager.csv"

excel_file_path1 <- "G:BDE_VU/GreenLab/data/performance_final/toji/GL1/frame_time.csv"
excel_file_path2 <- "G:BDE_VU/GreenLab/data/performance_final/toji/GPU1/frame_time.csv"

#column_name <- "Energy_trapz"
#column_name <- "avg_memory"
column_name <- "delayed_rate"

data1 <- read.csv(excel_file_path1)
data2 <- read.csv(excel_file_path2)

column_data1 <- data1[[column_name]]
column_data2 <- data2[[column_name]]

result = wilcox.test(column_data1, column_data2)

cat("Wilcoxon Rank Sum Test Results:\n")
cat("W Statistic:", result$statistic, "\n")
cat("P-value:", result$p.value, "\n")


if (result$p.value < 0.05) {
  cat("Conclusion: There is a significant difference between the two groups.\n")
} else {
  cat("Conclusion: There is no significant difference between the two groups.\n")
}