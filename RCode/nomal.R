excel_file_path <- "G:BDE_VU/GreenLab/data/BatteryManager_Babylon/2023.10.17_WebGPU_Babylon/GPU_Aggregated_Results_Batterymanager.csv"


column_name <- "Energy_trapz"


data <- read.csv(excel_file_path)


column_data <- data[[column_name]]

# Shapiro-Wilk test
shapiro_result <- shapiro.test(column_data)

# print results
cat("Shapiro-Wilk results:\n")
print(shapiro_result)

# judge if conform to a normal distribution
alpha_level <- 0.05
if (shapiro_result$p.value < alpha_level) {
  cat("the groups of data did not conform to a nomal distribution (p-value < 0.05)\n")
} else {
  cat("the groups of data possbly conform to a nomal distribution (p-value >= 0.05)\n")
}

# drawing a Q-Q plot
qqnorm(column_data)
qqline(column_data)

library(rcompanion)

plotNormalHistogram( column_data, prob = FALSE,
                     main = "Energy Consumption Distribution of WebGPU ",
                     length = 1000,xlim = c(0.1, 0.4),breaks = 10 )


