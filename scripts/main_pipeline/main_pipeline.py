# main_pipeline.py
import subprocess

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        raise Exception(f"Failed to run {script_name}")
    else:
        print(f"Successfully ran {script_name}: {result.stdout}")

def main():
    try:
        # Step 1: Data Preprocessing
        print("Running Data Preprocessing...")
        run_script('main_data_preprocessing.py')

        # Step 2: Model Training
        print("Running Model Training...")
        run_script('main_model_training.py')

        # Step 3: Model Evaluation
        print("Running Model Evaluation...")
        run_script('main_model_evaluation.py')

        print("Pipeline executed successfully!")

    except Exception as e:
        print(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()