from textSummarization.pipeline.Stage_01_Data_Ingestion import DataIngestionTrainingPipeline
from textSummarization.pipeline.Stage_02_Data_Validation import DataValidationTrainingPipeline
from textSummarization.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> {STAGE_NAME} Started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> {STAGE_NAME} Completed <<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> {STAGE_NAME} Started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> {STAGE_NAME} Completed <<<<<<<\n\n")

except Exception as e:
    logger.exception(e)
    raise e