install.packages("caret")
library(caret)

train_original <- read.csv('../../data/train.csv')
train_normalized <- read.csv('train_normalized.csv')
train_All <- data.frame(Response=train_original$Response, train_normalized)

#===
smp_size <- floor(0.8 * nrow(train_All))
set.seed(123)
train_sample_rows_numbers <- sample(seq_len(nrow(train_All)), size = smp_size)
#
train_large  <- train_All[train_sample_rows_numbers, ]
train_mini   <- train_All[sample(1:nrow(train_All), 1000), ]
#
valid_large  <- train_All[-train_sample_rows_numbers, ]
valid_mini <- valid_large[sample(1:nrow(valid_large),1000),]

#=== 
write.csv(train_large, "train.csv",row.names=F)
write.csv(train_mini,  "train_mini.csv",row.names=F)
write.csv(valid_large, "valid.csv",row.names=F)
write.csv(valid_mini,  "valid_1000.csv",row.names=F)