# Arcane incantation to print all the other targets, from https://stackoverflow.com/a/26339924
help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Install exact Python and CUDA versions
conda-update:
	conda env update --prune -f environment.yml
	echo "!!!RUN RIGHT NOWconda:\nconda activate fastapi-streamlit-ml"

# Compile and install exact python packages
poetry:
	poetry install

DBPW?=mysecretpassword

# run a PostgreSql container with Docker
run-db:
	docker run --name banknote_postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DBPW)' -e POSTGRES_DB=banknote -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres

# # Example training command
# train-mnist-cnn-ddp:
# 	python training/run_experiment.py --max_epochs=10 --gpus=-1 --accelerator=ddp --num_workers=20 --data_class=MNIST --model_class=CNN

# Lint
lint:
	bash ./tasks/lint.sh