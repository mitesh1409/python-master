import os
import swimclub

def main():
    data_files = os.listdir(swimclub.FOLDER)

    if ".DS_Store" in data_files:
        data_files.remove(".DS_Store")

    processed_data = []
    for n, data_file in enumerate(data_files, 1):
        print(f"{n} Data file: {data_file}")
        processed_data.append(swimclub.process_swim_data(data_file))
        print("Processed\n\n")

    print(f"Total {len(data_files)} data files processed successfully.")

    print(processed_data)

if __name__ == "__main__":
    main()
