from textSummarization.pipeline.Stage_01_Data_Ingestion import DataIngestionTrainingPipeline
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