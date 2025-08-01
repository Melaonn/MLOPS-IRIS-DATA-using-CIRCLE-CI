from src.data_preprocessing import DataProcessing
from src.model_training import ModelTraining

if __name__ == "__main__":
    data_processor = DataProcessing("artifacts/raw/data.csv")
    data_processor.run()

    trainer =  ModelTraining()
    trainer.run()

