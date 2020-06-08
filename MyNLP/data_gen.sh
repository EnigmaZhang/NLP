USR_DIR=./usr_dir
DATA_DIR=./data_dir
PROBLEM=translate_up2down

t2t-datagen \
  --t2t_usr_dir=${USR_DIR} \
  --data_dir=${DATA_DIR} \
  --problem=${PROBLEM}